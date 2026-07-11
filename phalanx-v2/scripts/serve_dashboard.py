#!/usr/bin/env python3
"""Minimal HTTP server to serve the Phalanx dashboard."""

import http.server
import os
import socketserver
import sys

PORT = int(os.environ.get("PHALANX_PORT", "8080"))
UI_DIR = os.path.join(os.path.dirname(__file__), "..", "ui")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=UI_DIR, **kwargs)

    def log_message(self, fmt, *args):
        # Quieter logging
        pass

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving Phalanx dashboard at http://localhost:{PORT}/dashboard.html")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            sys.exit(0)
