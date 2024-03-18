-- create tables
CREATE TABLE students (
  id INTEGER UNIQUE,
  name TEXT NOT NULL,
  gender TEXT NOT NULL
);

CREATE TABLE customers (
    id INTEGER UNIQUE,
    name TEXT NOT NULL,
    meal TEXT
);

-- insert values into tables (order matters)
INSERT INTO students VALUES (1, 'Frank', 'M');
INSERT INTO students VALUES (2, 'Selina', 'F');
INSERT INTO students VALUES (3, 'Max', 'M');

INSERT INTO customers VALUES (1, 'Frank', 'Fish');
INSERT INTO customers VALUES (4, 'Dylan', 'Green salad');
INSERT INTO customers VALUES (2, 'Selina', 'Ice coffee');
INSERT INTO customers VALUES (5, 'Bwalya', 'Nshima');

-- select all rows from the customers table
-- SELECT * FROM customers;

SELECT * FROM students INNER JOIN customers ON students.id = customers.id;
