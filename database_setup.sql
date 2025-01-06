CREATE DATABASE SecurityAuditDB;

USE SecurityAuditDB;

CREATE TABLE Users (
    UserID INT IDENTITY PRIMARY KEY,
    Username NVARCHAR(50) NOT NULL,
    Password NVARCHAR(255) NOT NULL, -- Encrypted passwords
    Role NVARCHAR(50) NOT NULL
);

INSERT INTO Users (Username, Password, Role) 
VALUES 
('admin', 'P@ssw0rd!', 'Admin'), 
('user1', 'weakpass', 'User'), 
('auditor', 'Str0ng@123', 'Auditor');

SELECT *from Users;
