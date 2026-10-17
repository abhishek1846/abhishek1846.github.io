---
title: "Building Gatsby: Why I Wrote an E-Book Manager in Rust and Tauri"
description: "Why traditional e-book managers like Calibre are bloated, and how building a ~40MB RAM native desktop app solved Kindle bug bypasses."
pubDate: 2026-10-15
tags: ["Rust", "Tauri", "Product Design", "Kindle", "Side Projects"]
---

For years, anyone reading e-books on a Kindle outside the Amazon walled garden has had to rely on **Calibre**. Calibre is an undeniably impressive piece of software that has sustained the e-book community for nearly two decades. But it also looks and feels like it was designed in 2006. It consumes hundreds of megabytes of memory, feels sluggish, and buries simple tasks under dozens of configuration menus.

I wanted something different: a **hyper-minimalist, blisteringly fast e-book manager** built specifically for macOS. Something with a clean Linear-style interface that takes less than 15MB of disk space, uses ~40MB of RAM, and treats reading with the aesthetic simplicity it deserves.

That was the genesis of **[Gatsby](https://github.com/abhisheksingh0196/gatsby-releases)**.

## The Architecture: Rust + Tauri + React

Instead of shipping a heavy Electron binary with an entire Chromium and Node.js runtime bundled into every release, I chose **Tauri v2** with **Rust** under the hood:

- **Frontend:** React, TypeScript, Vite, Tailwind CSS. Clean, responsive, and adheres to native macOS dark/light mode standards.
- **Backend/Engine:** Rust. Using crates like `boko` and `epub` to parse metadata and cover art in milliseconds.
- **Strict Sandboxing:** E-books in the wild (especially from various public archives) often contain poorly structured HTML or embedded scripts. By implementing a strict Content Security Policy (CSP) and scoped asset protocol (`asset.localhost`), the app is cryptographically restricted from reading files outside its dedicated cache.

## Bypassing the Kindle's Amazon-Enforced Flaws

When you transfer non-Amazon `.azw3` books to a modern Kindle via USB, you run into frustrating Amazon bugs:

1. **The Disappearing Cover Thumbnail Bug:** Amazon's Kindle OS often refuses to display cover thumbnails for side-loaded books because it expects covers to be fetched directly from Amazon servers with an ASIN (Amazon Standard Identification Number). If you connect to Wi-Fi, it will even actively overwrite your covers.
2. **Missing Page Numbers:** Sideloaded MOBI/AZW3 files natively lack page numbers, showing only generic "Locations".

To solve this in Gatsby, I built two low-level bypasses in Rust:
- **Binary Header Patching & Thumbnail Injection:** Gatsby generates a deterministic ASIN identifier, patches the raw AZW3 binary header on the fly, and forcefully injects high-resolution thumbnails directly into the Kindle's hidden `/system/thumbnails/` directory.
- **Native APNX Sidecar Generator:** A lightweight generator that calculates byte-offsets and creates a matching `.apnx` file inside the `.sdr` directory, giving you authentic page numbers on your Kindle.

Building Gatsby reinforced my core philosophy on product craft: **software should be lean, fast, respectful of the user's system, and solve hard edge cases seamlessly behind an invisible UI.**
