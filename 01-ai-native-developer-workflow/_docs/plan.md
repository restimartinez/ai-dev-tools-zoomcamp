# Implementation Plan: Family Chore Manager

## Project goal

Build a small, responsive Django web app for one household to manage shared chores, award points, and show a weekly family ranking. Architecture stays beginner-friendly: one Django app, server-rendered templates, SQLite for local development.

## MVP scope

**In scope**

- Login / logout (Django auth)
- Parent creates and deactivates family members
- Parent creates, edits (while open), and cancels tasks
- Assign task to one member or leave unassigned
- Fixed points per task
- Any active member can complete any open task
- Immutable completion history (completer, time, assignee, points)
- Recurring tasks: daily, weekly, or selected weekdays; next occurrence only on completion
- Ranking: current calendar week (Mon–Sun), then all-time as tie-breaker
- Responsive HTML/CSS for desktop and mobile browsers

**Out of scope**

- Notifications, native/offline apps, multi-family, co-admins
- REST API / SPA
- Editing or deleting completed history
- Auto-creating the next occurrence while a task is still pending

## Main user roles and permissions

| Role | Permissions |
|------|-------------|
| **Parent (admin)** | Create/deactivate members; create/edit/cancel open tasks; set points, assignee, recurrence; complete tasks; view history and ranking |
| **Family member** | Log in; view open tasks; complete any open task; view history and ranking |
| **Deactivated member** | Cannot log in or complete tasks; historical completions and points remain |

The parent is also a family member and can earn points. Exactly one parent per family. First parent account is created via Django admin or a one-time setup (no self-service family registration).

## Main features

1. **Authentication** — Session login/logout; protect all app views.
2. **Member management** — Parent-only create and deactivate.
3. **Task board** — List open tasks for all active members.
4. **Task management** — Parent CRUD for open tasks (create, edit, cancel).
5. **Complete task** — Award points to completer; record assignee and completer.
6. **Recurrence** — On complete, spawn next occurrence with same settings.
7. **History** — Read-only list of completions.
8. **Ranking** — Sort by current-week points, then all-time points.

## Data models and relationships

Keep models few and explicit. Prefer Django `User` for credentials.

```
User (Django auth)
  └── FamilyMember (1:1)
        - is_parent: bool
        - is_active: bool
        - display name (optional; else use User.get_username())

Task
  - title
  - points: positive integer
  - assignee: FK → FamilyMember, null=True (unassigned)
  - status: open | completed | cancelled
  - recurrence: none | daily | weekly | weekdays
  - weekdays: optional (for selected-weekdays recurrence)
  - created_by: FK → FamilyMember (parent)
  - created_at
  - related open/closed instances are separate Task rows when recurring

TaskCompletion
  - task: FK → Task (the occurrence that was completed)
  - completed_by: FK → FamilyMember
  - assigned_to: FK → FamilyMember, null=True (snapshot at completion)
  - points_awarded: integer (snapshot)
  - completed_at
  - immutable after create (no update/delete in app logic)
```

**Relationships**

- One `User` ↔ one `FamilyMember`.
- `Task.assignee` → optional `FamilyMember`.
- `TaskCompletion` → one `Task`, one completer, optional assignee snapshot.
- Recurring work = new `Task` row created when the previous open task is completed.

**Notes for beginners**

- Do not model “Family” as a table in MVP (single household).
- Store point snapshots on `TaskCompletion` so later task edits do not change history.
- Week boundaries use one timezone from Django settings.

## Main business rules

1. Only the parent creates/edits/cancels open tasks and manages members.
2. Open tasks may be assigned or unassigned; any active member may complete them.
3. Points go to the completer; history always keeps original assignee and completer.
4. Parent may change points, assignment, and recurrence only while status is open.
5. Completed and cancelled tasks are not editable for scoring fields; completions are never deleted.
6. Cancelling an open task awards no points and does not create a next occurrence.
7. Recurring: if pending, it stays pending; next occurrence is created only on completion.
8. Ranking: sum points in current Mon–Sun week first; all-time points break ties.
9. Deactivated members keep history; exclude them from assignee picker and from completing tasks.
10. No notifications in v1.

## Suggested implementation phases

### Phase 1 — Project skeleton
- Create Django project and one app (e.g. `chores`)
- Settings: auth, timezone, static files, templates
- Base layout template (responsive)
- Login / logout pages

### Phase 2 — Members
- `FamilyMember` model + migration
- Parent-only views/forms: create member, deactivate member
- List active members
- Seed/create the parent via Django admin if needed

### Phase 3 — Tasks (non-recurring)
- `Task` model with open/completed/cancelled
- Parent: create, edit open task, cancel
- All members: list open tasks
- Complete action → create `TaskCompletion`, mark task completed, award points to completer

### Phase 4 — History and ranking
- History page (read-only completions)
- Ranking page: current week + all-time; sort rules as specified
- Simple helpers/services for week range and point totals (plain functions, not a heavy service layer)

### Phase 5 — Recurrence
- Add recurrence fields to `Task`
- On complete of recurring task: create next open `Task` (daily / weekly / selected weekdays)
- Parent can edit recurrence while task is open

### Phase 6 — Polish
- Permission checks on every mutating view
- Responsive CSS pass
- Empty states and basic validation messages
- Django admin registration for debugging (optional)

## Testing strategy

Keep tests practical and focused on business rules (Django `TestCase`).

**Model / logic tests**

- Completing a task creates a completion with correct completer, assignee snapshot, and points
- Completer receives points even if different from assignee
- Recurring completion creates exactly one next open task; pending recurring task does not spawn another
- Cancel does not create completion or next occurrence
- Deactivated member cannot be treated as active for completion (view/permission tests)

**Permission tests**

- Non-parent cannot create/edit/cancel tasks or manage members
- Anonymous users redirected to login
- Deactivated user cannot log in (or cannot access app)

**Ranking tests**

- Week window Mon–Sun (timezone-aware)
- Sort by current-week points, then all-time

**What not to over-test in MVP**

- Pixel-perfect UI, browser E2E, performance

Run from this homework directory (`01-ai-native-developer-workflow/`): `uv run python manage.py test`

## Definition of done

- [ ] Parent can create/deactivate members
- [ ] Parent can create, edit, and cancel open tasks (points, assignee, recurrence)
- [ ] Active members can view open tasks and complete any of them
- [ ] Completions store completer, assignee, points, and timestamp; history is immutable in the UI
- [ ] Recurring tasks spawn the next occurrence only on completion
- [ ] Ranking shows current week (Mon–Sun) and all-time, sorted correctly
- [ ] App works in a desktop and mobile browser viewport
- [ ] Core business rules covered by automated tests
- [ ] README with how to run locally (install, migrate, createsuperuser/parent, runserver)
- [ ] No features from the out-of-scope list shipped “half-done”

## Architecture constraints (beginner Django)

- One app, MVT (models–views–templates), forms + Django auth
- No Celery, channels, or external task queues
- No separate API layer
- Prefer clarity over abstraction; small helper functions for recurrence dates and weekly totals are enough
