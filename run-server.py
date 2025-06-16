#!/usr/bin/env python3
"""
Advocatenkantoor Missault - Van Volcem Website Server
Een eenvoudige HTTP-server om de website lokaal te runnen.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# Server configuratie
PORT = 8000
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler met betere MIME types en error handling."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def end_headers(self):
        # Voeg security headers toe
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom logging voor betere output."""
        print(f"[{self.log_date_time_string()}] {format % args}")

def check_files():
    """Controleer of alle benodigde bestanden aanwezig zijn."""
    required_files = ['index.html', 'styles.css', 'script.js']
    missing_files = []
    
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Fout: De volgende bestanden ontbreken:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nZorg ervoor dat alle website bestanden in dezelfde map staan als dit script.")
        return False
    
    print("✅ Alle benodigde bestanden gevonden!")
    return True

def find_available_port(start_port=8000):
    """Zoek een beschikbare poort."""
    import socket
    
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, port))
                return port
        except OSError:
            continue
    
    return None

def start_server():
    """Start de HTTP-server."""
    global PORT
    
    # Controleer bestanden
    if not check_files():
        return False
    
    # Zoek beschikbare poort
    available_port = find_available_port(PORT)
    if available_port is None:
        print(f"❌ Fout: Geen beschikbare poort gevonden vanaf {PORT}")
        return False
    
    PORT = available_port
    
    try:
        # Start server
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            server_url = f"http://{HOST}:{PORT}"
            
            print("🏛️  Advocatenkantoor Missault - Van Volcem Website Server")
            print("=" * 60)
            print(f"🌐 Server draait op: {server_url}")
            print(f"📁 Directory: {os.getcwd()}")
            print(f"🚀 Server gestart op poort {PORT}")
            print("=" * 60)
            print("💡 Tips:")
            print("   - Druk Ctrl+C om de server te stoppen")
            print("   - De website opent automatisch in je browser")
            print("   - Wijzigingen in bestanden zijn direct zichtbaar na refresh")
            print("=" * 60)
            
            # Open browser automatisch
            try:
                webbrowser.open(server_url)
                print(f"🔗 Browser geopend: {server_url}")
            except Exception as e:
                print(f"⚠️  Kon browser niet automatisch openen: {e}")
                print(f"   Open handmatig: {server_url}")
            
            print("\n📊 Server logs:")
            print("-" * 30)
            
            # Start server
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Server gestopt door gebruiker")
        return True
    except Exception as e:
        print(f"\n❌ Server fout: {e}")
        return False

def main():
    """Hoofdfunctie."""
    print("🏛️  Advocatenkantoor Website Server Starter")
    print("Bezig met opstarten...\n")
    
    try:
        success = start_server()
        if success:
            print("✅ Server succesvol afgesloten")
        else:
            print("❌ Server gestopt met fouten")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Onverwachte fout: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 