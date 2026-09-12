# Flux — Product Specification

**Application:** Flux
**Project:** Mini Kanban Board

## 1. Product overview

Flux (Mini Kanban Board) is a simple web application for managing tasks on a single board with three fixed columns: **TODO**, **IN PROGRESS**, and **DONE**.

It is intentionally small in scope and suitable as a homework project for the DataTalksClub AI Dev Tools Zoomcamp. The product focuses on basic task CRUD and moving tasks between columns. There is no authentication, no multi-board support, and no collaboration features.

## 2. Goals

* Provide a clear, usable Kanban board for personal task tracking.
* Support creating, viewing, editing, deleting, and moving tasks.
* Keep implementation and product scope small enough for a homework assignment.
* Demonstrate a complete, working MVP without unnecessary complexity.

## 3. Out of scope

The following are explicitly **not** part of this product:

* Authentication or user accounts
* Multiple boards or board switching
* Notifications
* Real-time collaboration
* Task assignment to people
* Due dates, priorities, labels, tags, or comments
* File attachments
* Drag-and-drop animations beyond basic move behavior (optional polish only; not required)
* Search, filtering, sorting beyond column grouping
* History, activity logs, or audit trails
* Mobile-native apps or offline support

## 4. Users

| User                  | Description                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Single board user** | Anyone using the application locally or in a shared demo environment. There is one implicit user and one board. No login is required. |

There are no roles, permissions, or multi-user concepts.

## 5. Functional requirements

| ID   | Requirement                                                                                             |
| ---- | ------------------------------------------------------------------------------------------------------- |
| FR-1 | The application displays a single Kanban board with exactly three columns: TODO, IN PROGRESS, and DONE. |
| FR-2 | Users can create a new task with a title, description, and initial status.                              |
| FR-3 | Users can view all tasks on the board, grouped by status into the three columns.                        |
| FR-4 | Users can edit an existing task’s title, description, and status.                                       |
| FR-5 | Users can delete an existing task.                                                                      |
| FR-6 | Users can move a task between the three columns (changing its status).                                  |
| FR-7 | Each task has a unique ID assigned by the system.                                                       |
| FR-8 | The application supports exactly one board; board creation or selection is not offered.                 |

## 6. Task data model

A **Task** is the only domain entity required for the MVP.

| Field         | Type                                                    | Required               | Description                                                                                                                                               |
| ------------- | ------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`          | unique identifier (e.g. UUID or auto-increment integer) | Yes (system-generated) | Uniquely identifies the task. Not editable by the user.                                                                                                   |
| `title`       | string                                                  | Yes                    | Short name of the task. Must not be empty.                                                                                                                |
| `description` | string                                                  | Yes                    | Longer details about the task. May be empty string if the product allows blank descriptions; if blank is allowed, treat it as valid empty text, not null. |
| `status`      | enum                                                    | Yes                    | One of: `TODO`, `IN_PROGRESS`, `DONE`. Determines which column the task appears in.                                                                       |

### Status values

| Status value  | Column label |
| ------------- | ------------ |
| `TODO`        | TODO         |
| `IN_PROGRESS` | IN PROGRESS  |
| `DONE`        | DONE         |

### Constraints

* `id` is unique across all tasks on the board.
* `title` must be a non-empty string after trimming whitespace.
* `status` must be one of the three allowed values.
* There is no separate Board entity in the MVP; all tasks belong to the single implicit board.

## 7. Kanban board behavior

* The board always shows three columns in this order: **TODO → IN PROGRESS → DONE**.
* Each column lists the tasks whose `status` matches that column.
* Creating a task places it in the column matching its chosen (or default) status. Default status for new tasks is **TODO** unless the user selects another status at creation.
* Moving a task updates its `status` so it appears in the destination column.
* Editing a task’s status is equivalent to moving it to the corresponding column.
* Deleting a task removes it from the board permanently (hard delete is acceptable for this homework scope).
* An empty column is valid and should still be visible.
* Column order and column names are fixed; users cannot rename, add, or remove columns.

## 8. User interactions

### Create task

1. User initiates “create task” (e.g. button or form).
2. User enters title and description, and optionally selects status (default: TODO).
3. System validates required fields and creates the task with a unique ID.
4. Task appears in the matching column.

### View tasks

1. User opens the board.
2. System shows all tasks grouped into the three columns.

### Edit task

1. User selects a task to edit.
2. User updates title, description, and/or status.
3. System saves changes and refreshes the board view so the task reflects the new data (and column, if status changed).

### Delete task

1. User selects a task to delete.
2. User confirms deletion (confirmation recommended for safety).
3. System removes the task; it no longer appears on the board.

### Move task

1. User chooses to move a task to a different column (e.g. move control, status change, or equivalent UI action).
2. System updates the task status to the destination column’s status.
3. Task disappears from the previous column and appears in the new one.

## 9. Acceptance criteria

The product meets the homework MVP when all of the following are true:

1. **Board layout** — Opening the app shows one board with three columns labeled TODO, IN PROGRESS, and DONE.
2. **Create** — A user can create a task with title, description, and status; the task receives a unique ID and appears in the correct column.
3. **View** — All existing tasks are visible on the board, each in the column matching its status.
4. **Edit** — A user can change a task’s title, description, and status; changes persist and are reflected on the board.
5. **Delete** — A user can delete a task; it is removed from the board and no longer listed.
6. **Move** — A user can move a task from any column to either of the other two columns; its status updates accordingly.
7. **Unique ID** — No two tasks share the same ID.
8. **Single board** — There is no UI or flow for creating, selecting, or managing multiple boards.
9. **No auth** — The app is usable without login or registration.
10. **Scope** — The delivered product does not include notifications, real-time collaboration, or other items listed in Out of scope as required features.
