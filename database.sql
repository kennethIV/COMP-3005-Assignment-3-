-- Create the students table using the assignment's schema.
-- Run this script within your chosen PostgreSQL database in pgAdmin.
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

-- Add the three initial student records without duplicating them
-- if the script is run again.
INSERT INTO students (first_name, last_name, email, enrollment_date)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
ON CONFLICT (email) DO NOTHING;

-- View the current records.
SELECT * FROM students ORDER BY student_id;
