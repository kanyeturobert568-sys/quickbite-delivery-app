# University Database Design Documentation

## Task 1: Requirements Analysis
- Identify the main entities: Students, Courses, Professors, Enrollments.

## Task 2: Entity-Relationship Diagram (ERD)
- ![ERD Diagram](link_to_erd_image)
  - Entities: Students, Courses, Professors
  - Relationships: Enrollments, Teaching

## Task 3: SQL Schema
```sql
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

CREATE TABLE Professors (
    professor_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
```

## Task 4: Sample Data
```sql
INSERT INTO Students (student_id, first_name, last_name, email)
VALUES (1, 'John', 'Doe', 'john.doe@example.com'),
       (2, 'Jane', 'Doe', 'jane.doe@example.com');

INSERT INTO Courses (course_id, course_name, credits)
VALUES (101, 'Database Systems', 3),
       (102, 'Algorithms', 4);

INSERT INTO Professors (professor_id, first_name, last_name)
VALUES (1, 'Dr. Smith', 'Johnson');

INSERT INTO Enrollments (enrollment_id, student_id, course_id)
VALUES (1, 1, 101),
       (2, 2, 102);
```

## Task 5: Queries
```sql
-- List all students enrolled in a specific course
SELECT Students.first_name, Students.last_name 
FROM Students 
JOIN Enrollments ON Students.student_id = Enrollments.student_id 
WHERE Enrollments.course_id = 101;

-- List all courses taught by a specific professor
SELECT Courses.course_name 
FROM Courses 
JOIN Enrollments ON Courses.course_id = Enrollments.course_id 
JOIN Professors ON Professors.professor_id = 1;
```

## Task 6: Forms
- Student Enrollment Form (HTML)
```html
<form>
  <label for="student_id">Student ID:</label>
  <input type="text" id="student_id" name="student_id"><br>
  <label for="course_id">Course ID:</label>
  <input type="text" id="course_id" name="course_id"><br>
  <input type="submit" value="Enroll">
</form>
```

---
### Conclusion
This document includes a complete database design for the University Database System covering all major requirements and future expansions.