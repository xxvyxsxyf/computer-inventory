CREATE DATABASE IF NOT EXISTS computer_inventory;

USE computer_inventory;

CREATE TABLE IF NOT EXISTS computers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100) NOT NULL,
    serial_number VARCHAR(100) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    os VARCHAR(100),    
    location VARCHAR(100),
    status VARCHAR(50) NOT NULL
);
