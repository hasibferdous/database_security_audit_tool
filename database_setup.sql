CREATE DATABASE SecurityAuditDB;

USE SecurityAuditDB;

CREATE TABLE
    users1 (
        Username NVARCHAR (50) NOT NULL,
        Password NVARCHAR (50) NOT NULL,
        Role NVARCHAR (50) NOT NULL
    );

-- Sample data
INSERT INTO Users (Username, Password, Role)  VALUES 
('user73421', '2e7hss', 'Developer'),
('user77821', 'ks45@dfghyjhss', 'Auditor'),
('user72121', 'Wesdfghyjhss', 'User'),
('user79121', 'lesdfghyjhss', 'Manager'),
('user72421', '$Wesdfghyjhs78s', 'Admin');


SELECT *FROM Users;


-- Truncate Users table (removes all data without logging individual row deletions)
TRUNCATE TABLE Users;


-- Drop Users table (removes the table structure and data permanently)
DROP TABLE Users;