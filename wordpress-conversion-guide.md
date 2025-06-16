# WordPress Theme Conversie Gids
## Advocatenkantoor Missault - Van Volcem

Deze gids legt uit hoe je de HTML website kunt omzetten naar een WordPress theme.

## 🎯 Conversie Opties

### Optie 1: WordPress Theme Maken (Geavanceerd)

**Benodigde bestanden voor WordPress theme:**
```
wp-theme/
├── style.css           # Theme stylesheet met header info
├── index.php          # Hoofdtemplate
├── header.php         # Header sectie
├── footer.php         # Footer sectie
├── functions.php      # Theme functies
├── page.php           # Pagina template
├── single.php         # Post template
├── screenshot.png     # Theme preview
└── assets/
    ├── css/
    ├── js/
    └── images/
```

**Stappen:**
1. Converteer HTML naar PHP templates
2. Integreer WordPress functies
3. Maak admin customizer opties
4. Test en upload naar WordPress

### Optie 2: Page Builder Recreatie (Eenvoudig)

**Gebruik Elementor/Divi/Gutenberg:**
1. Installeer page builder plugin
2. Recreëer design met drag & drop
3. Kopieer content over
4. Pas styling aan

### Optie 3: Static Site Plugin (Hybride)

**Simply Static Plugin:**
1. Installeer WordPress lokaal
2. Bouw site met page builder
3. Exporteer als statische HTML
4. Host waar je wilt

## 🛠️ WordPress Theme Conversie

### Stap 1: Theme Header (style.css)
```css
/*
Theme Name: Advocatenkantoor Missault - Van Volcem
Description: Professional law firm website theme
Version: 1.0
Author: Jean Decroos
*/

/* Bestaande CSS hier... */
```

### Stap 2: PHP Templates

**header.php:**
```php
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php wp_title('|', true, 'right'); bloginfo('name'); ?></title>
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
```

**index.php:**
```php
<?php get_header(); ?>

<!-- Hero Section -->
<section id="home" class="hero">
    <div class="hero-content">
        <h1><?php bloginfo('name'); ?><br>
        <span class="highlight"><?php bloginfo('description'); ?></span></h1>
        <!-- Rest van hero content -->
    </div>
</section>

<?php get_footer(); ?>
```

**functions.php:**
```php
<?php
function advocatenkantoor_theme_setup() {
    // Theme support
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    
    // Enqueue scripts and styles
    wp_enqueue_style('theme-style', get_stylesheet_uri());
    wp_enqueue_script('theme-script', get_template_directory_uri() . '/assets/js/script.js', array(), '1.0', true);
}
add_action('after_setup_theme', 'advocatenkantoor_theme_setup');
?>
```

## 🎨 WordPress Customizer Integratie

**Voeg customizer opties toe:**
```php
function advocatenkantoor_customize_register($wp_customize) {
    // Hero Section
    $wp_customize->add_section('hero_section', array(
        'title' => 'Hero Section',
        'priority' => 30,
    ));
    
    $wp_customize->add_setting('hero_title');
    $wp_customize->add_control('hero_title', array(
        'label' => 'Hero Title',
        'section' => 'hero_section',
        'type' => 'text',
    ));
}
add_action('customize_register', 'advocatenkantoor_customize_register');
```

## 📧 Contact Form Integration

**WordPress Contact Form 7:**
```php
// In template
echo do_shortcode('[contact-form-7 id="123" title="Contact form"]');
```

**Gravity Forms:**
```php
// In template
gravity_form(1, false, true);
```

## 🚀 Deployment Opties

### 1. WordPress.com Business
- Upload theme via admin
- Activeer en configureer
- Eigen domein koppelen

### 2. Zelf-gehoste WordPress
- Upload via FTP naar `/wp-content/themes/`
- Activeer in admin dashboard
- Configureer via customizer

### 3. WordPress Multisite
- Network activeer theme
- Beschikbaar voor alle sites

## 💡 Aanbevelingen

**Voor Advocatenkantoor:**

1. **Eenvoudigste:** Gebruik Elementor Pro
   - Importeer HTML design
   - Drag & drop interface
   - Geen coding nodig

2. **Professioneel:** Custom theme ontwikkeling
   - Volledige controle
   - WordPress CMS voordelen
   - Toekomstbestendig

3. **Hybride:** Static site + WordPress headless
   - Behoud huidige snelheid
   - WordPress content management
   - API-driven updates

## 🔧 Benodigde Skills

**Voor theme conversie:**
- PHP kennis
- WordPress template hierarchy
- WordPress hooks/filters
- CSS/JavaScript integratie

**Voor page builder:**
- WordPress admin kennis
- Page builder ervaring
- Design eye voor recreatie

## 📞 Ondersteuning

**WordPress ontwikkelaars:**
- Lokale WordPress developers
- Freelance platforms (Upwork, Fiverr)
- WordPress agencies

**Kosten inschatting:**
- Theme conversie: €500-1500
- Page builder setup: €200-500
- Onderhoud: €50-100/maand

## 🎯 Conclusie

**Beste optie voor advocatenkantoor:**
1. Start met huidige GitHub Pages hosting (gratis)
2. Test en verfijn de website
3. Later eventueel WordPress conversie overwegen
4. Focus eerst op content en SEO optimalisatie

De huidige HTML website is al professioneel en snel - WordPress toevoegen is alleen nodig als je regelmatig content wilt bijwerken zonder technische kennis. 