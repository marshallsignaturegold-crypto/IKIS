# Phalanx Swarm v2.0-OMEGA — Inter-Agent Communication Protocol Specification

## 1. Overview

This document defines the messaging layer enabling structured, secure, and reliable communication among the 30 agents of the Phalanx Swarm v2.0-OMEGA. All agents communicate over gRPC with Protocol Buffers (protobuf) payloads, secured with mutual TLS (mTLS). The protocol supports direct addressing, pub/sub, broadcast, consensus, whisper, and alert channels.

---

## 2. Message Types

| Type | Purpose | Direction | Payload Constraints |
|------|---------|-----------|---------------------|
| **COMMAND** | Instruct an agent to perform an action | Unicast, may chain | Requires `command_id`, `deadline`, `authority_signature` |
| **QUERY** | Request information or a computation | Unicast, synchronous | Requires `query_id`, `max_wait_ms`, `response_schema_hint` |
| **RESPONSE** | Reply to a `QUERY` or `COMMAND` | Unicast, back to sender | Must reference `query_id` or `command_id`; includes `confidence_score` |
| **ALERT** | High-priority signal for anomaly or threshold breach | Unicast or multicast | Auto-escalates if unacknowledged; includes `severity`, `ack_deadline` |
| **BROADCAST** | General information to all agents or a group | Multicast / pubsub | Must include `topic_tag`; no guaranteed individual delivery |
| **WHISPER** | Confidential, need-to-know agent-to-agent message | Unicast, encrypted | Uses ephemeral session keys; no logging by default; requires `clearance_level` |
| **CONSENSUS** | Propose, vote, or ratify a collective decision | Coalition-scoped | Requires `proposal_id`, `quorum_fraction`, `voting_deadline` |

---

## 3. Routing Logic

### 3.1 Addressing Model
- **Agent ID**: `A-001`, `B-003`, etc. (`{group}-{seq}`).
- **Group ID**: `ALPHA`, `BETA`, etc.
- **Topic Tag**: Hierarchical labels like `infra.deploy`, `security.alert`, `research.gap`.

### 3.2 Routing Table (managed by Nexus O-002)
- `direct(agent_id)`: Unicast to a specific agent via persistent gRPC stream.
- `pubsub(topic_tag)`: Publish to all subscribers of a topic.
- `broadcast(group_id, scope)`: Scoped broadcast (`scope`: `group`, `swarm`, `coalition`).
- `consensus(coalition_id)`: Routed to all members of a coalition.
- `whisper(target_agent_id, clearance)`: Route through encrypted tunnel with ephemeral key exchange.
- `alert(target_list, severity)`: Overrides normal routing; uses redundant paths if primary is down.

### 3.3 Routing Algorithm
1. **Resolve**: Look up destination(s) in the Nexus routing table.
2. **Filter**: Apply capability, clearance, and health filters.
3. **Load Balance**: For `QUERY` and `COMMAND` to interchangeable agents, use weighted round-robin.
4. **Encrypt**: Apply mTLS + per-message encryption (AES-256-GCM).
5. **Deliver**: Transmit over the chosen channel.
6. **Dead Letter**: On delivery failure, route to the Dead Letter Queue (DLQ) for analysis.

---

## 4. Priority Levels

| Level | Name | Latency Target | Preemption | Use Case |
|-------|------|----------------|------------|----------|
| 0 | **CRITICAL** | < 50ms | Can preempt all others | System failure, safety breach, deadlock |
| 1 | **URGENT** | < 200ms | Can preempt NORMAL | Active threat, deadline breach, resource starvation |
| 2 | **NORMAL** | < 1s | Can preempt BACKGROUND | Standard task coordination, queries, responses |
| 3 | **BACKGROUND** | < 5s | Can preempt SPECULATIVE | Indexing, compaction, long-running analytics |
| 4 | **SPECULATIVE** | Best-effort | None | Pre-computation, cache warming, hypothesis testing |

Priority is encoded in the message envelope as `priority_level`. Agents must maintain per-priority queues and preempt lower-priority work when a higher-priority message arrives (up to agent-specific limits to avoid starvation).

---

## 5. Delivery Guarantees

| Guarantee | Applicable Types | Implementation | Retry Policy |
|-----------|------------------|----------------|--------------|
| **At-most-once** | `WHISPER`, `BROADCAST` (best-effort), `ALERT` (initial) | Fire-and-forget; deduplication via `message_id` at receiver | No retries |
| **At-least-once** | `COMMAND`, `QUERY`, `RESPONSE`, `BROADCAST` (reliable) | Acknowledgment + retry with exponential backoff | 3 retries, max 5s total |
| **Exactly-once** | `CONSENSUS`, `AUDIT`, `COMMAND` (idempotent) | Deduplication + idempotency key + persistent log | Bounded retries until `deadline` or success |

### 5.1 Exactly-Once Idempotency
- Every `COMMAND` and `CONSENSUS` message carries an `idempotency_key` (UUID v4 + timestamp hash).
- Receivers maintain an idempotency log for `ttl = 24 hours`.
- Duplicate keys are acknowledged but not reprocessed.

### 5.2 Timeout and Cancellation
- All messages carry a `deadline` timestamp.
- If a message is not processed by `deadline`, the receiver must send a `CANCEL` or `TIMEOUT` response.
- The sender may reissue or escalate based on the deadline miss.

---

## 6. Encryption Model

### 6.1 Transport Layer
- **mTLS**: All agent-to-agent connections use mutual TLS with per-agent X.509 certificates signed by the swarm CA.
- **Certificate Rotation**: Automatic rotation every 30 days; grace period of 7 days.

### 6.2 Message Layer
- **AES-256-GCM**: Each message is encrypted with an ephemeral key derived via ECDH (secp256r1) between sender and receiver.
- **Nonce Management**: 96-bit nonces, monotonically incremented per stream; nonce reuse is a fatal protocol error.
- **Forward Secrecy**: Session keys are rotated every 1,000 messages or 1 hour, whichever comes first.

### 6.3 Trust Boundaries
- **Intra-Group**: Default clearance; no additional encryption beyond transport.
- **Inter-Group**: Message-level encryption required for `WHISPER` and `ALERT`.
- **Coalition**: Coalition-scoped ephemeral keys are generated by the coalition leader during formation.
- **Theta Group (Cipher, Vanguard, Reclaimer)**: Hardware-token-bound keys; additional HSM layer for `WHISPER`.
- **Omega Group (Apex, Nexus, Aegis)**: Admin-cert signed messages; messages signed by Apex require explicit acknowledgment from Aegis for destructive commands.

### 6.4 Audit & Non-Repudiation
- All messages (except `WHISPER`) are logged with a SHA-256 hash in the `Auditor` (D-003) immutable log.
- `WHISPER` logs only the existence (timestamp, sender, receiver) but not payload, unless both parties consent.

---

## 7. Dead Letter Handling

### 7.1 Dead Letter Queue (DLQ)
- Managed by Nexus (O-002) and monitored by Apex (O-001).
- Messages are moved to the DLQ if:
  - The destination agent is unreachable after 3 retries.
  - The destination agent rejects the message (capability mismatch, constraint violation, or security boundary breach).
  - The message deadline expires before delivery.

### 7.2 DLQ Processing
1. **Classify**: `routing_error`, `capability_error`, `security_error`, `timeout_error`.
2. **Alert**: `ALERT` sent to `Apex` and `Aegis` for security-related DLQ entries.
3. **Retry Routing**: For `routing_error`, attempt alternate path or wait for agent recovery.
4. **Escalation**: For `security_error`, escalate to `Aegis` and `Shield` for investigation.
5. **Audit**: All DLQ events are written to `Auditor` (D-003) with full message hash.
6. **TTL**: DLQ entries expire after 72 hours unless explicitly retained for forensics.

### 7.3 Agent Recovery and Re-Play
- When an agent comes back online after a failure, it must reconcile its state with `Chronos` (H-001) and `Hermes` (H-002).
- Unacknowledged messages that are still within deadline may be replayed from the DLQ with a new `delivery_attempt` count.
- Exactly-once messages use their `idempotency_key` to prevent double-processing during replay.

---

## 8. Message Schema (Protobuf Summary)

```protobuf
message SwarmEnvelope {
  string message_id = 1;           // UUID v4
  string correlation_id = 2;       // Links request/response pairs
  MessageType type = 3;            // enum: COMMAND, QUERY, RESPONSE, ALERT, BROADCAST, WHISPER, CONSENSUS
  int32 priority = 4;              // 0=CRITICAL, 4=SPECULATIVE
  string sender_id = 5;
  string target_id = 6;          // agent_id, group_id, coalition_id, or topic_tag
  string coalition_id = 7;         // optional, for coalition-scoped messages
  string topic_tag = 8;            // optional, for pub/sub
  bytes payload = 9;             // encrypted protobuf payload
  string idempotency_key = 10;     // for exactly-once semantics
  int64 deadline_ms = 11;          // Unix epoch ms
  string authority_signature = 12; // for COMMAND and CONSENSUS
  string clearance_level = 13;     // for WHISPER and ALERT
  map<string, string> metadata = 14;
}
```

---

## 9. Operational Guarantees

- **Throughput**: Nexus (O-002) must sustain >10,000 messages/second across all channels.
- **Latency**: p99 latency < 100ms for CRITICAL, < 500ms for NORMAL.
- **Availability**: If Nexus fails, agents fall back to a gossip protocol (udp-based) for heartbeats and basic broadcast, then self-organize a new Nexus election via `Chorus` (Z-004) consensus.
- **Observability**: All messages carry OpenTelemetry trace IDs for end-to-end tracing.

---

## 10. Version History

- **v2.0.0-OMEGA**: Current. Replaced v1.5 pub/sub with gRPC+protobuf. Introduced `WHISPER`, `CONSENSUS`, and exactly-once delivery. Added DLQ and HSM support for Theta group.
- **v1.5**: HTTP/REST + JSON. At-least-once only. No coalition encryption.
- **v1.0**: Basic socket-based messaging. No encryption, no guarantees.

---

*Document steward: O-002 Nexus | Review cycle: 30 days | Last updated: 2024-06-15*
