# AI Career Copilot

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite) ![ATS](https://img.shields.io/badge/ATS-6C5CE7?style=flat-square) ![Resume](https://img.shields.io/badge/Resume-000000?style=flat-square&logo=markdown)

Analyze a resume against a job description and generate ATS keywords, gaps, bullets, and a cover letter draft.

![copilot-demo](screenshots/copilot-demo.png)

## Why this project exists

This is a portfolio-ready MVP in the **career services** lane. It demonstrates practical API product thinking, clean documentation, tests, and a working local browser demo.

## Features

- Resume/job description analyzer
- Keyword overlap scoring
- Skill gap detection
- Improved resume bullet suggestions
- Cover letter draft generator

## Tech Stack

- Python 3.11+
- FastAPI
- SQLite
- Vanilla HTML/CSS/JS frontend served by the API
- Pytest API tests

## Quick Start

```bash
uv sync
uv run uvicorn src.main:app --reload --port 8102
```

Then open: http://localhost:8102

Windows one-click launcher: `run.bat`

## API

- `GET /` - browser demo
- `GET /api/health` - health check
- `GET /docs` - interactive FastAPI docs

## Verification

```bash
uv run pytest -q
```

## Roadmap

- Add authenticated user accounts
- Add production deployment config
- Replace deterministic helper logic with local Ollama model calls where useful
- Add screenshots and a short demo GIF
