-- 1️⃣ Create the database
CREATE DATABASE IF NOT EXISTS alx_book_store;

-- 2️⃣ Use the database
USE alx_book_store;
 -- TABLE: AUTHORS
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- TABLE: BOOKS
CREATE TABLE IF NOT EXISTS Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- TABLE: CUSTOMERS
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) UNIQUE NOT NULL,
    address TEXT
);


-- TABLE: ORDERS
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- TABLE: ORDER_DETAILS
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Insert authors
INSERT INTO Authors (author_name) VALUES 
('J.K. Rowling'),
('George R.R. Martin'),
('Chinua Achebe');

-- Insert books
INSERT INTO Books (title, author_id, price, publication_date) VALUES
('Harry Potter and the Sorcerer''s Stone', 1, 19.99, '1997-06-26'),
('A Game of Thrones', 2, 24.99, '1996-08-06'),
('Things Fall Apart', 3, 14.99, '1958-01-01');

-- Insert customers
INSERT INTO Customers (customer_name, email, address) VALUES
('Alice Johnson', 'alice@example.com', '123 Main St, Nairobi'),
('Brian Otieno', 'brian@example.com', '456 Park Ave, Kisumu');

-- Insert orders
INSERT INTO Orders (customer_id, order_date) VALUES
(1, '2025-10-17'),
(2, '2025-10-17');

-- Insert order details
INSERT INTO Order_Details (order_id, book_id, quantity) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 2, 1);