import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

task_entry = tk.Entry(root)
task_entry.pack(pady=10)
task_list = tk.Listbox(root)
task_list.pack()
completed_listbox = tk.Listbox(root)
completed_listbox.pack()

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def complete_task():
    try:
        selected_task = task_list.curselection()[0]
        task = task_list.get(selected_task)
        task_list.delete(selected_task)
        completed_listbox.insert(tk.END, "✔ " + task)
    except IndexError:
        pass

def uncomplete_task():
    try:
        selected_task = completed_listbox.curselection()[0]
        task = completed_listbox.get(selected_task)
        completed_listbox.delete(selected_task)
        task_list.insert(tk.END, task[2:])
    except IndexError:
        pass

add_button = tk.Button(root, text="Add Task", command=add_task)
complete_button = tk.Button(root, text="Complete Task", command=complete_task)
uncomplete_button = tk.Button(root, text="Uncomplete Task", command=uncomplete_task)
add_button.pack()
complete_button.pack()
uncomplete_button.pack()

root.mainloop()
