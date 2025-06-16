# Advocatenkantoor Missault - Van Volcem Website

Een moderne, elegante website voor advocatenkantoor Missault - Van Volcem in Brugge, België.

## Overzicht

Deze website is ontworpen met focus op **integriteit** en **betrouwbaarheid** - de kernwaarden van advocatuur. De site biedt een professionele uitstraling met moderne UX-principes en is volledig responsief voor alle apparaten.

## Kenmerken

### 🎨 Design & UX
- **Elegante, professionele uitstraling** die vertrouwen uitstraalt
- **Moderne typografie** met Playfair Display voor koppen en Inter voor tekst
- **Subtiele kleurenpalet** met donkerblauw (#1a365d) als primaire kleur en goud (#d4af37) als accent
- **Volledig responsief** design voor desktop, tablet en mobiel
- **Smooth scrolling** en subtiele animaties

### 📱 Functionaliteiten
- **Mobiele navigatie** met hamburger menu
- **Contactformulier** met validatie
- **Scroll-to-top** knop
- **Actieve navigatie** highlighting
- **Notificatiesysteem** voor formulier feedback

### 🏛️ Inhoud
- **7 Specialisaties**: Handelsrecht, Fiscaal Recht, Sociaal Recht, Bouwrecht, Verkeersrecht, Familierecht, Ondernemingen in Moeilijkheden
- **Advocaten profiel**: Francis Missault en Mercedes Van Volcem (zaakvoerders)
- **Contactinformatie**: Koningin Elisabethlaan 34, Brugge
- **Over ons sectie** met bedrijfsstatistieken

## Bestandsstructuur

```
/
├── index.html          # Hoofdpagina
├── styles.css          # CSS styling
├── script.js           # JavaScript functionaliteit
├── start.py            # Cross-platform starter (AANBEVOLEN)
├── run-server.py       # Geavanceerde Python HTTP server
├── run-website.bat     # Windows batch script
├── run-website.sh      # macOS/Linux shell script
└── README.md           # Deze documentatie
```

## Hoe te gebruiken

### 🚀 Website Starten (Aanbevolen)

**Optie 1: Automatische Starter (Alle besturingssystemen)**
```bash
python3 start.py
# of op Windows:
python start.py
```

**Optie 2: Platform-specifieke scripts**

**Windows:**
```cmd
run-website.bat
```

**macOS/Linux:**
```bash
./run-website.sh
```

**Optie 3: Geavanceerde Python Server**
```bash
python3 run-server.py
```

**Optie 4: Eenvoudige Python Server**
```bash
python3 -m http.server 8000
```

### 📱 Gebruik
1. **Automatisch**: De website opent automatisch in je browser
2. **Handmatig**: Ga naar `http://localhost:8000` in je browser
3. **Navigatie**: Gebruik het menu om tussen secties te navigeren
4. **Contactformulier**: Vul het formulier in voor contact (simulatie)
5. **Mobiel**: De site is volledig responsief voor mobiele apparaten
6. **Stoppen**: Druk `Ctrl+C` in de terminal om de server te stoppen

## Technische Details

### HTML
- Semantische HTML5 structuur
- Toegankelijkheidsfeatures (ARIA labels, focus states)
- SEO-geoptimaliseerd met meta tags

### CSS
- CSS Custom Properties (CSS variabelen)
- Flexbox en CSS Grid voor layout
- Mobile-first responsive design
- Smooth transitions en hover effecten

### JavaScript
- Vanilla JavaScript (geen frameworks)
- Event listeners voor interactiviteit
- Form validatie
- Intersection Observer voor animaties
- Local storage voor toekomstige uitbreidingen

## Kleurenpalet

- **Primair**: #1a365d (Donkerblauw)
- **Secundair**: #2c5282 (Blauw)
- **Accent**: #d4af37 (Goud)
- **Tekst Donker**: #2d3748
- **Tekst Licht**: #718096
- **Achtergrond**: #f7fafc

## Typografie

- **Koppen**: Playfair Display (serif)
- **Tekst**: Inter (sans-serif)
- **Iconen**: Font Awesome 6.0

## Browser Ondersteuning

- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+

## Toekomstige Uitbreidingen

- **CMS integratie** voor eenvoudig contentbeheer
- **Blog sectie** voor juridische artikelen
- **Nieuwsbrief aanmelding** functionaliteit
- **Meertalige ondersteuning** (Nederlands/Frans/Engels)
- **Online afspraak systeem**
- **Cliënt portal** voor bestaande klanten

## Aanpassingen

### Contactgegevens wijzigen
Bewerk de contactinformatie in `index.html` rond regel 200-230.

### Kleuren aanpassen
Wijzig de CSS variabelen in `styles.css` rond regel 8-18.

### Inhoud bijwerken
Alle tekst kan aangepast worden in `index.html`.

## Deployment

Voor productie:
1. Upload alle bestanden naar webserver
2. Configureer contactformulier backend
3. Voeg Google Analytics toe (optioneel)
4. Configureer SSL certificaat

## Contact

Voor vragen over deze website implementatie, neem contact op met de ontwikkelaar.

---

**© 2024 Advocatenkantoor Missault - Van Volcem. Alle rechten voorbehouden.** 