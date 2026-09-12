import type { Task, TaskInput, TaskStatus } from '../types/task'

const API_BASE_URL = 'http://localhost:8000'

function validateTitle(title: string): string {
  const trimmed = title.trim()
  if (!trimmed) {
    throw new Error('Title is required.')
  }
  return trimmed
}

async function readErrorDetail(response: Response): Promise<string> {
  try {
    const body: unknown = await response.json()
    if (
      typeof body === 'object' &&
      body !== null &&
      'detail' in body &&
      (body as { detail: unknown }).detail !== undefined
    ) {
      const detail = (body as { detail: unknown }).detail
      return typeof detail === 'string' ? detail : JSON.stringify(detail)
    }
    return JSON.stringify(body)
  } catch {
    return response.statusText || 'Unknown error'
  }
}

async function handleResponse(response: Response): Promise<void> {
  if (response.ok) {
    return
  }

  const detail = await readErrorDetail(response)
  throw new Error(`HTTP ${response.status}: ${detail}`)
}

export async function getTasks(): Promise<Task[]> {
  const response = await fetch(`${API_BASE_URL}/tasks`)
  await handleResponse(response)
  return (await response.json()) as Task[]
}

export async function createTask(input: TaskInput): Promise<Task> {
  const response = await fetch(`${API_BASE_URL}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      title: validateTitle(input.title),
      description: input.description.trim(),
      status: input.status,
    }),
  })
  await handleResponse(response)
  return (await response.json()) as Task
}

export async function updateTask(id: string, input: TaskInput): Promise<Task> {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      title: validateTitle(input.title),
      description: input.description.trim(),
      status: input.status,
    }),
  })
  await handleResponse(response)
  return (await response.json()) as Task
}

export async function deleteTask(id: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
    method: 'DELETE',
  })
  await handleResponse(response)
}

export async function moveTask(id: string, status: TaskStatus): Promise<Task> {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}/status`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status }),
  })
  await handleResponse(response)
  return (await response.json()) as Task
}
