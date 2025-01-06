def check_privileges():
    conn = connect_to_database()
    cursor = conn.cursor()

    # Query for roles and privileges
    cursor.execute("""
        SELECT DP1.name AS UserName, 
               DP2.name AS RoleName
        FROM sys.database_role_members AS DRM
        INNER JOIN sys.database_principals AS DP1
        ON DRM.member_principal_id = DP1.principal_id
        INNER JOIN sys.database_principals AS DP2
        ON DRM.role_principal_id = DP2.principal_id
    """)
    privileges = cursor.fetchall()
    conn.close()
    return privileges
