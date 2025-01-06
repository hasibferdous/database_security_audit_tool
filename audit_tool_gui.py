import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from database_audit import audit_users, check_role_privileges
from audit_logs import log_audit_event
from export_report import export_to_csv, export_to_pdf

def run_audit():
    results = audit_users()
    display_results(results)
    log_audit_event("Audit run completed.")

def display_results(results):
    for row in tree.get_children():
        tree.delete(row)
    for result in results:
        tree.insert("", "end", values=(result[0], result[1], result[2], "; ".join(result[3])))

def export_results():
    results = audit_users()
    file_type = file_type_var.get()
    if file_type == "CSV":
        file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_name:
            export_to_csv(results, file_name)
            messagebox.showinfo("Export", "Results exported to CSV successfully!")
    elif file_type == "PDF":
        file_name = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_name:
            export_to_pdf(results, file_name)
            messagebox.showinfo("Export", "Results exported to PDF successfully!")

# GUI Setup
root = tk.Tk()
root.title("Database Security Audit Tool")
root.geometry("1000x1000")

# Styles
style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 10))
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

# Treeview
columns = ("Username", "Role", "Password Policy", "Suggestions")
tree = ttk.Treeview(root, columns=columns, show="headings", height=20)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=200)
tree.pack(pady=20)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

run_button = tk.Button(frame, text="Run Audit", command=run_audit, bg="blue", fg="white", font=("Helvetica", 12))
run_button.grid(row=0, column=0, padx=10)

export_button = tk.Button(frame, text="Export Results", command=export_results, bg="green", fg="white", font=("Helvetica", 12))
export_button.grid(row=0, column=1, padx=10)

file_type_var = tk.StringVar(value="CSV")
file_type_menu = ttk.OptionMenu(frame, file_type_var, "CSV", "CSV", "PDF")
file_type_menu.grid(row=0, column=2, padx=10)

root.mainloop()
