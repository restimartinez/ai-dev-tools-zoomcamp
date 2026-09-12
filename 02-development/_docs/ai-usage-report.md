# AI Usage Report

## 1. Overview

Flux was developed as an AI-assisted software development project for the DataTalksClub AI Dev Tools Zoomcamp Homework 2.

AI was used as a development assistant throughout the project, while the final implementation, validation, testing, and decisions were reviewed and executed by the developer.

## 2. How AI was used

AI assistance was used for the following activities:

### Product specification

AI was used to help define and refine the product specification for the Mini Kanban Board.

The specification was used as the source of truth for the implementation and included:

* Product goals and scope.
* Functional requirements.
* Task data model.
* Kanban board behavior.
* User interactions.
* Acceptance criteria.
* Explicitly out-of-scope features.

### Project structure and architecture

AI was used to discuss and validate a simple full-stack architecture:

* React + TypeScript frontend.
* FastAPI backend.
* OpenAPI API contract.
* SQLite database.
* SQLAlchemy for database access.
* Automated backend tests.

The architecture was intentionally kept small to match the homework scope.

### Frontend development

AI assistance was used to help implement and review the frontend components, including:

* Kanban board layout.
* Task columns.
* Task cards.
* Task creation and editing form.
* Task status changes.
* Task deletion.
* API service layer.

The frontend was initially developed with mocked data and was later connected to the real backend API.

### API design

AI was used to help design the REST API contract in `openapi.yaml`.

The API covers:

* Listing tasks.
* Creating tasks.
* Updating tasks.
* Moving tasks between columns.
* Deleting tasks.

The OpenAPI contract was created before implementing the backend endpoints.

### Backend development

AI assistance was used during the implementation of the FastAPI backend.

The backend was developed incrementally:

1. FastAPI project structure.
2. Pydantic request and response models.
3. In-memory task store.
4. REST API endpoints.
5. Automated tests.
6. SQLite persistence.
7. SQLAlchemy integration.

The initial in-memory implementation was intentionally used before introducing the database, making it possible to validate the API independently from the persistence layer.

### Database implementation

AI was used to help implement the persistence layer using SQLAlchemy and SQLite.

The database implementation includes:

* SQLAlchemy engine configuration.
* Declarative model for tasks.
* Database sessions.
* CRUD operations.
* SQLite persistence across application restarts.

The database layer was designed so that the application logic is not directly dependent on SQLite-specific operations.

### Testing

AI was used to help design and review backend tests based on the API contract.

The test suite verifies:

* Listing tasks.
* Creating tasks.
* Updating tasks.
* Moving tasks.
* Deleting tasks.
* Validation errors.
* Not-found behavior.
* Persistence-related API behavior.

The final backend test suite contains 15 tests.

The tests use an isolated in-memory SQLite database so that test execution does not modify the development database.

### Debugging

AI assistance was also used to investigate and resolve development issues.

Examples included:

* Frontend/backend integration problems.
* CORS configuration.
* Uvicorn process/reload behavior.
* API request and response errors.
* Database persistence verification.
* SQLAlchemy session handling.
* Test isolation.

AI suggestions were tested against the actual application rather than being accepted without verification.

### Documentation

AI was used to help structure and improve project documentation, including:

* `README.md`
* `AGENTS.md`
* `product-spec.md`
* `openapi.yaml`
* This AI usage report.

## 3. Development workflow

The general workflow used during the project was:

1. Define the product requirements.
2. Create the project structure.
3. Define the API contract.
4. Implement the frontend using mocked data.
5. Implement the backend API.
6. Add automated tests.
7. Connect the frontend to the backend.
8. Replace the in-memory store with SQLite and SQLAlchemy.
9. Verify persistence.
10. Run the complete test and build checks.
11. Review and document the final implementation.

AI was used as an assistant during these steps, but changes were reviewed and executed locally in the development environment.

## 4. Verification

The final implementation was verified locally.

Backend tests:

```text
15 passed
```

Frontend checks:

```text
npm run lint
npm run build
```

The application was also manually tested through the API to verify that tasks persisted after restarting the backend.

## 5. AI-assisted development principles

The following principles were followed when using AI:

* The product specification remained the source of truth.
* AI-generated suggestions were reviewed before being applied.
* Changes were tested locally.
* Existing functionality was checked after significant changes.
* The implementation was kept intentionally simple.
* Unnecessary features suggested by AI were not added when they were outside the product scope.
* The developer remained responsible for the final code, architecture, testing, and decisions.
