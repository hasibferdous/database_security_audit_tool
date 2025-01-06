import pyodbc
from password_policy import check_password_policy

def connect_to_database():
    connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-HP873LD\SQLEXPRESS;"  # Replace with your SQL Server name
        "Database=SecurityAuditDB;"
        "Trusted_Connection=yes;"
    )
    return connection

def audit_users():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Username, Password, Role FROM Users")
    results = cursor.fetchall()
    conn.close()

    audited_results = []
    for row in results:
        username, password, role = row
        password_policy, suggestions = check_password_policy(password)
        audited_results.append((username, role, password_policy, suggestions))
    return audited_results

def check_role_privileges(role):
    """
    Check privileges for the specified role.
    """
    privileges = {
        "Admin": ["Full Access", "Manage Users", "Database Config"],
        "Auditor": ["View Logs", "Audit Data"],
        "User": ["Limited Access"]
    }
    return privileges.get(role, ["No privileges assigned."])
