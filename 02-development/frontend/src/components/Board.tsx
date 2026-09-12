import type { Task, TaskStatus } from '../types/task'
import { COLUMN_ORDER } from '../types/task'
import { Column } from './Column'

type BoardProps = {
  tasks: Task[]
  onEdit: (task: Task) => void
  onDelete: (task: Task) => void
  onMove: (task: Task, status: TaskStatus) => void
}

export function Board({ tasks, onEdit, onDelete, onMove }: BoardProps) {
  return (
    <div className="board">
      {COLUMN_ORDER.map((status) => (
        <Column
          key={status}
          status={status}
          tasks={tasks.filter((task) => task.status === status)}
          onEdit={onEdit}
          onDelete={onDelete}
          onMove={onMove}
        />
      ))}
    </div>
  )
}
