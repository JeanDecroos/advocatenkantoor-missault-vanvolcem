#!/bin/bash

# Advocatenkantoor Missault - Van Volcem Website Server
# Shell script voor macOS/Linux

# Kleuren voor output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo ""
echo "========================================================"
echo "   Advocatenkantoor Missault - Van Volcem Website"
echo "========================================================"
echo ""

# Functie om te controleren of een commando bestaat
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Controleer of Python beschikbaar is
if ! command_exists python3 && ! command_exists python; then
    echo -e "${RED}❌ Python is niet geïnstalleerd${NC}"
    echo ""
    echo -e "${YELLOW}💡 Installeer Python:${NC}"
    echo "   macOS: brew install python3"
    echo "   Ubuntu/Debian: sudo apt install python3"
    echo "   CentOS/RHEL: sudo yum install python3"
    echo ""
    exit 1
fi

# Bepaal welke Python versie te gebruiken
if command_exists python3; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

echo -e "${GREEN}✅ Python gevonden: $($PYTHON_CMD --version)${NC}"

# Controleer of bestanden bestaan
missing_files=()

if [ ! -f "index.html" ]; then
    missing_files+=("index.html")
fi

if [ ! -f "styles.css" ]; then
    missing_files+=("styles.css")
fi

if [ ! -f "script.js" ]; then
    missing_files+=("script.js")
fi

if [ ${#missing_files[@]} -ne 0 ]; then
    echo -e "${RED}❌ Benodigde website bestanden ontbreken:${NC}"
    for file in "${missing_files[@]}"; do
        echo "   - $file"
    done
    echo ""
    echo "Zorg ervoor dat alle bestanden in dezelfde map staan als dit script."
    exit 1
fi

echo -e "${GREEN}✅ Alle bestanden gevonden!${NC}"
echo ""

# Maak script uitvoerbaar als het dat nog niet is
chmod +x "$0" 2>/dev/null

echo -e "${BLUE}🚀 Website server wordt gestart...${NC}"
echo -e "${YELLOW}💡 De website opent automatisch in je browser${NC}"
echo -e "${YELLOW}🛑 Druk Ctrl+C om de server te stoppen${NC}"
echo ""

# Functie om de server te stoppen
cleanup() {
    echo ""
    echo ""
    echo -e "${GREEN}✅ Server afgesloten${NC}"
    exit 0
}

# Trap Ctrl+C
trap cleanup INT

# Start server
if [ -f "run-server.py" ]; then
    echo -e "${BLUE}📡 Start geavanceerde server...${NC}"
    $PYTHON_CMD run-server.py
else
    echo -e "${BLUE}📡 Start eenvoudige HTTP server...${NC}"
    
    # Zoek beschikbare poort
    PORT=8000
    while lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; do
        PORT=$((PORT + 1))
    done
    
    echo -e "${GREEN}🌐 Server draait op: http://localhost:$PORT${NC}"
    echo -e "${GREEN}📁 Directory: $(pwd)${NC}"
    echo ""
    
    # Open browser (probeer verschillende browsers)
    if command_exists open; then
        # macOS
        open "http://localhost:$PORT" 2>/dev/null &
    elif command_exists xdg-open; then
        # Linux
        xdg-open "http://localhost:$PORT" 2>/dev/null &
    elif command_exists firefox; then
        firefox "http://localhost:$PORT" 2>/dev/null &
    elif command_exists google-chrome; then
        google-chrome "http://localhost:$PORT" 2>/dev/null &
    fi
    
    # Start Python HTTP server
    $PYTHON_CMD -m http.server $PORT
fi 