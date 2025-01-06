import pyodbc
from password_policy import check_password_policy

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
    cursor.execute("SELECT Username, Role, Password FROM Users")
    results = cursor.fetchall()
    conn.close()
 
 
     # Add password policy checking
    audited_results = []
    for row in results:
        username, password, role = row
        password_policy = check_password_policy(password)
        audited_results.append((username, role, password_policy))
    return audited_results
