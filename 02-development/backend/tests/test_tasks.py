"""Contract tests for the Flux task API (openapi.yaml).

These tests are written before the task endpoints are implemented and are
expected to fail until the API is added.
"""

from fastapi.testclient import TestClient

MISSING_TASK_ID = "nonexistent-task-id"


def _create_task(
    client: TestClient,
    *,
    title: str = "Sample task",
    description: str = "Sample description",
    status: str | None = None,
) -> dict:
    payload: dict = {"title": title, "description": description}
    if status is not None:
        payload["status"] = status

    response = client.post("/tasks", json=payload)
    assert response.status_code == 201, response.text
    return response.json()


def test_list_tasks_returns_200_and_json_array(client: TestClient) -> None:
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task_returns_201_with_generated_id_and_fields(
    client: TestClient,
) -> None:
    response = client.post(
        "/tasks",
        json={
            "title": "Connect to FastAPI backend",
            "description": "Replace mock data with real API requests.",
            "status": "IN_PROGRESS",
        },
    )

    assert response.status_code == 201
    task = response.json()
    assert "id" in task
    assert task["id"]
    assert task["title"] == "Connect to FastAPI backend"
    assert task["description"] == "Replace mock data with real API requests."
    assert task["status"] == "IN_PROGRESS"


def test_create_task_defaults_status_to_todo_when_omitted(
    client: TestClient,
) -> None:
    response = client.post(
        "/tasks",
        json={
            "title": "Write homework notes",
            "description": "Document decisions made while building Flux.",
        },
    )

    assert response.status_code == 201
    task = response.json()
    assert task["status"] == "TODO"


def test_get_task_returns_existing_task(client: TestClient) -> None:
    created = _create_task(
        client,
        title="Design Kanban board UI",
        description="Build three columns.",
        status="TODO",
    )

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    task = response.json()
    assert task["id"] == created["id"]
    assert task["title"] == "Design Kanban board UI"
    assert task["description"] == "Build three columns."
    assert task["status"] == "TODO"


def test_get_task_returns_404_for_missing_task(client: TestClient) -> None:
    response = client.get(f"/tasks/{MISSING_TASK_ID}")

    assert response.status_code == 404


def test_update_task_updates_fields_and_returns_200(client: TestClient) -> None:
    created = _create_task(client, title="Old title", description="Old description")

    response = client.put(
        f"/tasks/{created['id']}",
        json={
            "title": "Design Kanban board UI",
            "description": "Build three columns for TODO, IN PROGRESS, and DONE.",
            "status": "DONE",
        },
    )

    assert response.status_code == 200
    task = response.json()
    assert task["id"] == created["id"]
    assert task["title"] == "Design Kanban board UI"
    assert task["description"] == (
        "Build three columns for TODO, IN PROGRESS, and DONE."
    )
    assert task["status"] == "DONE"


def test_update_task_returns_404_for_missing_task(client: TestClient) -> None:
    response = client.put(
        f"/tasks/{MISSING_TASK_ID}",
        json={
            "title": "Updated title",
            "description": "Updated description",
            "status": "TODO",
        },
    )

    assert response.status_code == 404


def test_move_task_changes_status_and_returns_200(client: TestClient) -> None:
    created = _create_task(client, status="TODO")

    response = client.patch(
        f"/tasks/{created['id']}/status",
        json={"status": "IN_PROGRESS"},
    )

    assert response.status_code == 200
    task = response.json()
    assert task["id"] == created["id"]
    assert task["status"] == "IN_PROGRESS"


def test_move_task_returns_404_for_missing_task(client: TestClient) -> None:
    response = client.patch(
        f"/tasks/{MISSING_TASK_ID}/status",
        json={"status": "DONE"},
    )

    assert response.status_code == 404


def test_delete_task_returns_204_and_removes_task(client: TestClient) -> None:
    created = _create_task(client, title="Task to delete")

    delete_response = client.delete(f"/tasks/{created['id']}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/tasks/{created['id']}")
    assert get_response.status_code == 404


def test_delete_task_returns_404_for_missing_task(client: TestClient) -> None:
    response = client.delete(f"/tasks/{MISSING_TASK_ID}")

    assert response.status_code == 404


def test_create_task_without_title_fails(client: TestClient) -> None:
    response = client.post(
        "/tasks",
        json={"description": "Missing title should fail."},
    )

    assert response.status_code == 422


def test_create_task_with_invalid_status_fails(client: TestClient) -> None:
    response = client.post(
        "/tasks",
        json={
            "title": "Invalid status task",
            "description": "Status is not allowed.",
            "status": "BLOCKED",
        },
    )

    assert response.status_code == 422


def test_update_task_with_invalid_status_fails(client: TestClient) -> None:
    created = _create_task(client)

    response = client.put(
        f"/tasks/{created['id']}",
        json={
            "title": created["title"],
            "description": created["description"],
            "status": "BLOCKED",
        },
    )

    assert response.status_code == 422


def test_move_task_with_invalid_status_fails(client: TestClient) -> None:
    created = _create_task(client)

    response = client.patch(
        f"/tasks/{created['id']}/status",
        json={"status": "BLOCKED"},
    )

    assert response.status_code == 422
