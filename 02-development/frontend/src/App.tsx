import { useCallback, useEffect, useState } from 'react'
import { Board } from './components/Board'
import { TaskForm } from './components/TaskForm'
import {
  createTask,
  deleteTask,
  getTasks,
  moveTask,
  updateTask,
} from './services/taskService'
import type { Task, TaskInput, TaskStatus } from './types/task'
import './App.css'

function App() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [formOpen, setFormOpen] = useState(false)
  const [editingTask, setEditingTask] = useState<Task | null>(null)

  const refreshTasks = useCallback(async () => {
    const nextTasks = await getTasks()
    setTasks(nextTasks)
  }, [])

  useEffect(() => {
    let cancelled = false

    async function load() {
      try {
        const nextTasks = await getTasks()
        if (!cancelled) {
          setTasks(nextTasks)
          setError('')
        }
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : 'Failed to load tasks.')
        }
      } finally {
        if (!cancelled) {
          setLoading(false)
        }
      }
    }

    void load()
    return () => {
      cancelled = true
    }
  }, [])

  function openCreateForm() {
    setEditingTask(null)
    setFormOpen(true)
  }

  function openEditForm(task: Task) {
    setEditingTask(task)
    setFormOpen(true)
  }

  function closeForm() {
    setFormOpen(false)
    setEditingTask(null)
  }

  async function handleSave(input: TaskInput) {
    if (editingTask) {
      await updateTask(editingTask.id, input)
    } else {
      await createTask(input)
    }
    await refreshTasks()
    closeForm()
  }

  async function handleDelete(task: Task) {
    const confirmed = window.confirm(`Delete task "${task.title}"?`)
    if (!confirmed) {
      return
    }

    try {
      await deleteTask(task.id)
      await refreshTasks()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete task.')
    }
  }

  async function handleMove(task: Task, status: TaskStatus) {
    try {
      await moveTask(task.id, status)
      await refreshTasks()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to move task.')
    }
  }

  return (
    <div className="app">
      <header className="app__header">
        <div>
          <p className="app__eyebrow">Mini Kanban Board</p>
          <h1 className="app__title">Flux</h1>
          <p className="app__subtitle">
            Track tasks across TODO, IN PROGRESS, and DONE.
          </p>
        </div>
        <button type="button" className="btn" onClick={openCreateForm}>
          New task
        </button>
      </header>

      {error ? <p className="app__error">{error}</p> : null}

      {loading ? (
        <p className="app__status">Loading board…</p>
      ) : (
        <Board
          tasks={tasks}
          onEdit={openEditForm}
          onDelete={handleDelete}
          onMove={handleMove}
        />
      )}

      {formOpen ? (
        <TaskForm
          initialTask={editingTask}
          onSubmit={handleSave}
          onCancel={closeForm}
        />
      ) : null}
    </div>
  )
}

export default App
