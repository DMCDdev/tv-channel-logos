# TV Channel Logos

[![Total Channels](https://img.shields.io/badge/Channels-2-blue.svg)](#)
[![Stored Logos](https://img.shields.io/badge/Stored_Files-0-green.svg)](#)
[![Attached Links](https://img.shields.io/badge/Attached_Links-1-orange.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A unified repository for TV channel logos designed for **[DreamTuner TV](https://github.com/DMCDdev/DreamTunerTV)**, IPTV players, M3U playlists, and XMLTV EPG guides.

This repository allows you to either:
1. **Store logo files** directly in the `logos/` directory (served via GitHub Raw and fast jsDelivr CDN).
2. **Attach external links** (e.g. Wikimedia, Imgur, or official network links) in `channels.json` without storing local files.
3. Automatically download any attached link into local storage whenever desired.

---

## Direct URLs & Endpoints

### 1. Fast Global CDN (Recommended for Apps)
```text
https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/<channel_filename>.png
```

### 2. GitHub Raw Storage
```text
https://raw.githubusercontent.com/DMCDdev/tv-channel-logos/main/logos/<channel_filename>.png
```

### 3. Master Lookup JSON API
A flat key-value dictionary mapping any channel name, alias, or `tvg-id` directly to its logo URL:
```text
https://raw.githubusercontent.com/DMCDdev/tv-channel-logos/main/logos.json
```

### 4. Integration with DreamTuner TV Pro
In DreamTuner TV's **Batch Metadata Tools**, use either:
- **Base Directory**: `https://raw.githubusercontent.com/DMCDdev/tv-channel-logos/main/`
- **Pattern Mode**: `https://raw.githubusercontent.com/DMCDdev/tv-channel-logos/main/logos/{name}.png`

DreamTuner TV will automatically match channel names, callsigns, and sanitized aliases against this catalog.

---

## How to Add Logos

### Option A: Use the CLI Helper (Fastest)

Run the included helper script:

```bash
# Add a channel and attach an external link
py scripts/add_logo.py --name "GMA 7" --tvg-id "GMA.ph" --country "PH" --category "Entertainment" --url "https://i.imgur.com/example.png"

# Add a channel, download the logo, and store it locally in logos/
py scripts/add_logo.py --name "TV5" --tvg-id "TV5.ph" --country "PH" --url "https://i.imgur.com/example.png" --download
```

### Option B: Add Manually to `channels.json`

Add an entry to `channels.json`:

```json
{
  "id": "alltv",
  "name": "ALLTV",
  "aliases": ["ALL TV", "AllTV.ph", "All TV HD"],
  "tvg_id": "AllTV.ph",
  "country": "PH",
  "category": "Entertainment",
  "file": "logos/alltv.png",
  "external_url": "https://i.imgur.com/vuzKeNN.png"
}
```

- If you want to **store the file locally**: place the image into `logos/` and set `"file": "logos/<filename>.png"`.
- If you only want to **attach an external link**: set `"file": null` and provide `"external_url"`.
- Run `py scripts/update_catalog.py` to regenerate `logos.json` and update this README table.
- Run `py scripts/update_catalog.py --download` if you want to automatically download all attached external links to local files.

---

## Channel Directory & Gallery

| Logo | Channel Name | tvg-id | Category | Country | Storage Type | Direct Link |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| — | **Sample Channel One** | <code>Sample1.tv</code> | General | US | `Missing` | — |
| <img src="https://example.com/logos/sample-news.png" alt="Sample News Network" height="32" style="max-height:32px; vertical-align:middle;"/> | **Sample News Network** | <code>SampleNews.tv</code> | News | US | `Attached Link` | [Direct Link](https://example.com/logos/sample-news.png) |

---

## Automation

This repository includes a GitHub Actions workflow (`.github/workflows/update-catalog.yml`). Whenever you commit changes to `channels.json` or add files to `logos/`, the workflow automatically:
1. Validates all channels.
2. Generates updated `logos.json`.
3. Rebuilds the visual Markdown table in `README.md`.
4. Commits and pushes the updates back to `main`.
