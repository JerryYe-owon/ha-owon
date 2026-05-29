# OWON Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Home Assistant integration for OWON smart meters (PCT321, PCT341) via MQTT.

## Supported Devices

- OWON PCT321 (WiFi MQTT)
- OWON PCT341 (WiFi MQTT)

## Installation via HACS

1. Open HACS in Home Assistant
2. Click the three dots in the upper right corner → **Custom repositories**
3. Add `https://github.com/zzdota/ha-owon` as an **Integration**
4. Search for **OWON** and install
5. Restart Home Assistant

## Configuration

Go to **Settings → Devices & Services → Add Integration** and search for **OWON**.

Make sure MQTT is configured before adding this integration.

## Requirements

- Home Assistant with MQTT integration configured
- OWON smart meter connected to the same MQTT broker
