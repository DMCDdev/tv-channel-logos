# TV Channel Logos

[![Total Channels](https://img.shields.io/badge/Channels-45-blue.svg)](#)
[![Stored Logos](https://img.shields.io/badge/Stored_Files-45-green.svg)](#)
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
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/animax.png" alt="Animax" height="32" style="max-height:32px; vertical-align:middle;"/> | **Animax** | <code>Animax.asia</code> | Animation | Asia | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/animax.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/axn.png" alt="AXN" height="32" style="max-height:32px; vertical-align:middle;"/> | **AXN** | <code>AXN.asia</code> | Entertainment | Asia | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/axn.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cartoon%20network.png" alt="Cartoon Network" height="32" style="max-height:32px; vertical-align:middle;"/> | **Cartoon Network** | <code>CartoonNetwork.asia</code> | Animation | Asia | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cartoon%20network.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cnn.png" alt="CNN" height="32" style="max-height:32px; vertical-align:middle;"/> | **CNN** | <code>CNN.asia</code> | News | Asia | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cnn.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/discovery%20channel.png" alt="Discovery Channel" height="32" style="max-height:32px; vertical-align:middle;"/> | **Discovery Channel** | <code>DiscoveryChannel.asia</code> | Documentary | Asia | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/discovery%20channel.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/history.png" alt="History" height="32" style="max-height:32px; vertical-align:middle;"/> | **History** | <code>History.asia</code> | Documentary | Asia | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/history.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tlc.png" alt="TLC" height="32" style="max-height:32px; vertical-align:middle;"/> | **TLC** | <code>TLC.asia</code> | Documentary | Asia | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tlc.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/al-jazeera.png" alt="Al Jazeera" height="32" style="max-height:32px; vertical-align:middle;"/> | **Al Jazeera** | <code>AlJazeeraEnglish.net</code> | News | Global | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/al-jazeera.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/a2z.png" alt="A2Z" height="32" style="max-height:32px; vertical-align:middle;"/> | **A2Z** | <code>A2Z.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/a2z.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/aliw%2023%20channel.png" alt="Aliw 23 Channel" height="32" style="max-height:32px; vertical-align:middle;"/> | **Aliw 23 Channel** | <code>aliw23channel.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/aliw%2023%20channel.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/abs-cbn%20sa%20alltv2.png" alt="ALLTV2" height="32" style="max-height:32px; vertical-align:middle;"/> | **ALLTV2** | <code>ALLTV2.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/abs-cbn%20sa%20alltv2.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/anc.png" alt="ANC" height="32" style="max-height:32px; vertical-align:middle;"/> | **ANC** | <code>anc.ph</code> | News | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/anc.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cinema%20one.png" alt="Cinema One" height="32" style="max-height:32px; vertical-align:middle;"/> | **Cinema One** | <code>cinemaone.ph</code> | Movies | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cinema%20one.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cinemo.png" alt="Cinemo" height="32" style="max-height:32px; vertical-align:middle;"/> | **Cinemo** | <code>cinemo.ph</code> | Movies | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cinemo.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cltv%2036.png" alt="CLTV 36" height="32" style="max-height:32px; vertical-align:middle;"/> | **CLTV 36** | <code>cltv36.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/cltv%2036.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/dzmm%20teleradyo.png" alt="DZMM Teleradyo" height="32" style="max-height:32px; vertical-align:middle;"/> | **DZMM Teleradyo** | <code>dzmmteleradyo.ph</code> | News | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/dzmm%20teleradyo.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/dzrh%20tv.png" alt="DZRH TV" height="32" style="max-height:32px; vertical-align:middle;"/> | **DZRH TV** | <code>dzrhtv.ph</code> | News | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/dzrh%20tv.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/ewtn.png" alt="EWTN" height="32" style="max-height:32px; vertical-align:middle;"/> | **EWTN** | <code>ewtn.ph</code> | Religious | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/ewtn.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/gma.png" alt="GMA" height="32" style="max-height:32px; vertical-align:middle;"/> | **GMA** | <code>gma.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/gma.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/gtv.png" alt="GTV" height="32" style="max-height:32px; vertical-align:middle;"/> | **GTV** | <code>gtv.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/gtv.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/ibc%2013.png" alt="IBC 13" height="32" style="max-height:32px; vertical-align:middle;"/> | **IBC 13** | <code>ibc13.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/ibc%2013.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/inc%20radio.png" alt="INC Radio" height="32" style="max-height:32px; vertical-align:middle;"/> | **INC Radio** | <code>incradio.ph</code> | Religious | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/inc%20radio.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/inc%20tv.png" alt="INC TV" height="32" style="max-height:32px; vertical-align:middle;"/> | **INC TV** | <code>inctv.ph</code> | Religious | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/inc%20tv.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/abs-cbn%20kapamilya%20channel.png" alt="Kapamilya Channel" height="32" style="max-height:32px; vertical-align:middle;"/> | **Kapamilya Channel** | <code>abscbnkapamilyachannel.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/abs-cbn%20kapamilya%20channel.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/abs-cbn%20kapamilya%20channel%20hd.png" alt="Kapamilya Channel HD" height="32" style="max-height:32px; vertical-align:middle;"/> | **Kapamilya Channel HD** | <code>KapamilyaChannelHD.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/abs-cbn%20kapamilya%20channel%20hd.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/metro%20channel.png" alt="Metro Channel" height="32" style="max-height:32px; vertical-align:middle;"/> | **Metro Channel** | <code>metrochannel.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/metro%20channel.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/moviesphere.png" alt="Moviesphere" height="32" style="max-height:32px; vertical-align:middle;"/> | **Moviesphere** | <code>moviesphere.ph</code> | Movies | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/moviesphere.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/myx.png" alt="MYX" height="32" style="max-height:32px; vertical-align:middle;"/> | **MYX** | <code>myx.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/myx.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/net25.png" alt="Net25" height="32" style="max-height:32px; vertical-align:middle;"/> | **Net25** | <code>net25.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/net25.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/one%20news%20ph.png" alt="One News PH" height="32" style="max-height:32px; vertical-align:middle;"/> | **One News PH** | <code>onenewsph.ph</code> | News | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/one%20news%20ph.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/one%20ph.png" alt="One PH" height="32" style="max-height:32px; vertical-align:middle;"/> | **One PH** | <code>oneph.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/one%20ph.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/one%20sports.png" alt="One Sports" height="32" style="max-height:32px; vertical-align:middle;"/> | **One Sports** | <code>onesports.ph</code> | Sports | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/one%20sports.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/pba%20rush.png" alt="PBA Rush" height="32" style="max-height:32px; vertical-align:middle;"/> | **PBA Rush** | <code>pbarush.ph</code> | Sports | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/pba%20rush.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/pbo.png" alt="PBO" height="32" style="max-height:32px; vertical-align:middle;"/> | **PBO** | <code>pbo.ph</code> | Movies | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/pbo.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/ptv%204.png" alt="PTV 4" height="32" style="max-height:32px; vertical-align:middle;"/> | **PTV 4** | <code>ptv4.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/ptv%204.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/rptv.png" alt="RPTV" height="32" style="max-height:32px; vertical-align:middle;"/> | **RPTV** | <code>rptv.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/rptv.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/smni.png" alt="SMNI" height="32" style="max-height:32px; vertical-align:middle;"/> | **SMNI** | <code>smni.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/smni.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tap%20actionflix.png" alt="Tap Actionflix" height="32" style="max-height:32px; vertical-align:middle;"/> | **Tap Actionflix** | <code>tapactionflix.ph</code> | Movies | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tap%20actionflix.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tap%20movies.png" alt="Tap Movies" height="32" style="max-height:32px; vertical-align:middle;"/> | **Tap Movies** | <code>tapmovies.ph</code> | Movies | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tap%20movies.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tap%20sports.png" alt="Tap Sports" height="32" style="max-height:32px; vertical-align:middle;"/> | **Tap Sports** | <code>tapsports.ph</code> | Sports | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tap%20sports.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tap%20tv.png" alt="Tap TV" height="32" style="max-height:32px; vertical-align:middle;"/> | **Tap TV** | <code>taptv.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tap%20tv.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tv5.png" alt="Tv5" height="32" style="max-height:32px; vertical-align:middle;"/> | **Tv5** | <code>tv5.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/tv5.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/untv.png" alt="UNTV" height="32" style="max-height:32px; vertical-align:middle;"/> | **UNTV** | <code>untv.ph</code> | Entertainment | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/untv.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/vivacinema.png" alt="Vivacinema" height="32" style="max-height:32px; vertical-align:middle;"/> | **Vivacinema** | <code>vivacinema.ph</code> | Movies | PH | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/vivacinema.png) |
| <img src="https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/fox%20news%20channel.png" alt="Fox News Channel" height="32" style="max-height:32px; vertical-align:middle;"/> | **Fox News Channel** | <code>foxnewschannel.us</code> | News | US | `Stored (Repo)` | [Direct Link](https://cdn.jsdelivr.net/gh/DMCDdev/tv-channel-logos@main/logos/fox%20news%20channel.png) |

---

## Automation

This repository includes a GitHub Actions workflow (`.github/workflows/update-catalog.yml`). Whenever you commit changes to `channels.json` or add files to `logos/`, the workflow automatically:
1. Auto-discovers and validates all channels.
2. Generates updated `logos.json`.
3. Rebuilds the visual Markdown table in `README.md`.
4. Commits and pushes the updates back to `main`.
