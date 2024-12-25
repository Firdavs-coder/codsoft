import tkinter as tk
from tkinter import messagebox
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks[selected_task[0]]["completed"] = True
        update_task_list()
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "[✓]" if task["completed"] else "[ ]"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

complete_button = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

update_task_list()

root.mainloop()
