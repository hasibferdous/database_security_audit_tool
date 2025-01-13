import pyodbc
from password_policy import check_password_policy

# Connect to the database
def connect_to_database():
    connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-HP873LD\SQLEXPRESS;"  # Replace with your SQL Server name
        "Database=SecurityAuditDB;"
        "Trusted_Connection=yes;"
    )
    return connection

# Fetch all user data
def fetch_users():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Username, Password, Role FROM Users")
    results = cursor.fetchall()
    conn.close()
    return results

# Perform the audit
def audit_users():
    results = fetch_users()
    audited_results = []

    for row in results:
        username, password, role = row
        password_status, suggestions = check_password_policy(password)
        audited_results.append((username, role, password_status, suggestions))

    return audited_results

# Check privileges based on roles
def check_role_privileges(role):
    privileges = {
        "Admin": ["Full Access", "Create, Read, Update, Delete"],
        "Manager": ["Full Access", "Create, Read, Update, Delete"],
        "Developer": ["Full Access", "Create, Read, Update, Delete"],
        "Auditor": ["Read-Only Access", "Generate Reports"],
        "User": ["Read Access", "Limited Privileges"],
    }
    return privileges.get(role, ["No Privileges Assigned"])
