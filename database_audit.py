import pyodbc
from password_policy import check_password_policy
from audit_log import log_audit

# Connect to SQL Server
def connect_to_database():
    connection = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-HP873LD\SQLEXPRESS;"  # Replace with your SQL Server name
        "Database=SecurityAuditDB;"
        "Trusted_Connection=yes;"
    )
    return connection

# Function to audit users
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
        log_audit(f"Audited user: {username}, Role: {role}, Password Policy: {password_policy}")
    return audited_results
