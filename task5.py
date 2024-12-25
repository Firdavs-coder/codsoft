import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    if not name:
        messagebox.showwarning("Input Error", "Name is required!")
        return

    phone = simpledialog.askstring("Add Contact", "Enter phone number:")
    if not phone:
        messagebox.showwarning("Input Error", "Phone number is required!")
        return

    email = simpledialog.askstring("Add Contact", "Enter email:")
    address = simpledialog.askstring("Add Contact", "Enter address:")

    if name in contacts:
        messagebox.showwarning("Duplicate Entry", f"Contact with name '{name}' already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        update_contact_list()
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    if not query:
        messagebox.showwarning("Input Error", "Search query is required!")
        return

    results = [
        f"{name} - {details['phone']}"
        for name, details in contacts.items()
        if query.lower() in name.lower() or query in details["phone"]
    ]

    if results:
        messagebox.showinfo("Search Results", "\n".join(results))
    else:
        messagebox.showinfo("Search Results", "No contacts found!")

def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
    if name not in contacts:
        messagebox.showerror("Error", f"No contact found with name '{name}'!")
        return

    phone = simpledialog.askstring("Update Contact", f"Enter new phone number (current: {contacts[name]['phone']}):")
    email = simpledialog.askstring("Update Contact", f"Enter new email (current: {contacts[name]['email']}):")
    address = simpledialog.askstring("Update Contact", f"Enter new address (current: {contacts[name]['address']}):")

    contacts[name] = {"phone": phone or contacts[name]["phone"],
                      "email": email or contacts[name]["email"],
                      "address": address or contacts[name]["address"]}
    update_contact_list()
    messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")

def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
    if name in contacts:
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{name}'?")
        if confirm:
            del contacts[name]
            update_contact_list()
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
    else:
        messagebox.showerror("Error", f"No contact found with name '{name}'!")

def view_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact from the list!")
        return

    name = contact_list.get(selected).split(" - ")[0]
    details = contacts[name]
    messagebox.showinfo("Contact Details",
                        f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")

root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x500")

title_label = tk.Label(root, text="Contact Manager", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

contact_list = tk.Listbox(root, font=("Arial", 12), height=15, width=50)
contact_list.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", font=("Arial", 12), command=add_contact)
add_button.grid(row=0, column=0, padx=5)

view_button = tk.Button(button_frame, text="View Contact", font=("Arial", 12), command=view_contact)
view_button.grid(row=0, column=1, padx=5)

search_button = tk.Button(button_frame, text="Search Contact", font=("Arial", 12), command=search_contact)
search_button.grid(row=1, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Contact", font=("Arial", 12), command=update_contact)
update_button.grid(row=1, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Contact", font=("Arial", 12), command=delete_contact)
delete_button.grid(row=2, column=0, padx=5, pady=5)

quit_button = tk.Button(button_frame, text="Quit", font=("Arial", 12), command=root.destroy)
quit_button.grid(row=2, column=1, padx=5, pady=5)

update_contact_list()

root.mainloop()
