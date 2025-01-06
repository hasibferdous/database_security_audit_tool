-- Create a sample database
CREATE DATABASE SecurityAuditDB;

-- Switch to the database
USE SecurityAuditDB;

-- Create a table to simulate user accounts
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    Password NVARCHAR(255) NOT NULL,
    Role NVARCHAR(50),
);

-- Insert sample data
INSERT INTO Users (Username, Password, Role)
VALUES
('admin2', 'hashed_password1', 'Admin'),
('user2', 'hashed_password2', 'User'),
('auditor1', 'hashed_password3', 'Auditor');


--To query
SELECT * FROM Users;