# Flux

Flux is a Mini Kanban Board for managing tasks on a single board.

This project is being developed as part of the **DataTalksClub AI Dev Tools Zoomcamp Homework 2**.

## Purpose

Flux helps you track work visually with three fixed columns:

- **TODO**
- **IN PROGRESS**
- **DONE**

You can **create**, **view**, **edit**, **delete**, and **move** tasks between columns.

## Development

### Prerequisites

- [Node.js](https://nodejs.org/) (LTS recommended) and npm

### Frontend

The frontend is a Vite + React + TypeScript app under [`frontend/`](frontend/).
It currently uses an in-memory mock data layer in `frontend/src/services/taskService.ts`, so it runs without a backend.

```bash
cd frontend
npm install
npm run dev
```

Then open the URL shown in the terminal (usually `http://localhost:5173`).

Other useful commands:

```bash
cd frontend
npm run build    # production build
npm run preview  # preview the production build
```

### Backend

Backend setup (FastAPI + SQLite + SQLAlchemy) will be documented here once implemented.

## Project layout

```text
02-development/
├── _docs/specs.md      # Product requirements (source of truth)
├── AGENTS.md           # Guidance for contributors / AI agents
├── README.md
└── frontend/           # React Kanban UI (mock data for now)
```

For product requirements, see [`_docs/specs.md`](_docs/specs.md).
For agent/contributor guidance, see [`AGENTS.md`](AGENTS.md).
