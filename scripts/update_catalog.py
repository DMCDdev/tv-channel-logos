#!/usr/bin/env python3
"""
tv-channel-logos Catalog Generator & Manager
Maintains channels.json, generates logos.json, and builds the visual README gallery.
"""

import json
import os
import re
import ssl
import sys
import time
import urllib.request
from pathlib import Path

REPO_OWNER = "DMCDdev"
REPO_NAME = "tv-channel-logos"
BRANCH = "main"

RAW_BASE = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/"
CDN_BASE = f"https://cdn.jsdelivr.net/gh/{REPO_OWNER}/{REPO_NAME}@{BRANCH}/"

ROOT_DIR = Path(__file__).resolve().parent.parent
LOGOS_DIR = ROOT_DIR / "logos"
CHANNELS_FILE = ROOT_DIR / "channels.json"
LOGOS_JSON_FILE = ROOT_DIR / "logos.json"
README_FILE = ROOT_DIR / "README.md"

def download_file(url: str, dest_path: Path) -> bool:
    """Download an image from url to dest_path with compliant user-agent and retry."""
    headers = {
        "User-Agent": "TVChannelLogosBot/1.0 (https://github.com/DMCDdev/tv-channel-logos; daryl@DMCD-PT300)",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
    }
    ctx = ssl._create_unverified_context()
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                if resp.status in (200, 206):
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    dest_path.write_bytes(resp.read())
                    time.sleep(1.2)  # Respect rate limits
                    return True
        except Exception as e:
            if attempt == 0:
                time.sleep(2.5)
            else:
                print(f"  [ERROR] Failed to download {url}: {e}")
    return False

def sanitize_filename(name: str) -> str:
    """Sanitize string for clean file name."""
    s = re.sub(r"[^a-zA-Z0-9_-]", "-", name.lower())
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "logo"

def load_channels():
    if not CHANNELS_FILE.exists():
        return []
    with open(CHANNELS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_channels(channels):
    with open(CHANNELS_FILE, "w", encoding="utf-8") as f:
        json.dump(channels, f, indent=2, ensure_ascii=False)
        f.write("\n")

def main():
    download_missing = "--download" in sys.argv
    print(f"Loading {CHANNELS_FILE}...")
    channels = load_channels()
    print(f"Found {len(channels)} channel definitions.")

    LOGOS_DIR.mkdir(parents=True, exist_ok=True)

    lookup_map = {}
    table_rows = []

    stored_count = 0
    external_count = 0
    updated_channels = False

    for item in sorted(channels, key=lambda x: (x.get("country", ""), x.get("name", "").lower())):
        cid = item.get("id", "").strip()
        name = item.get("name", "").strip()
        tvg_id = item.get("tvg_id", "").strip()
        country = item.get("country", "").strip()
        category = item.get("category", "").strip()
        aliases = item.get("aliases", [])
        file_rel = item.get("file", "").strip() if item.get("file") else None
        ext_url = item.get("external_url", "").strip() if item.get("external_url") else None

        # Check local file
        local_exists = False
        if file_rel:
            local_path = ROOT_DIR / file_rel
            local_exists = local_path.is_file()

        # If --download is passed and local file is missing, try to download external_url
        if download_missing and not local_exists and ext_url:
            ext = ".png"
            if "." in ext_url.split("?")[0]:
                raw_ext = "." + ext_url.split("?")[0].split(".")[-1].lower()
                if raw_ext in [".png", ".svg", ".jpg", ".jpeg", ".webp"]:
                    ext = raw_ext
            target_name = f"{cid or sanitize_filename(name)}{ext}"
            target_path = LOGOS_DIR / target_name
            print(f"Downloading logo for '{name}' -> {target_name}...")
            if download_file(ext_url, target_path):
                file_rel = f"logos/{target_name}"
                item["file"] = file_rel
                local_exists = True
                updated_channels = True

        # Determine primary resolved URL
        primary_url = ""
        storage_type = "None"
        if local_exists and file_rel:
            primary_url = f"{CDN_BASE}{file_rel}"
            raw_url = f"{RAW_BASE}{file_rel}"
            storage_type = "Stored (Repo)"
            stored_count += 1
        elif ext_url:
            primary_url = ext_url
            raw_url = ext_url
            storage_type = "Attached Link"
            external_count += 1
        else:
            primary_url = ""
            raw_url = ""
            storage_type = "Missing"

        # Populate quick lookup map
        if primary_url:
            # Map by ID
            if cid:
                lookup_map[cid] = primary_url
                lookup_map[cid.lower()] = primary_url
                lookup_map[cid.upper()] = primary_url
            # Map by name and common variants
            if name:
                lookup_map[name] = primary_url
                lookup_map[name.lower()] = primary_url
                lookup_map[name.upper()] = primary_url
                lookup_map[name.replace(" ", "")] = primary_url
                lookup_map[name.replace(" ", "-")] = primary_url
                lookup_map[name.replace(" ", "_")] = primary_url
            # Map by tvg_id
            if tvg_id:
                lookup_map[tvg_id] = primary_url
                lookup_map[tvg_id.lower()] = primary_url
            # Map by aliases
            for alias in aliases:
                a_str = str(alias).strip()
                if a_str:
                    lookup_map[a_str] = primary_url
                    lookup_map[a_str.lower()] = primary_url
                    lookup_map[a_str.replace(" ", "")] = primary_url

        # Build table row
        # Preview image
        preview_img = f'<img src="{primary_url}" alt="{name}" height="32" style="max-height:32px; vertical-align:middle;"/>' if primary_url else "—"
        tvg_display = f"<code>{tvg_id}</code>" if tvg_id else "—"
        type_badge = f"`{storage_type}`"
        link_display = f"[Direct Link]({primary_url})" if primary_url else "—"

        table_rows.append(
            f"| {preview_img} | **{name}** | {tvg_display} | {category or 'General'} | {country or 'Global'} | {type_badge} | {link_display} |"
        )

    if updated_channels:
        print("Updating channels.json with downloaded local files...")
        save_channels(channels)

    # Save logos.json
    print(f"Writing {LOGOS_JSON_FILE} with {len(lookup_map)} lookup keys...")
    with open(LOGOS_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(lookup_map, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # Generate README.md
    print(f"Generating {README_FILE}...")
    table_content = "\n".join(table_rows) if table_rows else "| — | No channels in catalog yet | — | — | — | — | — |"

    readme_text = f"""# TV Channel Logos

[![Total Channels](https://img.shields.io/badge/Channels-{len(channels)}-blue.svg)](#)
[![Stored Logos](https://img.shields.io/badge/Stored_Files-{stored_count}-green.svg)](#)
[![Attached Links](https://img.shields.io/badge/Attached_Links-{external_count}-orange.svg)](#)
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
https://cdn.jsdelivr.net/gh/{REPO_OWNER}/{REPO_NAME}@{BRANCH}/logos/<channel_filename>.png
```

### 2. GitHub Raw Storage
```text
{RAW_BASE}logos/<channel_filename>.png
```

### 3. Master Lookup JSON API
A flat key-value dictionary mapping any channel name, alias, or `tvg-id` directly to its logo URL:
```text
{RAW_BASE}logos.json
```

### 4. Integration with DreamTuner TV Pro
In DreamTuner TV's **Batch Metadata Tools**, use either:
- **Base Directory**: `{RAW_BASE}`
- **Pattern Mode**: `{RAW_BASE}logos/{{name}}.png`

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
{{
  "id": "alltv",
  "name": "ALLTV",
  "aliases": ["ALL TV", "AllTV.ph", "All TV HD"],
  "tvg_id": "AllTV.ph",
  "country": "PH",
  "category": "Entertainment",
  "file": "logos/alltv.png",
  "external_url": "https://i.imgur.com/vuzKeNN.png"
}}
```

- If you want to **store the file locally**: place the image into `logos/` and set `"file": "logos/<filename>.png"`.
- If you only want to **attach an external link**: set `"file": null` and provide `"external_url"`.
- Run `py scripts/update_catalog.py` to regenerate `logos.json` and update this README table.
- Run `py scripts/update_catalog.py --download` if you want to automatically download all attached external links to local files.

---

## Channel Directory & Gallery

| Logo | Channel Name | tvg-id | Category | Country | Storage Type | Direct Link |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
{table_content}

---

## Automation

This repository includes a GitHub Actions workflow (`.github/workflows/update-catalog.yml`). Whenever you commit changes to `channels.json` or add files to `logos/`, the workflow automatically:
1. Validates all channels.
2. Generates updated `logos.json`.
3. Rebuilds the visual Markdown table in `README.md`.
4. Commits and pushes the updates back to `main`.
"""

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_text)

    print(f"Catalog updated successfully! Stored: {stored_count}, External: {external_count}")

if __name__ == "__main__":
    main()
