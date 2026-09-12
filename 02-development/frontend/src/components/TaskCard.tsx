import type { Task, TaskStatus } from '../types/task'
import { COLUMN_ORDER, STATUS_LABELS } from '../types/task'

type TaskCardProps = {
  task: Task
  onEdit: (task: Task) => void
  onDelete: (task: Task) => void
  onMove: (task: Task, status: TaskStatus) => void
}

export function TaskCard({ task, onEdit, onDelete, onMove }: TaskCardProps) {
  const moveTargets = COLUMN_ORDER.filter((status) => status !== task.status)

  return (
    <article className="task-card">
      <h3 className="task-card__title">{task.title}</h3>
      {task.description ? (
        <p className="task-card__description">{task.description}</p>
      ) : (
        <p className="task-card__description task-card__description--empty">
          No description
        </p>
      )}

      <div className="task-card__actions">
        <button type="button" className="btn btn--small" onClick={() => onEdit(task)}>
          Edit
        </button>
        <button
          type="button"
          className="btn btn--small btn--danger"
          onClick={() => onDelete(task)}
        >
          Delete
        </button>
      </div>

      <label className="task-card__move">
        <span>Move to</span>
        <select
          aria-label={`Move ${task.title}`}
          value=""
          onChange={(event) => {
            const nextStatus = event.target.value as TaskStatus
            if (nextStatus) {
              onMove(task, nextStatus)
            }
          }}
        >
          <option value="" disabled>
            Select column…
          </option>
          {moveTargets.map((status) => (
            <option key={status} value={status}>
              {STATUS_LABELS[status]}
            </option>
          ))}
        </select>
      </label>
    </article>
  )
}
