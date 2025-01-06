from fpdf import FPDF
import csv

def export_to_pdf(data, filename="audit_report.pdf"):
    """
    Exports audit report to PDF.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Database Security Audit Report", ln=True, align="C")
    
    for row in data:
        pdf.cell(200, 10, txt=" | ".join(row), ln=True, align="L")
    
    pdf.output(filename)

def export_to_csv(data, filename="audit_report.csv"):
    """
    Exports audit report to CSV.
    """
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
