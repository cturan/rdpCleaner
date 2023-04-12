import winreg
import tkinter as tk
from tkinter import messagebox


class RDPManagerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.listbox.yview)
        self.scrollbar.grid(row=0, column=1, pady=10, sticky="ns")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.remove_button = tk.Button(self, text="Remove", command=self.remove_rdp_entry)
        self.remove_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.quit_button = tk.Button(self, text="Close", command=self.master.destroy)
        self.quit_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        self.update_rdp_entries()

    def update_rdp_entries(self):
        self.listbox.delete(0, tk.END)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Default', 0, winreg.KEY_ALL_ACCESS) as default_key:
            try:
                i = 0
                while True:
                    server_name, server_ip, _ = winreg.EnumValue(default_key, i)
                    self.listbox.insert(tk.END, f"{server_name} ({server_ip})")
                    i += 1
            except OSError:
                pass

    def remove_rdp_entry(self):
        try:
            selection = self.listbox.curselection()[0]
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Default', 0, winreg.KEY_ALL_ACCESS) as default_key:
                server_name, _, _ = winreg.EnumValue(default_key, selection)

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Default', 0, winreg.KEY_ALL_ACCESS) as default_key:
                winreg.DeleteValue(default_key, server_name)

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Servers', 0, winreg.KEY_ALL_ACCESS) as servers_key:
                try:
                    winreg.DeleteKey(servers_key, server_name)
                except OSError:
                    pass

            self.update_rdp_entries()
            messagebox.showinfo("Success", f"{server_name} removed successfully")
        except (ValueError, OSError, IndexError) as e:
            messagebox.showerror("Error", f"Error: {e}")


def main():
    root = tk.Tk()
    root.title("RDP Manager")
    root.geometry("400x300")
    app = RDPManagerGUI(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
