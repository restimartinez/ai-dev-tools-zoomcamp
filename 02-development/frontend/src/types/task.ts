export const TASK_STATUSES = ['TODO', 'IN_PROGRESS', 'DONE'] as const

export type TaskStatus = (typeof TASK_STATUSES)[number]

export interface Task {
  id: string
  title: string
  description: string
  status: TaskStatus
}

export type TaskInput = {
  title: string
  description: string
  status: TaskStatus
}

export const STATUS_LABELS: Record<TaskStatus, string> = {
  TODO: 'TODO',
  IN_PROGRESS: 'IN PROGRESS',
  DONE: 'DONE',
}

export const COLUMN_ORDER: TaskStatus[] = ['TODO', 'IN_PROGRESS', 'DONE']
