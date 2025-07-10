class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = {'id': self.next_id, 'description': description, 'completed': False}
        self.tasks.append(task)
        self.next_id += 1
        return task['id']

    def _find_task_index_by_id(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                return i
        return -1

    def mark_complete(self, task_id):
        index = self._find_task_index_by_id(task_id)
        if index != -1:
            self.tasks[index]['completed'] = True
            return True
        return False

    def delete_task(self, task_id):
        index = self._find_task_index_by_id(task_id)
        if index != -1:
            del self.tasks[index]
            return True
        return False

    def view_tasks(self):
        formatted_tasks = []
        for task in self.tasks:
            status = "[X]" if task['completed'] else "[ ]"
            formatted_tasks.append(f"{task['id']}. {status} {task['description']}")
        return formatted_tasks

if __name__ == "__main__":
    todo_list = TodoList()

    print("Current tasks:")
    if not todo_list.view_tasks():
        print("No tasks.")
    for task_str in todo_list.view_tasks():
        print(task_str)

    task1_id = todo_list.add_task("Buy groceries")
    task2_id = todo_list.add_task("Finish project report")
    task3_id = todo_list.add_task("Call mom")

    print("\nAfter adding 3 tasks:")
    for task_str in todo_list.view_tasks():
        print(task_str)

    todo_list.mark_complete(task1_id)
    print(f"\nAfter marking task ID {task1_id} complete:")
    for task_str in todo_list.view_tasks():
        print(task_str)

    task4_id = todo_list.add_task("Go for a run")
    print("\nAfter adding another task:")
    for task_str in todo_list.view_tasks():
        print(task_str)

    todo_list.delete_task(task2_id)
    print(f"\nAfter deleting task ID {task2_id}:")
    for task_str in todo_list.view_tasks():
        print(task_str)

    todo_list.mark_complete(99)
    print("\nAfter attempting to mark non-existent task ID 99 complete:")
    for task_str in todo_list.view_tasks():
        print(task_str)

    todo_list.delete_task(100)
    print("\nAfter attempting to delete non-existent task ID 100:")
    for task_str in todo_list.view_tasks():
        print(task_str)

    todo_list.delete_task(task1_id)
    todo_list.delete_task(task3_id)
    todo_list.delete_task(task4_id)

    print("\nAfter deleting all remaining tasks:")
    if not todo_list.view_tasks():
        print("No tasks.")
    for task_str in todo_list.view_tasks():
        print(task_str)