#!/usr/bin/env python3
"""
Cross-platform starter voor Advocatenkantoor Missault - Van Volcem Website
Detecteert automatisch het besturingssysteem en start het juiste script.
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def detect_os():
    """Detecteer het besturingssysteem."""
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system in ["darwin", "linux"]:
        return "unix"
    else:
        return "unknown"

def check_python():
    """Controleer of Python correct geïnstalleerd is."""
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 6:
            return True
        else:
            print(f"❌ Python {version.major}.{version.minor} gevonden, maar Python 3.6+ is vereist")
            return False
    except:
        return False

def run_website():
    """Start de website server."""
    print("🏛️  Advocatenkantoor Missault - Van Volcem")
    print("=" * 50)
    print("🚀 Website starter wordt geladen...")
    print()
    
    # Controleer Python versie
    if not check_python():
        print("💡 Installeer een nieuwere versie van Python van https://python.org")
        input("Druk Enter om af te sluiten...")
        return False
    
    # Detecteer OS
    os_type = detect_os()
    current_dir = Path.cwd()
    
    print(f"🖥️  Besturingssysteem: {platform.system()}")
    print(f"🐍 Python versie: {sys.version.split()[0]}")
    print(f"📁 Directory: {current_dir}")
    print()
    
    # Controleer of website bestanden bestaan
    required_files = ["index.html", "styles.css", "script.js"]
    missing_files = [f for f in required_files if not Path(f).exists()]
    
    if missing_files:
        print("❌ Website bestanden ontbreken:")
        for file in missing_files:
            print(f"   - {file}")
        print()
        print("Zorg ervoor dat alle website bestanden in dezelfde map staan.")
        input("Druk Enter om af te sluiten...")
        return False
    
    print("✅ Alle website bestanden gevonden!")
    print()
    
    # Kies en start het juiste script
    try:
        if os_type == "windows":
            # Windows: probeer batch script
            if Path("run-website.bat").exists():
                print("🪟 Start Windows batch script...")
                subprocess.run(["run-website.bat"], shell=True)
            else:
                print("📡 Start Python HTTP server...")
                start_python_server()
                
        elif os_type == "unix":
            # macOS/Linux: probeer shell script
            if Path("run-website.sh").exists():
                print("🐧 Start Unix shell script...")
                subprocess.run(["./run-website.sh"], shell=True)
            else:
                print("📡 Start Python HTTP server...")
                start_python_server()
                
        else:
            print("❓ Onbekend besturingssysteem, start Python server...")
            start_python_server()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Gestopt door gebruiker")
        return True
    except Exception as e:
        print(f"\n❌ Fout bij starten: {e}")
        print("📡 Probeer Python HTTP server als fallback...")
        start_python_server()
    
    return True

def start_python_server():
    """Start een eenvoudige Python HTTP server als fallback."""
    import http.server
    import socketserver
    import webbrowser
    from threading import Timer
    
    PORT = 8000
    
    # Zoek beschikbare poort
    import socket
    for port in range(8000, 8100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                PORT = port
                break
        except OSError:
            continue
    
    server_url = f"http://localhost:{PORT}"
    
    print(f"🌐 Server start op: {server_url}")
    print("💡 De website opent automatisch in je browser")
    print("🛑 Druk Ctrl+C om te stoppen")
    print()
    
    # Open browser na 2 seconden
    def open_browser():
        try:
            webbrowser.open(server_url)
            print(f"🔗 Browser geopend: {server_url}")
        except:
            print(f"⚠️  Open handmatig: {server_url}")
    
    Timer(2.0, open_browser).start()
    
    # Start server
    try:
        with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
            print("📊 Server logs:")
            print("-" * 20)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server gestopt")

def main():
    """Hoofdfunctie."""
    try:
        success = run_website()
        if not success:
            sys.exit(1)
    except Exception as e:
        print(f"❌ Onverwachte fout: {e}")
        input("Druk Enter om af te sluiten...")
        sys.exit(1)

if __name__ == "__main__":
    main() 