# Raspberry Pi Climate Early Warning System

An open-source Raspberry Pi climate early warning system designed to monitor environmental conditions such as rainfall, atmospheric pressure, temperature, and river levels.

This prototype demonstrates how low-cost edge computing systems can contribute to climate resilience by detecting environmental changes that may precede floods, storms, or other climate-related hazards.

## SDG Alignment

Primary:

SDG 13 — Climate Action

Supporting:

- SDG 9 — Industry, Innovation and Infrastructure
- SDG 11 — Sustainable Cities and Communities

Environmental monitoring enables earlier responses to emerging climate risks.

## System Overview

The system collects environmental data from sensors and logs the information locally for analysis.

Typical monitored variables include:

- temperature
- humidity
- atmospheric pressure
- rainfall
- water level

The Raspberry Pi acts as a small environmental monitoring node capable of collecting continuous environmental observations.

## Hardware Components

- Raspberry Pi 4 or Raspberry Pi Zero 2 W
- BME280 environmental sensor
- tipping-bucket rain gauge
- ultrasonic water level sensor
- ADS1115 ADC (optional)
- microSD card
- solar power system (optional)

## System Architecture

Sensors → Raspberry Pi → Local Data Logging → Analysis / Alerting

The Raspberry Pi collects environmental data, stores readings locally, and can support alert logic for abnormal conditions.

## Repository Structure

raspberry-pi-climate-early-warning-system/

README.md
LICENSE
requirements.txt

src/
  read_climate_sensors.py
  log_climate_data.py
  anomaly_detection.py
  alert_engine.py

docs/
  setup_guide.md
  deployment_notes.md
  sensor_notes.md

data/
  example_climate_readings.csv

hardware/

## Applications

Possible uses include:

- flood early warning systems
- environmental monitoring stations
- climate research prototypes
- citizen science weather stations
- disaster resilience infrastructure

## License

MIT License

## Sustainable Catalyst

Part of the Sustainable Catalyst Sustainability Engineering Series.
