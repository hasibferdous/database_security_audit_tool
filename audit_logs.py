import csv
from datetime import datetime
import os

# Define the log file path
LOG_FILE_PATH = "audit_logs.csv"

def log_event(event_description):
    """
    Logs an event into the audit_logs.csv file with a timestamp.

    Parameters:
    event_description (str): A description of the event to be logged.
    """
    # Ensure the file exists, create it if not
    file_exists = os.path.exists(LOG_FILE_PATH)

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write the event to the CSV file
    with open(LOG_FILE_PATH, mode="a", newline="", encoding="utf-8") as log_file:
        writer = csv.writer(log_file)
        
        # If the file is newly created, write the header
        if not file_exists:
            writer.writerow(["Timestamp", "Event Description"])
        
        # Write the log entry
        writer.writerow([timestamp, event_description])

    print(f"Event logged: {event_description}")

# Example usage
if __name__ == "__main__":
    log_event("Audit process started.")
    log_event("User 'admin' generated an audit report.")
    log_event("Audit completed successfully.")
    log_event("Exported audit report to PDF.")