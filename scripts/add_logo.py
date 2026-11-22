#!/usr/bin/env python3
"""
CLI tool to easily add or update channel logos in tv-channel-logos.
Supports attaching external links or downloading/storing files locally.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Add scripts directory to path to import update_catalog functions
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

import update_catalog

def parse_args():
    parser = argparse.ArgumentParser(description="Add or update a channel logo in the catalog.")
    parser.add_argument("--id", help="Canonical ID for channel (e.g. 'alltv', 'gma'). Auto-generated if omitted.")
    parser.add_argument("--name", help="Display name of the channel (e.g. 'ALLTV', 'GMA Network').")
    parser.add_argument("--tvg-id", help="XMLTV / EPG tvg-id (e.g. 'AllTV.ph', 'GMA.ph').")
    parser.add_argument("--aliases", nargs="*", default=[], help="Alternative channel names or callsigns.")
    parser.add_argument("--country", default="PH", help="Country code (ISO 2-letter, e.g. 'PH', 'US', 'GB'). Default: PH.")
    parser.add_argument("--category", default="Entertainment", help="Channel genre/category (e.g. 'Entertainment', 'News', 'Sports', 'Movies').")
    parser.add_argument("--url", help="External logo URL to attach (or download from).")
    parser.add_argument("--file", help="Path to local file already in logos/ (e.g. 'logos/gma.png').")
    parser.add_argument("--download", action="store_true", help="Download the image from --url and store locally in logos/.")
    return parser.parse_args()

def interactive_prompt():
    print("\n--- Add New TV Channel Logo ---")
    name = input("Channel Name (e.g. 'GMA 7'): ").strip()
    if not name:
        print("Channel name is required.")
        sys.exit(1)

    cid = update_catalog.sanitize_filename(name)
    cid_input = input(f"Channel ID [{cid}]: ").strip()
    if cid_input:
        cid = cid_input

    tvg_id = input("XMLTV tvg-id (e.g. 'GMA.ph') [optional]: ").strip()
    aliases_raw = input("Aliases (comma-separated, e.g. 'GMA, DZBB TV') [optional]: ").strip()
    aliases = [a.strip() for a in aliases_raw.split(",") if a.strip()]

    country = input("Country code (e.g. 'PH') [PH]: ").strip() or "PH"
    category = input("Category (e.g. 'Entertainment', 'News', 'Sports') [Entertainment]: ").strip() or "Entertainment"

    print("\nHow would you like to provide the logo?")
    print("1. Attach external URL only (don't store file locally)")
    print("2. Download logo from external URL and store in logos/")
    print("3. Reference an already existing local file in logos/")
    choice = input("Choice (1/2/3) [1]: ").strip() or "1"

    url = None
    file_rel = None
    download = False

    if choice == "1":
        url = input("Enter External Logo Image URL: ").strip()
    elif choice == "2":
        url = input("Enter External Logo Image URL to download: ").strip()
        download = True
    elif choice == "3":
        file_input = input("File name inside logos/ (e.g. 'gma.png'): ").strip()
        file_rel = f"logos/{file_input}" if not file_input.startswith("logos/") else file_input

    return {
        "id": cid,
        "name": name,
        "tvg_id": tvg_id,
        "aliases": aliases,
        "country": country,
        "category": category,
        "url": url,
        "file": file_rel,
        "download": download
    }

def main():
    args = parse_args()
    if not args.name:
        data = interactive_prompt()
        cid = data["id"]
        name = data["name"]
        tvg_id = data["tvg_id"]
        aliases = data["aliases"]
        country = data["country"]
        category = data["category"]
        url = data["url"]
        file_rel = data["file"]
        download = data["download"]
    else:
        name = args.name.strip()
        cid = args.id.strip() if args.id else update_catalog.sanitize_filename(name)
        tvg_id = args.tvg_id.strip() if args.tvg_id else ""
        aliases = args.aliases or []
        country = args.country.strip() or "PH"
        category = args.category.strip() or "Entertainment"
        url = args.url.strip() if args.url else None
        file_rel = args.file.strip() if args.file else None
        download = args.download

    channels = update_catalog.load_channels()

    # Check if entry already exists (by id, name, or tvg_id)
    existing_idx = None
    for idx, c in enumerate(channels):
        if c.get("id") == cid or (c.get("name", "").lower() == name.lower()):
            existing_idx = idx
            break

    entry = channels[existing_idx] if existing_idx is not None else {}
    entry["id"] = cid
    entry["name"] = name
    if tvg_id:
        entry["tvg_id"] = tvg_id
    elif "tvg_id" not in entry:
        entry["tvg_id"] = ""

    current_aliases = set(entry.get("aliases", []))
    current_aliases.update(aliases)
    entry["aliases"] = sorted(list(current_aliases))

    entry["country"] = country
    entry["category"] = category

    if file_rel:
        entry["file"] = file_rel
    if url:
        entry["external_url"] = url

    # Handle download request
    if download and url:
        ext = ".png"
        raw_ext = "." + url.split("?")[0].split(".")[-1].lower()
        if raw_ext in [".png", ".svg", ".jpg", ".jpeg", ".webp"]:
            ext = raw_ext
        dest = update_catalog.LOGOS_DIR / f"{cid}{ext}"
        print(f"Downloading {url} to {dest}...")
        if update_catalog.download_file(url, dest):
            entry["file"] = f"logos/{cid}{ext}"
            print("Download successful!")
        else:
            print("Download failed, storing as external_url only.")

    if existing_idx is not None:
        channels[existing_idx] = entry
        print(f"Updated existing channel '{name}' ({cid}).")
    else:
        channels.append(entry)
        print(f"Added new channel '{name}' ({cid}).")

    update_catalog.save_channels(channels)
    print("Regenerating catalog and README...")
    update_catalog.main()

if __name__ == "__main__":
    main()
