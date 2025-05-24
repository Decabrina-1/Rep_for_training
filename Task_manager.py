# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline, task_id):
        self.description = description
        self.deadline = deadline
        self.task_id = task_id
        self.status = 'Не взято в работу'  # Начальный статус

class TaskManager:
    def __init__(self):
        self.tasks = []
        self._current_id = 0

    def add_task(self, description, deadline):
        """Добавляет новую задачу и возвращает её ID."""
        self._current_id += 1
        new_task = Task(description, deadline, self._current_id)
        self.tasks.append(new_task)
        return self._current_id

    def start_task(self, task_id):
        """Меняет статус задачи на 'Взято в работу'."""
        for task in self.tasks:
            if task.task_id == task_id:
                if task.status == 'Не взято в работу':
                    task.status = 'Взято в работу'
                    return True
                else:
                    print(f"Ошибка: Задача {task_id} уже взята в работу или выполнена.")
                    return False
        return False

    def mark_as_done(self, task_id):
        """Меняет статус задачи на 'Выполнено'."""
        for task in self.tasks:
            if task.task_id == task_id:
                if task.status == 'Взято в работу':
                    task.status = 'Выполнено'
                    return True
                else:
                    print(f"Ошибка: Задача {task_id} не может быть выполнена в текущем статусе.")
                    return False
        return False

    def list_current_tasks(self):
        """Выводит список незавершённых задач."""
        current_tasks = []
        for task in self.tasks:
            if task.status != 'Выполнено':
                current_tasks.append(
                    f"ID: {task.task_id}, Описание: {task.description}, Срок: {task.deadline}, Статус: {task.status}"
                )
        return '\n'.join(current_tasks) if current_tasks else "Нет текущих задач"



manager = TaskManager()

# Добавляем задачи
task1_id = manager.add_task("Покормить кота", "2023-10-30")
task2_id = manager.add_task("Сделать ДЗ", "2023-11-01")

# Попробуем изменить статусы
manager.start_task(task1_id)       # Статус задачи 1: "Взято в работу"
manager.mark_as_done(task1_id)     # Статус задачи 1: "Выполнено"

# Попробуем сделать ошибку (например, завершить задачу без начала)
manager.mark_as_done(task2_id)     # Выведет ошибку

# Выводим текущие задачи
print(manager.list_current_tasks())