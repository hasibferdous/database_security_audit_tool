CREATE DATABASE SecurityAuditDB;

USE SecurityAuditDB;

CREATE TABLE
    Users (
        Username NVARCHAR (50) NOT NULL,
        Password NVARCHAR (50) NOT NULL,
        Role NVARCHAR (50) NOT NULL
    );

-- Sample data
INSERT INTO
    Users (Username, Password, Role)
VALUES
    ('admin', 'Admin@123', 'Admin'),
    ('auditor', 'Audit123!', 'Auditor'),
    ('user1', '1234', 'User'),
    ('user2', 'WeakPass', 'User');

SELECT *FROM Users;


-- Truncate Users table (removes all data without logging individual row deletions)
TRUNCATE TABLE Users;


-- Drop Users table (removes the table structure and data permanently)
DROP TABLE Users;