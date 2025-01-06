def export_report(report, filename="security_audit_report.txt"):
    with open(filename, "w") as file:
        for line in report:
            file.write(line + "\n")
    print(f"Report saved to {filename}")
