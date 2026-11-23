# TV Channel Logos

[![Total Channels](https://img.shields.io/badge/Channels-45-blue.svg)](#)
[![Stored Logos](https://img.shields.io/badge/Stored_Files-0-green.svg)](#)
[![Attached Links](https://img.shields.io/badge/Attached_Links-0-orange.svg)](#)
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

### Option A: Drag & Drop directly on GitHub (Easiest)
1. Go to the `logos/` folder on GitHub and click **Add file** > **Upload files**.
2. Drag and drop your logo `.png` or `.svg`.
3. The automated GitHub Action will automatically register it and update this README gallery!

### Option B: Add Manually to `channels.json`

Add an entry to `channels.json`:

```json
{
  "id": "alltv-2",
  "name": "ALLTV2",
  "aliases": ["ABS-CBN sa ALLTV2", "ALLTV2"],
  "tvg_id": "ALLTV2.ph",
  "country": "PH",
  "category": "Entertainment",
  "file": "logos/abs-cbn sa alltv2.png",
  "external_url": null
}
```

- If you want to **store the file locally**: place the image into `logos/` and set `"file": "logos/<filename>.png"`.
- If you only want to **attach an external link**: set `"file": null` and provide `"external_url"`.

---

## Channel Directory & Gallery

| Logo | Channel Name | tvg-id | Category | Country | Storage Type | Direct Link |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| — | **Animax** | <code>Animax.asia</code> | Animation | Asia | `Missing` | — |
| — | **AXN** | <code>AXN.asia</code> | Entertainment | Asia | `Missing` | — |
| — | **Cartoon Network** | <code>CartoonNetwork.asia</code> | Animation | Asia | `Missing` | — |
| — | **CNN** | <code>CNN.asia</code> | News | Asia | `Missing` | — |
| — | **Discovery Channel** | <code>DiscoveryChannel.asia</code> | Documentary | Asia | `Missing` | — |
| — | **History** | <code>History.asia</code> | Documentary | Asia | `Missing` | — |
| — | **TLC** | <code>TLC.asia</code> | Documentary | Asia | `Missing` | — |
| — | **Al Jazeera** | <code>AlJazeeraEnglish.net</code> | News | Global | `Missing` | — |
| — | **A2Z** | <code>A2Z.ph</code> | Entertainment | PH | `Missing` | — |
| — | **Aliw 23 Channel** | <code>aliw23channel.ph</code> | Entertainment | PH | `Missing` | — |
| — | **ALLTV2** | <code>ALLTV2.ph</code> | Entertainment | PH | `Missing` | — |
| — | **ANC** | <code>anc.ph</code> | News | PH | `Missing` | — |
| — | **Cinema One** | <code>cinemaone.ph</code> | Movies | PH | `Missing` | — |
| — | **Cinemo** | <code>cinemo.ph</code> | Movies | PH | `Missing` | — |
| — | **CLTV 36** | <code>cltv36.ph</code> | Entertainment | PH | `Missing` | — |
| — | **DZMM Teleradyo** | <code>dzmmteleradyo.ph</code> | News | PH | `Missing` | — |
| — | **DZRH TV** | <code>dzrhtv.ph</code> | News | PH | `Missing` | — |
| — | **EWTN** | <code>ewtn.ph</code> | Religious | PH | `Missing` | — |
| — | **GMA** | <code>gma.ph</code> | Entertainment | PH | `Missing` | — |
| — | **GTV** | <code>gtv.ph</code> | Entertainment | PH | `Missing` | — |
| — | **IBC 13** | <code>ibc13.ph</code> | Entertainment | PH | `Missing` | — |
| — | **INC Radio** | <code>incradio.ph</code> | Religious | PH | `Missing` | — |
| — | **INC TV** | <code>inctv.ph</code> | Religious | PH | `Missing` | — |
| — | **Kapamilya Channel** | <code>abscbnkapamilyachannel.ph</code> | Entertainment | PH | `Missing` | — |
| — | **Kapamilya Channel HD** | <code>KapamilyaChannelHD.ph</code> | Entertainment | PH | `Missing` | — |
| — | **Metro Channel** | <code>metrochannel.ph</code> | Entertainment | PH | `Missing` | — |
| — | **Moviesphere** | <code>moviesphere.ph</code> | Movies | PH | `Missing` | — |
| — | **MYX** | <code>myx.ph</code> | Entertainment | PH | `Missing` | — |
| — | **Net25** | <code>net25.ph</code> | Entertainment | PH | `Missing` | — |
| — | **One News PH** | <code>onenewsph.ph</code> | News | PH | `Missing` | — |
| — | **One PH** | <code>oneph.ph</code> | Entertainment | PH | `Missing` | — |
| — | **One Sports** | <code>onesports.ph</code> | Sports | PH | `Missing` | — |
| — | **PBA Rush** | <code>pbarush.ph</code> | Sports | PH | `Missing` | — |
| — | **PBO** | <code>pbo.ph</code> | Movies | PH | `Missing` | — |
| — | **PTV 4** | <code>ptv4.ph</code> | Entertainment | PH | `Missing` | — |
| — | **RPTV** | <code>rptv.ph</code> | Entertainment | PH | `Missing` | — |
| — | **SMNI** | <code>smni.ph</code> | Entertainment | PH | `Missing` | — |
| — | **Tap Actionflix** | <code>tapactionflix.ph</code> | Movies | PH | `Missing` | — |
| — | **Tap Movies** | <code>tapmovies.ph</code> | Movies | PH | `Missing` | — |
| — | **Tap Sports** | <code>tapsports.ph</code> | Sports | PH | `Missing` | — |
| — | **Tap TV** | <code>taptv.ph</code> | Entertainment | PH | `Missing` | — |
| — | **Tv5** | <code>tv5.ph</code> | Entertainment | PH | `Missing` | — |
| — | **UNTV** | <code>untv.ph</code> | Entertainment | PH | `Missing` | — |
| — | **Vivacinema** | <code>vivacinema.ph</code> | Movies | PH | `Missing` | — |
| — | **Fox News Channel** | <code>foxnewschannel.us</code> | News | US | `Missing` | — |

---

## Automation

This repository includes a GitHub Actions workflow (`.github/workflows/update-catalog.yml`). Whenever you commit changes to `channels.json` or add files to `logos/`, the workflow automatically:
1. Auto-discovers and validates all channels.
2. Generates updated `logos.json`.
3. Rebuilds the visual Markdown table in `README.md`.
4. Commits and pushes the updates back to `main`.
