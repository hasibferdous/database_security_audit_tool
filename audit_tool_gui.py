import tkinter as tk
from tkinter import messagebox
from database_audit import audit_users
from audit_analysis import analyze_results

def run_audit():
    try:
        results = audit_users()
        report = analyze_results(results)
        report_text.delete("1.0", tk.END)  # Clear previous content
        for line in report:
            report_text.insert(tk.END, line + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run audit: {e}")

# Create the main GUI
root = tk.Tk()
root.title("Database Security Audit Tool")

# Add a button to run the audit
audit_button = tk.Button(root, text="Run Audit", command=run_audit)
audit_button.pack(pady=10)

# Add a text widget to display the report
report_text = tk.Text(root, width=80, height=20)
report_text.pack(padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()
