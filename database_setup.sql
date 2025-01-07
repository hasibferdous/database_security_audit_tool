CREATE DATABASE SecurityAuditDB;

USE SecurityAuditDB;

CREATE TABLE Users (
    Username NVARCHAR(50) NOT NULL,
    Password NVARCHAR(50) NOT NULL,
    Role NVARCHAR(50) NOT NULL
);

-- Sample data
INSERT INTO Users (Username, Password, Role)
VALUES
('admin', 'Admin@123', 'Admin'),
('auditor', 'Audit123!', 'Auditor'),
('user1', '1234', 'User'),
('user2', 'WeakPass', 'User');
