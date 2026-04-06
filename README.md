# pf.rec.ooo

Product-oriented resume site for Xue Juntao.

## Overview

A minimal, single-page resume website built with pure HTML/CSS/JavaScript. Features responsive design with separate mobile and desktop experiences.

**Live site:** [pf.rec.ooo](https://pf.rec.ooo)

## Structure

```
pf_rec/
├── index.html          # Desktop version (auto-redirects mobile)
├── mobile/
│   └── index.html      # Mobile-optimized version
├── CNAME              # GitHub Pages custom domain
├── redrec32.png        # Favicon
└── XueJuntao_ProductEngineer.pdf  # Resume PDF
```

## Features

- **Responsive Design**: Automatic mobile redirect (≤768px)
- **Theme Toggle**: Light/dark mode support
- **Copy-to-Clipboard**: Quick copy for email and GitHub links
- **Smooth Navigation**: Section anchors with smooth scrolling
- **Minimal UI**: Clean typography, monospace font, red accent color

## Tech Stack

- Pure HTML/CSS/JavaScript (no frameworks)
- CSS Variables for theming
- Mobile-first responsive design
- GitHub Pages hosting

## Deployment

This site is hosted on GitHub Pages with custom domain `pf.rec.ooo`.

### DNS Configuration (Porkbun)

```
Type: CNAME
Host: pf
Answer: recdnd.github.io
TTL: Auto
```

### GitHub Pages Settings

- Custom domain: `pf.rec.ooo`
- Enforce HTTPS: ✅ Enabled

## Development

1. Clone the repository
2. Open `index.html` in a browser
3. For mobile testing, use browser dev tools or visit on mobile device

## License

Personal portfolio site. All rights reserved.

