# Abhishek Singh — Personal Portfolio & Writing

A hyper-minimalist, blisteringly fast personal portfolio and essay platform built with **Astro**, **Tailwind CSS v4**, and native Markdown content collections.

- **Total Bundle Size:** ~90 KB (Zero runtime client-side JavaScript by default)
- **Design Philosophy:** Minimalist, typography-first, fast load times, dark/light mode toggle with zero layout flash.
- **Hosting Target:** GitHub Pages (`https://abhisheksingh0196.github.io`).

---

## Features

- **Selected Work:** Interactive highlights of leadership roles at Oleria, Kloudfuse, Komma (Acquired), Dashh, PharmEasy, and ZS Associates with outbound links.
- **Side Projects & Craft:** Featured showcase for **Gatsby** (minimal macOS e-book manager in Rust & Tauri) with direct DMG download links.
- **Writing Platform:** Native Markdown content collection in `src/content/writing/`.
- **Automated GitHub Pages CI/CD:** Ready-to-go GitHub Actions workflow in `.github/workflows/deploy.yml`.

---

## How to Add New Writing / Essays

To publish a new essay or note, simply drop a new `.md` file inside `src/content/writing/`:

```markdown
---
title: "Your Essay Title"
description: "A 1-2 sentence description for preview cards and SEO."
pubDate: 2026-10-18
tags: ["Product", "AI", "Identity"]
---

Write your markdown content here. Supports headings, lists, blockquotes, code blocks, and markdown links!
```

---

## Local Development

```bash
# Start local dev server
npm run dev

# Build production static bundle
npm run build

# Preview production build locally
npm run preview
```

---

## Deploying to GitHub Pages

1. Create a repository on GitHub named:
   `abhisheksingh0196.github.io`
2. Connect this local repository and push:
   ```bash
   git remote add origin https://github.com/abhisheksingh0196/abhisheksingh0196.github.io.git
   git push -u origin main
   ```
3. In your GitHub repository settings:
   - Go to **Settings** -> **Pages**.
   - Under **Build and deployment**, select **Source: GitHub Actions**.
4. The workflow will automatically build and deploy your site to `https://abhisheksingh0196.github.io`!
