import type { Task, TaskInput, TaskStatus } from '../types/task'

/**
 * In-memory task store for the frontend MVP.
 * Replace the implementations in this module with HTTP calls
 * when the FastAPI backend is available.
 */

const sampleTasks: Task[] = [
  {
    id: '1',
    title: 'Set up project structure',
    description: 'Create frontend and backend folders for Flux.',
    status: 'DONE',
  },
  {
    id: '2',
    title: 'Design Kanban board UI',
    description: 'Build three columns for TODO, IN PROGRESS, and DONE.',
    status: 'IN_PROGRESS',
  },
  {
    id: '3',
    title: 'Connect to FastAPI backend',
    description: 'Replace mock data with real API requests.',
    status: 'TODO',
  },
  {
    id: '4',
    title: 'Write homework notes',
    description: 'Document decisions made while building Flux.',
    status: 'TODO',
  },
]

let tasks: Task[] = structuredClone(sampleTasks)
let nextId = 5

function validateTitle(title: string): string {
  const trimmed = title.trim()
  if (!trimmed) {
    throw new Error('Title is required.')
  }
  return trimmed
}

function findTaskIndex(id: string): number {
  const index = tasks.findIndex((task) => task.id === id)
  if (index === -1) {
    throw new Error(`Task not found: ${id}`)
  }
  return index
}

export async function getTasks(): Promise<Task[]> {
  return structuredClone(tasks)
}

export async function createTask(input: TaskInput): Promise<Task> {
  const task: Task = {
    id: String(nextId++),
    title: validateTitle(input.title),
    description: input.description.trim(),
    status: input.status,
  }
  tasks = [...tasks, task]
  return structuredClone(task)
}

export async function updateTask(id: string, input: TaskInput): Promise<Task> {
  const index = findTaskIndex(id)
  const updated: Task = {
    ...tasks[index],
    title: validateTitle(input.title),
    description: input.description.trim(),
    status: input.status,
  }
  tasks = tasks.map((task, i) => (i === index ? updated : task))
  return structuredClone(updated)
}

export async function deleteTask(id: string): Promise<void> {
  findTaskIndex(id)
  tasks = tasks.filter((task) => task.id !== id)
}

export async function moveTask(id: string, status: TaskStatus): Promise<Task> {
  const index = findTaskIndex(id)
  const updated: Task = { ...tasks[index], status }
  tasks = tasks.map((task, i) => (i === index ? updated : task))
  return structuredClone(updated)
}
