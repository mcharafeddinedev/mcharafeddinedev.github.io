# Project Structure

This document outlines the organized structure of the portfolio website.

## 📁 Directory Structure

```
mcharafeddinedev.github.io/
│
├── _config.yml              # Jekyll configuration
├── 404.html                 # Custom 404 error page
├── robots.txt               # Search engine directives
├── .gitignore               # Git ignore rules
├── README.md                # Project documentation
│
├── index.md                 # Homepage (nav_order: 1)
├── work-history.md          # Work History (nav_order: 2)
├── projects.md              # Projects (nav_order: 3)
├── mylib.md                 # My Library (nav_order: 4)
├── activedev.md             # Current Pursuits (nav_exclude: true)
├── blog.md                  # Blog (nav_exclude: true)
│
├── _includes/               # Jekyll includes
│   └── head_custom.html     # Custom head elements (SEO, security)
│
├── _sass/                   # SCSS source files
│   └── custom/
│       ├── setup.scss       # SCSS variables
│       └── custom.scss      # Custom styles
│
├── assets/                  # Static assets
│   └── images/              # All project images and logo
│       ├── revisedLogoForGitHubPages.png
│       └── [9 project images]
│
└── _archive/                # Archived/unused files
    └── custom.css.old       # Old CSS file (replaced by SCSS)
```

## 📄 File Organization

### Root Level Files
- **Configuration**: `_config.yml`, `.gitignore`
- **Essential Pages**: All `.md` files (Jekyll requires pages in root)
- **System Files**: `404.html`, `robots.txt`
- **Documentation**: `README.md`, `STRUCTURE.md`

### Theme Files (Jekyll Standard)
- **`_includes/`**: Template includes (auto-loaded by theme)
- **`_sass/`**: SCSS source files (compiled by Jekyll)
- **`assets/`**: Static assets served directly

### Archived Files
- **`_archive/`**: Old/unused files (excluded from Jekyll processing)

## 🔗 Path References

### Internal Links
- Pages: Use relative paths (`projects.md`, `index.md`)
- Images: Use absolute paths (`/assets/images/logo.png`)
- Assets: Use absolute paths from root

### External Links
- All external links use full HTTPS URLs

## ✅ Organization Principles

1. **Pages in Root**: Required by Jekyll/Just the Docs for proper navigation
2. **Assets Organized**: Images in `assets/images/`, styles in `_sass/`
3. **Clean Root**: Only essential files in root directory
4. **Archive Old Files**: Unused files moved to `_archive/`
5. **Standard Jekyll Structure**: Follows Jekyll conventions

## 📝 Notes

- All markdown pages must remain in root for Just the Docs navigation
- SCSS files in `_sass/custom/` are automatically processed
- Old CSS file archived but kept for reference
- Empty `docs/` folder removed for cleanliness
