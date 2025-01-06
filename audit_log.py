from datetime import datetime

def log_audit(event):
    """
    Logs audit events to a file.
    """
    with open("audit_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {event}\n")
