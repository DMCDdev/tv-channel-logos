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
import urllib.parse
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

def format_title_name(raw_name: str) -> str:
    """Format file basename to clean channel title."""
    cleaned = raw_name.replace("-", " ").replace("_", " ").strip()
    words = cleaned.split()
    caps = ["tv", "hd", "sd", "ph", "us", "uk", "cnn", "gma", "gtv", "ibc", "ptv", "rptv", "a2z", "anc", "axn", "pbo", "pba", "sm", "smni", "untv", "ewtn", "tlc", "cltv", "dzmm", "dzrh", "inc", "myx", "tmc", "tap", "net"]
    result = []
    for w in words:
        if w.lower() in caps:
            result.append(w.upper())
        else:
            result.append(w.capitalize())
    return " ".join(result)

def load_channels():
    if not CHANNELS_FILE.exists():
        return []
    with open(CHANNELS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_channels(channels):
    with open(CHANNELS_FILE, "w", encoding="utf-8") as f:
        json.dump(channels, f, indent=2, ensure_ascii=False)
        f.write("\n")

def auto_discover_logos(existing_channels):
    """Auto-discover logo files in logos/ that aren't yet in channels.json."""
    if not LOGOS_DIR.exists():
        return existing_channels, False

    known_files = set()
    for c in existing_channels:
        f = c.get("file")
        if f:
            known_files.add(f.lower())
            known_files.add(f.replace("-", " ").lower())
            known_files.add(f.replace(" ", "-").lower())
            known_files.add(Path(f).name.lower())

    added = False
    valid_exts = {".png", ".jpg", ".jpeg", ".svg", ".webp"}

    for p in sorted(LOGOS_DIR.iterdir()):
        if p.is_file() and p.suffix.lower() in valid_exts and p.name != ".gitkeep":
            rel_file = f"logos/{p.name}"
            if p.name.lower() not in known_files and rel_file.lower() not in known_files:
                base_stem = p.stem
                cid = sanitize_filename(base_stem)
                title = format_title_name(base_stem)
                
                # Assign country based on common patterns
                country = "PH"
                if any(x in base_stem.lower() for x in ["cnn", "discovery", "fox", "al-jazeera", "animax", "axn", "cartoon network", "history", "tlc"]):
                    if "ph" not in base_stem.lower():
                        country = "US" if "al-jazeera" not in base_stem.lower() else "QA"

                # Assign category
                cat = "Entertainment"
                if any(x in base_stem.lower() for x in ["news", "cnn", "al-jazeera", "dzmm", "dzrh", "one news", "anc"]):
                    cat = "News"
                elif any(x in base_stem.lower() for x in ["sports", "pba"]):
                    cat = "Sports"
                elif any(x in base_stem.lower() for x in ["movie", "cinema", "cinemo", "pbo", "actionflix"]):
                    cat = "Movies"
                elif any(x in base_stem.lower() for x in ["discovery", "history", "tlc"]):
                    cat = "Documentary"
                elif any(x in base_stem.lower() for x in ["cartoon", "animax"]):
                    cat = "Animation"
                elif any(x in base_stem.lower() for x in ["ewtn", "inc"]):
                    cat = "Religious"

                new_entry = {
                    "id": cid,
                    "name": title,
                    "aliases": [title, base_stem],
                    "tvg_id": f"{cid.replace('-', '')}.{country.lower()}",
                    "country": country,
                    "category": cat,
                    "file": rel_file,
                    "external_url": None
                }
                existing_channels.append(new_entry)
                known_files.add(p.name.lower())
                added = True
                print(f"Auto-discovered new logo: '{p.name}' -> Added as '{title}'")

    return existing_channels, added

def main():
    download_missing = "--download" in sys.argv
    print(f"Loading {CHANNELS_FILE}...")
    channels = load_channels()
    print(f"Found {len(channels)} existing channel definitions.")

    LOGOS_DIR.mkdir(parents=True, exist_ok=True)

    # Auto-discover any unmapped logos in logos/ folder
    channels, auto_added = auto_discover_logos(channels)

    lookup_map = {}
    table_rows = []

    stored_count = 0
    external_count = 0
    updated_channels = auto_added

    for item in sorted(channels, key=lambda x: (x.get("country", ""), x.get("name", "").lower())):
        cid = item.get("id", "").strip()
        name = item.get("name", "").strip()
        tvg_id = item.get("tvg_id", "").strip()
        country = item.get("country", "").strip()
        category = item.get("category", "").strip()
        aliases = item.get("aliases", [])
        file_rel = item.get("file", "").strip() if item.get("file") else None
        ext_url = item.get("external_url", "").strip() if item.get("external_url") else None

        # Check local file with fallback to spaces / hyphens / URL unquote
        local_exists = False
        resolved_file = None
        if file_rel:
            candidates = [
                file_rel,
                urllib.parse.unquote(file_rel),
                file_rel.replace("-", " "),
                file_rel.replace(" ", "-"),
                Path(file_rel).name,
                Path(file_rel).name.replace("-", " "),
                Path(file_rel).name.replace(" ", "-"),
            ]
            for cand in candidates:
                cand_path = ROOT_DIR / cand if cand.startswith("logos") else LOGOS_DIR / cand
                if cand_path.is_file():
                    resolved_file = f"logos/{cand_path.name}"
                    local_exists = True
                    if file_rel != resolved_file:
                        item["file"] = resolved_file
                        updated_channels = True
                    break

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
                resolved_file = f"logos/{target_name}"
                item["file"] = resolved_file
                local_exists = True
                updated_channels = True

        # Determine primary resolved URL
        primary_url = ""
        storage_type = "None"
        preview_src = ""
        if local_exists and resolved_file:
            # Encode spaces and special chars for valid Web URL
            encoded_path = urllib.parse.quote(resolved_file)
            primary_url = f"{CDN_BASE}{encoded_path}"
            raw_url = f"{RAW_BASE}{encoded_path}"
            storage_type = "Stored (Repo)"
            stored_count += 1
            # Use repository relative path for GitHub README so newly pushed images render immediately without CDN caching delay
            preview_src = encoded_path
        elif ext_url:
            primary_url = ext_url
            raw_url = ext_url
            storage_type = "Attached Link"
            external_count += 1
            preview_src = ext_url
        else:
            primary_url = ""
            raw_url = ""
            storage_type = "Missing"
            preview_src = ""

        # Populate quick lookup map
        if primary_url:
            keys_to_map = [cid, name, tvg_id] + list(aliases)
            if resolved_file:
                file_stem = Path(resolved_file).stem
                keys_to_map.extend([file_stem, file_stem.replace("-", " "), file_stem.replace(" ", "-")])

            for k in set(keys_to_map):
                if not k:
                    continue
                k_str = str(k).strip()
                if not k_str:
                    continue
                lookup_map[k_str] = primary_url
                lookup_map[k_str.lower()] = primary_url
                lookup_map[k_str.upper()] = primary_url
                lookup_map[k_str.replace(" ", "")] = primary_url
                lookup_map[k_str.replace(" ", "-")] = primary_url
                lookup_map[k_str.replace(" ", "_")] = primary_url

        # Build table row
        preview_img = f'<img src="{preview_src}" alt="{name}" height="32" style="max-height:32px; vertical-align:middle;"/>' if preview_src else "—"
        tvg_display = f"<code>{tvg_id}</code>" if tvg_id else "—"
        type_badge = f"`{storage_type}`"
        link_display = f"[Direct Link]({primary_url})" if primary_url else "—"

        table_rows.append(
            f"| {preview_img} | **{name}** | {tvg_display} | {category or 'General'} | {country or 'Global'} | {type_badge} | {link_display} |"
        )

    if updated_channels:
        print("Updating channels.json with resolved paths and auto-discovered logos...")
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
3. Automatically discover and map any images placed in `logos/`.

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

### Option A: Drag & Drop directly on GitHub (Easiest)
1. Go to the `logos/` folder on GitHub and click **Add file** > **Upload files**.
2. Drag and drop your logo `.png` or `.svg`.
3. The automated GitHub Action will automatically register it and update this README gallery!

### Option B: Add Manually to `channels.json`

Add an entry to `channels.json`:

```json
{{
  "id": "alltv-2",
  "name": "ALLTV2",
  "aliases": ["ABS-CBN sa ALLTV2", "ALLTV2"],
  "tvg_id": "ALLTV2.ph",
  "country": "PH",
  "category": "Entertainment",
  "file": "logos/abs-cbn sa alltv2.png",
  "external_url": null
}}
```

- If you want to **store the file locally**: place the image into `logos/` and set `"file": "logos/<filename>.png"`.
- If you only want to **attach an external link**: set `"file": null` and provide `"external_url"`.

---

## Channel Directory & Gallery

| Logo | Channel Name | tvg-id | Category | Country | Storage Type | Direct Link |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
{table_content}

---

## Automation

This repository includes a GitHub Actions workflow (`.github/workflows/update-catalog.yml`). Whenever you commit changes to `channels.json` or add files to `logos/`, the workflow automatically:
1. Auto-discovers and validates all channels.
2. Generates updated `logos.json`.
3. Rebuilds the visual Markdown table in `README.md`.
4. Commits and pushes the updates back to `main`.
"""

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_text)

    print(f"Catalog updated successfully! Stored: {stored_count}, External: {external_count}")

    if "--purge" in sys.argv:
        purge_jsdelivr_cache([c.get("file") for c in channels if c.get("file")])

def purge_jsdelivr_cache(file_paths):
    """Purge jsDelivr cache for given relative file paths so updates appear immediately."""
    clean_paths = [p for p in file_paths if p]
    print(f"Purging jsDelivr CDN cache for {len(clean_paths)} files...")
    for fpath in clean_paths:
        encoded = urllib.parse.quote(fpath.replace("\\", "/"))
        url = f"https://purge.jsdelivr.net/gh/{REPO_OWNER}/{REPO_NAME}@{BRANCH}/{encoded}"
        req = urllib.request.Request(url, headers={"User-Agent": "TVChannelLogosBot/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                pass
        except Exception:
            pass
        time.sleep(0.05)
    print("jsDelivr CDN cache purged successfully.")

if __name__ == "__main__":
    main()
