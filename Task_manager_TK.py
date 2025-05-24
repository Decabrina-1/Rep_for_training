import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, deadline, task_id):
        self.description = description
        self.deadline = deadline
        self.task_id = task_id
        self.status = 'Не выполнено'

class TaskManager:
    def __init__(self):
        self.tasks = []
        self._current_id = 0

    def add_task(self, description, deadline):
        self._current_id += 1
        new_task = Task(description, deadline, self._current_id)
        self.tasks.append(new_task)
        return self._current_id

    def mark_as_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                if task.status == 'Не выполнено':
                    task.status = 'Выполнено'
                    return True
                else:
                    return False
        return False

    def list_current_tasks(self):
        filtered_tasks = []  # Пустой список для отфильтрованных задач
        for task in self.tasks:  # Перебираем все задачи
            if task.status != 'Выполнено':  # Если задача не выполнена
                filtered_tasks.append(task)  # Добавляем её в список
        return filtered_tasks  # Возвращаем фильтрованный список

class TaskApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Менеджер задач")
        self.manager = TaskManager()
        self.selected_task_id = None

        # Устанавливаем окно в левый верхний угол
        self.geometry("+0+0")  # "+X+Y" - координаты от левого верхнего угла экрана

        self.create_widgets()

    def create_widgets(self):
        top_frame = tk.Frame(self)
        top_frame.pack(pady=10, anchor=tk.W)  # anchor=tk.W для выравнивания по левому краю

        tk.Label(top_frame, text="Описание:").grid(row=0, column=0, sticky=tk.W)
        self.entry_desc = tk.Entry(top_frame, width=30)
        self.entry_desc.grid(row=0, column=1, padx=5, sticky=tk.W)

        tk.Label(top_frame, text="Срок:").grid(row=1, column=0, sticky=tk.W)
        self.entry_deadline = tk.Entry(top_frame, width=30)
        self.entry_deadline.grid(row=1, column=1, padx=5, sticky=tk.W)

        add_btn = tk.Button(top_frame, text="Добавить задачу", command=self.add_task)
        add_btn.grid(row=2, columnspan=2, pady=10, sticky=tk.W)

        list_frame = tk.Frame(self)
        list_frame.pack(pady=10, anchor=tk.W)

        self.listbox = tk.Listbox(list_frame, width=60, height=10)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, anchor=tk.W)
        self.listbox.bind('<<ListboxSelect>>', self.on_task_select)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10, anchor=tk.W)

        done_btn = tk.Button(btn_frame, text="Отметить как выполненную", command=self.mark_as_done)
        done_btn.pack(side=tk.LEFT, padx=5, anchor=tk.W)

        self.update_task_list()

    def add_task(self):
        desc = self.entry_desc.get().strip()
        deadline = self.entry_deadline.get().strip()

        if not desc:
            messagebox.showerror("Ошибка", "Введите описание задачи!")
            return

        self.manager.add_task(desc, deadline)
        self.entry_desc.delete(0, tk.END)
        self.entry_deadline.delete(0, tk.END)
        self.update_task_list()

    def update_task_list(self):
        self.listbox.delete(0, tk.END)
        tasks = self.manager.list_current_tasks()

        for task in tasks:
            self.listbox.insert(tk.END, f"ID: {task.task_id} | {task.description} | Срок: {task.deadline}")

    def on_task_select(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            task_str = self.listbox.get(selected_index)
            self.selected_task_id = int(task_str.split('ID: ')[1].split(' | ')[0])

    def mark_as_done(self):
        if not self.selected_task_id:
            messagebox.showerror("Ошибка", "Сначала выберите задачу!")
            return

        success = self.manager.mark_as_done(self.selected_task_id)
        if success:
            self.update_task_list()
            self.selected_task_id = None
        else:
            messagebox.showerror("Ошибка", "Задача уже выполнена!")

if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()