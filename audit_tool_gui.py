import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from audit_analysis import analyze_audit, export_to_pdf, export_to_csv
from database_audit import audit_users

# Create GUI
def create_gui():
    root = tk.Tk()
    root.title("Database Security Audit Tool")
    root.geometry("1300x600")
    root.configure(bg="#00ffff")

    # Function to generate audit and display results
    def generate_audit():
        audit_results = audit_users()  # Fetch audit results
        analysis = analyze_audit(audit_results)

        # Clear existing table content
        for row in tree.get_children():
            tree.delete(row)

        # Insert data into the Treeview (table)
        for record in analysis:
            tree.insert("", "end", values=(
                record["Username"], 
                record["Role"], 
                record["Password Status"], 
                "".join(record["Privileges"]), 
                record["Suggestions"]
            ))

        messagebox.showinfo("Audit Completed", "Audit results generated successfully!")

    # Export to PDF
    def export_pdf():
        audit_results = audit_users()
        analysis = analyze_audit(audit_results)
        export_to_pdf(analysis)
        messagebox.showinfo("Export Successful", "Audit report exported to PDF!")

    # Export to CSV
    def export_csv():
        audit_results = audit_users()
        analysis = analyze_audit(audit_results)
        export_to_csv(analysis)
        messagebox.showinfo("Export Successful", "Audit report exported to CSV!")

    # View logs
    def view_logs():
        if not os.path.exists("logs/activity_log.txt"):
            messagebox.showerror("Error", "No log file found.")
            return
        with open("logs/activity_log.txt", "r") as log_file:
            logs = log_file.read()
        log_window = tk.Toplevel(root)
        log_window.title("Activity Logs")
        log_window.geometry("500x300")
        log_text = tk.Text(log_window, wrap="word")
        log_text.insert(1.0, logs)
        log_text.pack(expand=True, fill=tk.BOTH)

    # Download log file
    def download_logs():
        if not os.path.exists("logs/activity_log.txt"):
            messagebox.showerror("Error", "No log file found.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open("logs/activity_log.txt", "r") as log_file:
                with open(file_path, "w") as out_file:
                    out_file.write(log_file.read())
            messagebox.showinfo("Download Successful", f"Log file downloaded to {file_path}")

    # GUI Layout
    tk.Label(root, text="Database Security Audit Tool", bg="#f0f8ff", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Generate Audit", command=generate_audit, bg="#4caf50", fg="white").pack(pady=5)
    tk.Button(root, text="Export to PDF", command=export_pdf, bg="#2196f3", fg="white").pack(pady=5)
    tk.Button(root, text="Export to CSV", command=export_csv, bg="#ff9800", fg="white").pack(pady=5)
    tk.Button(root, text="View Logs", command=view_logs, bg="#9c27b0", fg="white").pack(pady=5)
    tk.Button(root, text="Download Logs", command=download_logs, bg="#f44336", fg="white").pack(pady=5)

    # Table (Treeview) for displaying audit results
    columns = ("Username", "Role", "Password Status", "Privileges", "Suggestions")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
    tree.heading("Username", text="Username")
    tree.heading("Role", text="Role")
    tree.heading("Password Status", text="Password Status")
    tree.heading("Privileges", text="Privileges")
    tree.heading("Suggestions", text="Suggestions")
    tree.column("Username", width=100, anchor="center")
    tree.column("Role", width=50, anchor="center")
    tree.column("Password Status", width=70, anchor="center")
    tree.column("Privileges", width=180, anchor="center")
    tree.column("Suggestions", width=560, anchor="center")
    tree.pack(pady=10, fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == "__main__":
    create_gui()