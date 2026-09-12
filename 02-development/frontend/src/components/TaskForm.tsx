import { useState, type FormEvent } from 'react'
import type { Task, TaskInput, TaskStatus } from '../types/task'
import { STATUS_LABELS, TASK_STATUSES } from '../types/task'

type TaskFormProps = {
  initialTask?: Task | null
  onSubmit: (input: TaskInput) => Promise<void>
  onCancel: () => void
}

export function TaskForm({ initialTask, onSubmit, onCancel }: TaskFormProps) {
  const isEditing = Boolean(initialTask)
  const [title, setTitle] = useState(initialTask?.title ?? '')
  const [description, setDescription] = useState(initialTask?.description ?? '')
  const [status, setStatus] = useState<TaskStatus>(initialTask?.status ?? 'TODO')
  const [error, setError] = useState('')
  const [saving, setSaving] = useState(false)

  async function handleSubmit(event: FormEvent) {
    event.preventDefault()
    const trimmedTitle = title.trim()
    if (!trimmedTitle) {
      setError('Title is required.')
      return
    }

    setError('')
    setSaving(true)
    try {
      await onSubmit({
        title: trimmedTitle,
        description: description.trim(),
        status,
      })
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Could not save task.')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="modal-backdrop" role="presentation" onClick={onCancel}>
      <form
        className="modal"
        role="dialog"
        aria-modal="true"
        aria-labelledby="task-form-title"
        onClick={(event) => event.stopPropagation()}
        onSubmit={handleSubmit}
      >
        <h2 id="task-form-title">{isEditing ? 'Edit task' : 'Create task'}</h2>

        <label className="field">
          <span>Title</span>
          <input
            type="text"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
            placeholder="Task title"
            autoFocus
            required
          />
        </label>

        <label className="field">
          <span>Description</span>
          <textarea
            value={description}
            onChange={(event) => setDescription(event.target.value)}
            placeholder="Optional description"
            rows={4}
          />
        </label>

        <label className="field">
          <span>Status</span>
          <select
            value={status}
            onChange={(event) => setStatus(event.target.value as TaskStatus)}
          >
            {TASK_STATUSES.map((value) => (
              <option key={value} value={value}>
                {STATUS_LABELS[value]}
              </option>
            ))}
          </select>
        </label>

        {error ? <p className="form-error">{error}</p> : null}

        <div className="modal__actions">
          <button type="button" className="btn btn--secondary" onClick={onCancel}>
            Cancel
          </button>
          <button type="submit" className="btn" disabled={saving}>
            {saving ? 'Saving…' : isEditing ? 'Save changes' : 'Create task'}
          </button>
        </div>
      </form>
    </div>
  )
}
