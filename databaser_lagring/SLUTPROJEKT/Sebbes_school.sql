/*
Det här skriptet skapar en liten grund för en skoldatabas. Några antagen
har gjorts som till exempel, en evel kommer inte kunna gå samma kurs två
gånger. 

Jag valde att göra databsen baserad på att skolan är engelsktalande.

Detta är kurser jag vill ha,
1. Mathematics
2. Physics
3. Gymnastics
4. English
5. Computer Science
6. History

Det finns två stycken stored procedures. 
1. Show_Teachers Som ej visar lön

2. What_Teachers_And_Courses Som ett elev förnamn som inparameter


!!!!!
    Det här skriptet är testat mot en linux-container med SQL server i. Det bör
    fungera jättebra att köra det i windows. Man kan behöva ändra filepath för
    databas filen då den är anpassad för linux filepath.
!!!!!



Skriptfilen skapar grunderna i skoldatabasen i följande ordning.

1. Databas skapas om det inte redan finns
2. Tabeller skapas
3. Foreign keys skapas
4. Primär nycklar skapas
5. Indexeringar skapas
6. Vyer skapas
7. Procedurer skapas
8. Lägger in lärare
9. Lägger in kurser
10. Lägger studenter <------ GÖRS MED BULK IMPORT. SE TILL ATT HA PATH TILL CSV
11. Fördelar studenter till kurser

Lite mer om vad som händer i varje steg finns förklarat längre ned.
=============================================================================
FÖRKLARINGAR VAD SOM HÄNDER VID VARJE STEG
==============================================================================
1.  DATABASEN
Den kör först ett if statement för att kolla om det finns en databas redan med
det namn man angett. Om den inte finns så kör den igång och skapar databasen
samt går vidare skapar tabller.

!!!!
Att tänka på, är att under filepath används linux filstruktur. Det här 
databasskriptet är gjort till en linux-docker container där SQL server körs.
Det bör ändras om man använder windows.

==============================================================================
2. TABELLER 
Följande tabeller blir skapade 
 - Teachers
 - Courses
 - Students
 - Student_Courses

==============================================================================
3. Efter det skapas primär nycklarna till respektive tabell.
Kolla i min draw.io fil för att se förhållanderna
mellan nycklarna.

==============================================================================
4. Sist skapas alla foreign keys förehållandena. Förhållandena ses bäst på 
mitt ER diagram. Jag har gjort en egen tabell som länkar kurser och studenter.
Detta för att att en elev enkelt ska kunna delta i de kurser han vill.

==============================================================================
5. INDEXERING
tre st index finns.

1. Första är index på studenternas förnamn och efternamn
2. Andra indexet är på Student_Courses tabllen. Den behövs för att en elev
    endast ska kunna gå 1 kurs. Jag kör en Unique index där
3. Tredje index är på lärares förnamn och efternamn

==============================================================================
6. VYER
Jag har en vy som jag skapat för att kunna göra en bulk import till studenter
utan att behöva lägga in något StudentID i CSV filen.

Sedan har jag en till vy för att kunna visa allt i lärare UTOM löner.

==============================================================================
7. PROCEDURER
Två procedurer finns.

1. Show_Teachers <- som visar allt i min Vw_TeachersNoSalaries. 
2. What_Teacher_And_Course som tar in en namn parameter för att visa 
    vilka kurser och respektiva lärare som en student har. 

==============================================================================
*/

-- ----------------------------------- --
-- LÄGG TILL DATABAS OM DEN INTE FINNS --
-- ----------------------------------- --
USE master
GO

IF NOT EXISTS (
    SELECT [name]
    FROM sys.databases
    WHERE [name] = N'Sebbes_School' -- Namnet på databasen
)

CREATE DATABASE Sebbes_School
ON 
(
    NAME = Sebbes_School,
    FILENAME = N'C:\temp\Sebbes_school.mdf', -- WINDOWS PATH
    SIZE = 10GB, -- Sätt start storlek
    MAXSIZE = 600GB -- Liten skola
)
LOG ON 
(
    NAME = Sebbes_School_Log,
    FILENAME = N'C:\temp\Sebbe_school.ldf', -- WINDOWS PATH
    SIZE = 100MB,
    MAXSIZE = 2GB
)
GO

USE Sebbes_School
GO

-- --------------------- --
-- SKAPAR TABELLERNA     --
-- 1. Teachers           --
-- 2, Teacher_Salaries   --
-- 3. Courses            --
-- 4. Students           --
-- 5. Student_Courses    --
-- --------------------- --

-- Sätter primär och foreign keys längre ned
CREATE TABLE Teachers -- Lärartabell
(
    [TeacherID] INT IDENTITY(1,1) NOT NULL,
    [Firstname] VARCHAR(50) NOT NULL,
    [Lastname] VARCHAR(50) NOT NULL,
    [Email] VARCHAR(100) NOT NULL,
    [MobilePhoneNumber] VARCHAR(40),
    [Salary] SMALLMONEY NOT NULL  -- Ingen lärare kommer få mer än 922,337,203,685,477.58
)
GO

CREATE TABLE Courses -- Tabell över kurser
(
    [CourseID] INT IDENTITY(1,1) NOT NULL,
    [CourseName] VARCHAR(50) NOT NULL,
    [TeacherID] INT
)
GO

CREATE TABLE Students -- Elevtabell
(
    [StudentID] INT IDENTITY(1,1) NOT NULL,
    [Firstname] VARCHAR(50),
    [Lastname] VARCHAR(50),
    [Email] VARCHAR(100) NOT NULL,
    [MobilePhoneNumber] VARCHAR(40)
)
GO

CREATE TABLE Student_Courses -- Tabell över kurser och deltagare av kurserna
(
    [CourseID] INT NOT NULL,
    [StudentID] INT NOT NULL
)
GO

-- -------------------------- --
-- LÄGGER TILL PRIMÄR NYCKLAR --
-- -------------------------- --
ALTER TABLE Teachers 
    ADD CONSTRAINT Pk_Techers_TeacherID 
    PRIMARY KEY CLUSTERED
    (
        [TeacherID]
    )
GO

ALTER TABLE Students 
    ADD CONSTRAINT Pk_Students_StudentID 
    PRIMARY KEY CLUSTERED
    (
        [StudentID]
    )
GO

ALTER TABLE Courses
    ADD CONSTRAINT Pk_Courses_CourseID PRIMARY KEY 
    CLUSTERED
    (
        [CourseID]
    )
GO

-- ------------------------ --
-- LÄGGER TILL FOREIGN KEYS --
-- ------------------------ --
-- Lägg till foreign keys på Student_Courses tabellen
ALTER TABLE Student_Courses 
    ADD CONSTRAINT Fk_Student_Courses 
    FOREIGN KEY 
    (
        [StudentID]
    ) 
    REFERENCES Students 
    (
        [StudentID]
    ),
    CONSTRAINT Fk_Course_Students 
    FOREIGN KEY 
    (
        [CourseID]
    ) 
    REFERENCES Courses 
    (
        [CourseID]
    ), 
    UNIQUE (CourseID, StudentID) /* En elev ska inte kunna ta samma kurs två gånger
    -- Alternatuv hade varit att skapa en ny primärnyckel här som är kopplad till 
    -- tillexempel startdatum samt slutdatum för kurs. Då kan en elev gå om en kurs.
    -- Valde bort det i denna skola. One chance, or you're screwed */
GO

ALTER TABLE Courses
    ADD CONSTRAINT Fk_Course_Teacher 
    FOREIGN KEY 
    (
        [TeacherID]
    )
    REFERENCES Teachers 
    (
        [TeacherID]
    )
GO

/* 
Ifall jag ville ha en separat tabell med löner, för andra anställda också.
Då kan jag lätt utvidga genom att skapa ett employeeID utöver teacherID

ALTER TABLE Teacher_Salaries
    ADD CONSTRAINT Fk_Teacher_Salaries
    FOREIGN KEY 
    (
        [EmployeeID]
    )
    REFERENCES Teachers 
    (
        [TeacherID]
    )
GO
*/

-- ------------------------ --
-- LÄGGER TILL INDEXERINGAR --
-- ------------------------ --
CREATE NONCLUSTERED INDEX Idx_StudentNames -- För att snabbt kunna göra klasslistor
    ON Students(Lastname,Firstname)
GO

CREATE UNIQUE INDEX Idx_CourseStundents -- En elev kan bara ta en kurs.
    ON Student_Courses(CourseID, StudentID)
GO

CREATE INDEX Idx_TeachersNames
    ON Teachers(Lastname,Firstname)
GO

-- ---------------- --
-- LÄGGER TILL VYER --
-- ---------------- --
CREATE VIEW Vw_Students_No_ID -- Lägger in viewen för att kunna göra bulk insert
    AS
    SELECT Firstname, Lastname, Email, MobilePhoneNumber
    FROM Students
GO

CREATE VIEW Vw_Teachers_No_Salary
    AS
    SELECT Firstname, Lastname, Email, MobilePhoneNumber, TeacherID
    FROM Teachers
GO
-- ---------------------- --
-- LÄGGER TILL PROCEDURER --
-- ---------------------- --
CREATE PROCEDURE Show_Teachers
    AS
    SELECT *
    FROM Vw_Teachers_No_Salary
GO

CREATE PROCEDURE Which_Courses_And_Teachers @StudentName VARCHAR(100)
    AS
    SELECT S.Firstname, C.CourseName, T.Firstname + ' ' + T.Lastname AS TeacherFullName
    FROM Students AS S INNER JOIN Student_Courses AS SC 
    ON S.StudentID = SC.StudentID -- Hämta vilken kurs
    
    INNER JOIN Courses AS C 
    ON SC.CourseID = C.CourseID -- Hämta kursnamnet

    INNER JOIN Teachers AS T
    ON T.TeacherID = C.TeacherID -- Hämta vilken lärare
    
    WHERE S.Firstname = @StudentName
GO

-- ---------------- --
-- LÄGGER IN LÄRARE --
-- ---------------- --
INSERT INTO Teachers(Firstname, Lastname, Email, MobilePhoneNumber, Salary)
    VALUES
        ('Jeffery', 'Johnson', 'Jeff.Johnson@Sebbesschool.edu', '555-0214123',29500),
        ('Carin', 'Johansson', 'Carin.Johansson@Sebbesschool.edu', '0551-2321412',29000),
        ('John', 'Smith', 'John.Smith@Sebbesschool.edu', '2231-1231412',28000),
        ('Peter', 'Thomas', 'Peter.Thomas@Sebbesschool.edu', '624-341431',35000),
        ('Maria', 'Xin', 'Maria.Xin@Sebbesschool.edu', '341-425123',32000),
        ('Katheryn', 'Martell', 'Katheryn.Martell@Sebbesschool.edu', '554-4123425',32000)
GO

-- ---------------- --
-- LÄGGER IN KURSER -- 
-- ---------------- --
INSERT INTO Courses(CourseName, TeacherID)
    VALUES 
        ('Mathematics', 5), -- Lärare 5 ska vara lärare för kursen osv
        ('Phyics', 5),
        ('Gymnastics', 6),
        ('English', 1),
        ('Computer Science', 2),
        ('History', 3),
        ('Psychology', 4)
GO

-- ----------------------------------- --
-- LÄGGER IN STUDENTER MED BULK INSERT --
-- ----------------------------------- --
BULK INSERT Vw_Students_No_ID
    FROM 'C:\temp\Students.csv' -- LÄGG CSV FILEN DÄR FÖR KORREKT IMPORT
    WITH 
    ( 
        FORMAT = 'CSV',
        FIRSTROW = 2,
        ROWTERMINATOR = '0x0a'
    )
GO

-- ----------------------------- --
-- FÖRDELA STUDENTER TILL KURSER --
-- ----------------------------- --
INSERT INTO Student_Courses(StudentID, CourseID)
    VALUES
        ( 2, 1 ), ( 11, 1 ), ( 3, 1 ), ( 4, 1 ), -- Mathematic
        ( 5, 1 ), ( 6, 1 ), ( 7, 1 ), ( 8, 1 ),
        ( 9, 1 ), ( 10, 1 ),

        ( 1, 2 ), ( 2, 2 ), ( 3, 2 ), ( 5, 2 ), -- Phyics
        ( 9, 2 ), ( 12, 2 ), ( 13, 2 ), ( 14, 2 ),
        ( 19, 2 ), ( 90, 2 ), ( 22, 2 ), ( 23, 2 ),
        ( 18, 2 ), ( 33, 2 ), ( 7, 2 ), ( 31, 2 ),

        ( 40, 3 ), ( 41, 3 ), ( 42, 3 ), ( 1, 3 ), -- Gymnastics
        ( 49, 3 ), ( 48, 3 ), ( 37, 3 ), ( 12, 3 ), 
        ( 70, 3 ), ( 77, 3 ), ( 80, 3 ), ( 13, 3 ),
        ( 9, 3 ),
        
        ( 12, 4 ), ( 66, 4 ), ( 80, 4 ), ( 89, 4 ), -- English
        ( 99, 4 ), ( 98, 4 ), ( 27, 4 ), ( 97, 4 ), 
        ( 9, 4 ), ( 22, 4 ), ( 21, 4 ), ( 55, 4 ),
        ( 51, 4 ),

        ( 90, 5 ), ( 40, 5 ), ( 49, 5 ), ( 54, 5 ), -- Computer Science
        ( 19, 5 ), ( 12, 5 ), ( 61, 5 ), ( 62, 5 ), 
        ( 63, 5 ), ( 88, 5 ), ( 87, 5 ), ( 86, 5 ),
        ( 1, 5 ),

        ( 30, 6 ), ( 25, 6 ), ( 23, 6 ), ( 21, 6 ), -- History
        ( 24, 6 ), ( 28, 6 ), ( 39, 6 ), ( 22, 6 ), 
        ( 29, 6 ), ( 27, 6 ), ( 12, 6 ), ( 4, 6 ),
        ( 9, 6 )

-- Testing stored procedure
EXECUTE Show_Teachers
GO

EXECUTE Which_Courses_And_Teachers N'Allen'
GO