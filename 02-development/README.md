# Flux

Flux is a Mini Kanban Board for managing tasks on a single board.

This project is being developed as part of the **DataTalksClub AI Dev Tools Zoomcamp Homework 2**.

## Purpose

Flux helps you track work visually with three fixed columns:

* **TODO**
* **IN PROGRESS**
* **DONE**

You can:

* Create tasks.
* View tasks.
* Edit tasks.
* Delete tasks.
* Move tasks between columns.

The application uses a React frontend, a FastAPI backend, and SQLite for persistent storage.

## Requirements

* Node.js (LTS recommended) and npm
* Python 3.13+
* [uv](https://docs.astral.sh/uv/)

## Running the application

The application consists of two parts: the frontend and the backend.

### 1. Start the backend

Open a terminal and run:

```bash
cd 02-development/backend
uv sync
uv run uvicorn app.main:app --port 8000
```

The backend will be available at:

```text
http://localhost:8000
```

FastAPI's interactive API documentation is available at:

```text
http://localhost:8000/docs
```

The backend uses SQLite. The database file `flux.db` is created automatically in the `backend/` directory when the application starts.

### 2. Start the frontend

Open a second terminal and run:

```bash
cd 02-development/frontend
npm install
npm run dev
```

Then open the URL shown in the terminal, usually:

```text
http://localhost:5173
```

The frontend communicates with the backend API running on port 8000.

## Testing

### Backend tests

From the repository root:

```bash
cd 02-development/backend
uv run pytest
```

The test suite uses an isolated in-memory SQLite database.

### Frontend checks

From the frontend directory:

```bash
cd 02-development/frontend
npm run lint
npm run build
```

## API

The REST API contract is defined in:

```text
02-development/openapi.yaml
```

The main task endpoints are:

| Method | Endpoint                | Description    |
| ------ | ----------------------- | -------------- |
| GET    | `/tasks`                | List all tasks |
| POST   | `/tasks`                | Create a task  |
| GET    | `/tasks/{task_id}`      | Get a task     |
| PUT    | `/tasks/{task_id}`      | Update a task  |
| PATCH  | `/tasks/{task_id}/move` | Move a task    |
| DELETE | `/tasks/{task_id}`      | Delete a task  |

## Project layout

```text
02-development/
├── _docs/
│   ├── specs.md              # Product requirements / original specification
│   └── ai-usage-report.md    # AI-assisted development report
├── AGENTS.md                 # Guidance for contributors / AI agents
├── README.md                 # Project documentation
├── product-spec.md           # Product specification
├── openapi.yaml              # REST API contract
├── backend/
│   ├── app/
│   │   ├── database.py       # SQLAlchemy database configuration
│   │   ├── db_models.py      # Database models
│   │   ├── main.py           # FastAPI application and endpoints
│   │   ├── models
```
