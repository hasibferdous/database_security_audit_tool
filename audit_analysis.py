import csv

def export_audit_report(results, file_format="csv"):
    if file_format == "csv":
        with open("audit_report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Role", "Password Policy", "Suggestions"])
            for row in results:
                username, role, password_policy, suggestions = row
                writer.writerow([username, role, password_policy, ", ".join(suggestions)])
    elif file_format == "pdf":
        from fpdf import FPDF  # Install with `pip install fpdf`
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Database Audit Report", ln=True, align="C")
        for row in results:
            username, role, password_policy, suggestions = row
            pdf.cell(200, 10, txt=f"User: {username}, Role: {role}, Policy: {password_policy}", ln=True)
            pdf.cell(200, 10, txt=f"Suggestions: {', '.join(suggestions)}", ln=True)
        pdf.output("audit_report.pdf")
