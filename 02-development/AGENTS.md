# AGENTS.md — Flux

## Project

Flux is a small full-stack Mini Kanban Board application for DataTalksClub AI Dev Tools Zoomcamp Homework 2.

Treat [`_docs/specs.md`](_docs/specs.md) as the **source of truth** for product requirements. Do not invent features or requirements that are not present in that specification.

## Architecture

- The project has a **frontend** and a **backend**.
- Keep frontend and backend **clearly separated**.
- The backend will eventually use **FastAPI**, **SQLite**, and **SQLAlchemy**.
- Keep the implementation intentionally simple and suitable for a homework MVP.

## Scope boundaries

Do **not** introduce:

- Authentication or user accounts
- Multiple boards
- Notifications
- Real-time collaboration
- Any other feature explicitly excluded by `_docs/specs.md`

Stay within the specified task model and board behavior: one board, three columns (TODO, IN PROGRESS, DONE), and task create / view / edit / delete / move.

## Working style

- Prefer small, focused changes over large refactors.
- Align behavior with `_docs/specs.md` before adding polish or convenience features.
- When requirements are unclear, follow the specification rather than expanding scope.

## Testing

- Backend functionality **must** have tests.
- Add or update backend tests when changing API behavior, persistence, or task status/move logic.
