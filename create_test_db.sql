-- Step 1: Create a new database
CREATE DATABASE TestDB;

-- Step 2: Use the new database
USE TestDB;

-- Step 3: Create a sample table
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    Username NVARCHAR(50) NOT NULL,
    PasswordHash NVARCHAR(255) NOT NULL,
    Role NVARCHAR(50)
);

-- Step 4: Insert some test data
INSERT INTO Users (Username, PasswordHash, Role)
VALUES
('admin', HASHBYTES('SHA2_256', 'adminpassword'), 'Administrator'),
('user1', HASHBYTES('SHA2_256', 'user1password'), 'StandardUser');

-- Step 5: Create a new SQL Server login
CREATE LOGIN TestUser WITH PASSWORD = 'StrongPassword123!';

-- Step 6: Map the login to the database and assign roles
CREATE USER TestUser FOR LOGIN TestUser;
EXEC sp_addrolemember 'db_owner', 'TestUser';

--To query
SELECT * FROM Users;

-- Adding New Users
INSERT INTO Users (Username, PasswordHash, Role)
VALUES ('newuser', HASHBYTES('SHA2_256', 'newpassword'), 'StandardUser');


---Test the new user login
EXECUTE AS USER = 'TestUser';
SELECT * FROM Users;
REVERT;

