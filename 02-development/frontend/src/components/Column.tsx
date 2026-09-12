import type { Task, TaskStatus } from '../types/task'
import { STATUS_LABELS } from '../types/task'
import { TaskCard } from './TaskCard'

type ColumnProps = {
  status: TaskStatus
  tasks: Task[]
  onEdit: (task: Task) => void
  onDelete: (task: Task) => void
  onMove: (task: Task, status: TaskStatus) => void
}

export function Column({ status, tasks, onEdit, onDelete, onMove }: ColumnProps) {
  return (
    <section className="column" aria-labelledby={`column-${status}`}>
      <header className="column__header">
        <h2 id={`column-${status}`} className="column__title">
          {STATUS_LABELS[status]}
        </h2>
        <span className="column__count">{tasks.length}</span>
      </header>

      <div className="column__tasks">
        {tasks.length === 0 ? (
          <p className="column__empty">No tasks</p>
        ) : (
          tasks.map((task) => (
            <TaskCard
              key={task.id}
              task={task}
              onEdit={onEdit}
              onDelete={onDelete}
              onMove={onMove}
            />
          ))
        )}
      </div>
    </section>
  )
}
