import csv
from fpdf import FPDF

def export_to_csv(audited_results, file_name):
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Username", "Role", "Password Policy", "Suggestions"])
        for result in audited_results:
            writer.writerow([result[0], result[1], result[2], "; ".join(result[3])])

def export_to_pdf(audited_results, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Database Security Audit Report", ln=True, align="C")
    pdf.ln(10)

    for result in audited_results:
        pdf.cell(200, 10, txt=f"Username: {result[0]}, Role: {result[1]}", ln=True)
        pdf.cell(200, 10, txt=f"Password Policy: {result[2]}", ln=True)
        pdf.multi_cell(200, 10, txt=f"Suggestions: {', '.join(result[3])}")
        pdf.ln(5)
    
    pdf.output(file_name)
