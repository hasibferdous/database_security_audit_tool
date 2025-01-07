import os
from datetime import datetime
from fpdf import FPDF
import csv
from database_audit import check_role_privileges

# Analyze audit results
def analyze_audit(audit_results):
    analysis = []
    for username, role, password_status, suggestions in audit_results:
        role_privileges = check_role_privileges(role)
        suggestion_text = "; ".join(suggestions) if suggestions else "None"
        analysis.append({
            "Username": username,
            "Role": role,
            "Password Status": password_status,
            "Privileges": ", ".join(role_privileges),
            "Suggestions": suggestion_text,
        })
    return analysis

# Write log file for users with timestamp
def write_log(username):
    if not os.path.exists("logs"):
        os.makedirs("logs")
    with open("logs/activity_log.txt", "a") as log_file:
        log_file.write(f"User: {username}, Logged In: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Export to PDF
def export_to_pdf(analysis):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 102, 204)

    pdf.cell(200, 10, txt="Database Security Audit Report", ln=True, align="C")

    for record in analysis:
        pdf.ln(10)
        for key, value in record.items():
            pdf.cell(0, 10, f"{key}: {value}", ln=True)
    
    if not os.path.exists("reports"):
        os.makedirs("reports")
    pdf.output("reports/report.pdf")

# Export to CSV
def export_to_csv(analysis):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open("reports/report.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=analysis[0].keys())
        writer.writeheader()
        writer.writerows(analysis)

