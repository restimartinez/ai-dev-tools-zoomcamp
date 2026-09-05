# MVP Backlog: Family Chore Manager

Ordered by dependency. Source of truth: `_docs/plan.md`.

## 1. Finish project foundation and authentication

Complete Phase 1 settings that remain after the Django skeleton: timezone, template dirs, and static files. Add a responsive base layout, login/logout using Django auth, and require login for all app views.

## 2. FamilyMember model and parent bootstrap

Add the `FamilyMember` model (1:1 with Django `User`: `is_parent`, `is_active`, optional display name) and migrations. Document or support creating the first parent via Django admin (no self-service registration).

## 3. Member management (parent-only)

Parent-only forms/views to create members and deactivate members, plus a list of active members. Deactivated members must not log in or complete tasks; their history remains.

## 4. Task model and open-task board (non-recurring)

Add the `Task` model with title, points, optional assignee, status (`open` / `completed` / `cancelled`), `created_by`, and `created_at`. Show a board listing open tasks for all active members.

## 5. Parent task management (create, edit, cancel)

Parent-only create/edit for open tasks (points, assignee) and cancel without awarding points. Non-parents cannot mutate tasks. Edits allowed only while status is open.

## 6. Task completion and TaskCompletion history

Any active member can complete any open task: create an immutable `TaskCompletion` (completer, assignee snapshot, points snapshot, timestamp), mark the task completed, and award points to the completer. Add a read-only history page.

## 7. Recurring tasks

Add recurrence fields on `Task` (`none` / `daily` / `weekly` / `weekdays`, plus optional weekdays). On completion of a recurring task only, spawn the next open `Task` with the same settings. Parent can edit recurrence while the task is open; cancel does not spawn a next occurrence.

## 8. Weekly and all-time ranking

Add a ranking page that sorts active members by points in the current calendar week (Mon–Sun, timezone-aware), then by all-time points as a tie-breaker. Use small helper functions for week range and totals.

## 9. Permissions polish, responsive UI, and empty states

Enforce permission checks on every mutating view. Finish responsive CSS for desktop and mobile. Add empty states and basic validation messages. Optionally register models in Django admin for debugging.

## 10. Automated tests and README

Add focused Django `TestCase` coverage for completion/history rules, permissions, deactivated members, recurrence-on-complete, cancel behavior, and ranking sort/week window. Add a README with install, migrate, create parent, and runserver steps.
