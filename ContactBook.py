import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        # Name Label and Entry
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Phone Label and Entry
        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        # Add Button
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Contacts Listbox with Scrollbar
        self.contacts_frame = tk.Frame(master)
        self.contacts_frame.grid(row=3, column=0, columnspan=2, pady=5)
        self.contacts_listbox = tk.Listbox(self.contacts_frame, width=50, height=15)
        self.contacts_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.contacts_frame, orient=tk.VERTICAL, command=self.contacts_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.contacts_listbox.config(yscrollcommand=self.scrollbar.set)

        self.contacts = {}

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            if name not in self.contacts:
                self.contacts[name] = phone
                self.contacts_listbox.insert(tk.END, f"{name} - {phone}")
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Contact already exists.")
        else:
            messagebox.showerror("Error", "Name and phone cannot be empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()