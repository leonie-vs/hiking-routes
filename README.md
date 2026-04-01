# 🥾 Hiking Routes API (Manchester Public Transport)

## Overview

This project is a Python-based application designed to help find hiking routes that are accessible by public transport from Manchester.

As someone who enjoys hiking but doesn’t have a car, I often spend a lot of time manually searching for suitable routes, comparing travel times, and planning journeys. This project aims to automate that process by storing and filtering hiking routes based on key criteria.

---

## Features (MVP)

- Curated dataset of hiking routes stored in JSON
- Structured data including:
  - Distance, elevation, and duration (as ranges)
  - Public transport routes (departure, arrival, travel time, changes)
  - Additional metadata (e.g. pubs on route)
- Filtering logic for:
  - Maximum travel time (planned)
  - Route characteristics (planned)
- Built with Python using:
  - Pydantic for data modelling and validation
  - Pytest for test-driven development

---

## Example Use Case

> “Find a hike that is reachable within 60 minutes from Manchester and takes around 3–5 hours.”

---

## Tech Stack

- Python
- FastAPI (planned / in progress)
- Pytest (TDD approach)
- JSON (current data storage)

---

## Project Structure

```text
hiking-routes/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app (planned/in progress)
│   ├── models.py          # Pydantic models
│   ├── queries.py        # Filtering logic
│   ├── load_data.py      # Data access layer
│   └── data/
│       └── hikes.json     # Route data
│
├── tests/
│   └── test_services.py   # Unit tests
│
├── .venv/                 # Virtual environment (gitignored)
├── .gitignore
├── requirements.txt
└── README.md
```
---

## Future Improvements

- Migrate data to a relational database (e.g. PostgreSQL)
- Expose functionality via a REST API
- Add more advanced filtering and ranking
- Build a user-facing interface (e.g. chatbot or web app)
- Allow users to contribute routes
- Integrate external APIs for automated data collection

---

## Motivation

The goal of this project is to turn a time-consuming, manual planning process into a simple, data-driven tool — while also building practical experience in backend development, data modelling, and test-driven development.