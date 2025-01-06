from datetime import datetime
import csv

def log_audit_event(event):
    """
    Logs an audit event with a timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("audit_logs.csv", "a", newline="") as log_file:
        writer = csv.writer(log_file)
        writer.writerow([timestamp, event])
