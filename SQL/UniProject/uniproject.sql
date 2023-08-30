#create schema ex3;
use ex3;
-- Create Office Table

CREATE TABLE OFFICE (
    `Office Code` INT,
    `Office City` VARCHAR(20),
    `Office Phone Number` VARCHAR(15),
    `Office Address Line 1` VARCHAR(50),
    `Office Address Line 2` VARCHAR(50),
    `County` VARCHAR(30),
    `Office Country` VARCHAR(50),
    `Office Postal Code` VARCHAR(10),
    `Office Territory` VARCHAR(50),
    CONSTRAINT pk_office PRIMARY KEY (`Office Code`)
);

-- Create Company Employee Table

CREATE TABLE COMPANYEMP (
    `Employee Number` INT,
    `Employee First Name` VARCHAR(40),
    `Employee Last Name` VARCHAR(40),
    `Employee Phone Extension` INT,
    `Employee Email Address` VARCHAR(50),
    `Office Code` INT,
    `Job Title` VARCHAR(40),
    `CEO Employee Number` INT,
    CONSTRAINT pk_employee PRIMARY KEY (`Employee Number`),
    CONSTRAINT fk_office_companyemp FOREIGN KEY (`Office Code`) REFERENCES OFFICE (`Office Code`),
    CONSTRAINT fk_ceo_employee FOREIGN KEY (`CEO Employee Number`) REFERENCES COMPANYEMP (`Employee Number`)
);

-- Create Customer Table

CREATE TABLE CUSTOMER (
    `Customer Number` INT,
    `Customer First Name` VARCHAR(40),
    `Customer Last Name` VARCHAR(40),
    `Customer City` VARCHAR(20),
    `Customer Phone Number` VARCHAR(15),
    `Customer Address Line 1` VARCHAR(50),
    `Customer Address Line 2` VARCHAR(50),
    `Customer County` VARCHAR(30),
    `Customer Country` VARCHAR(50),
    `Customer Postal Code` VARCHAR(10),
    `Rep Employee Number` INT,
    `Credit Limit Number` DECIMAL(10, 2),
    `Sales Amount` DECIMAL(10, 2),
    CONSTRAINT pk_customer PRIMARY KEY (`Customer Number`)
);

-- Create Product Info Table
CREATE TABLE PRODUCTINFO (
    `Product Code` INT,
    `Product Name` VARCHAR(30),
    `Product Line` VARCHAR(30),
    `Scale-Weight` VARCHAR(50),
    `Vendor` VARCHAR(40),
    `Description` VARCHAR(150),
    `Quantity` INT,
    `Price` DECIMAL(10, 2), 
    `The MSRP` DECIMAL(10, 2),
    CONSTRAINT pk_productinfo PRIMARY KEY (`Product Code`, `Product Line`)
);

-- Create Product Lines Table

CREATE TABLE PRODUCTLINES (
    `Product Line Text` VARCHAR(40),
    `Description` VARCHAR(200),
    `Website` VARCHAR(60),
    `Product Image` VARCHAR(200),
    CONSTRAINT pk_productlines PRIMARY KEY (`Product Line Text`)
);

-- Create Payment Info Table
CREATE TABLE PAYMENTINFO (
    `Customer Number` INT,
    `Cheque Number` INT,
    `Payment Date` DATE,
    `Amount paid by Customer` DECIMAL(10, 2), 
    CONSTRAINT pk_paymentinfo PRIMARY KEY (`Cheque Number`),
    CONSTRAINT fk_paymentinfo_customer FOREIGN KEY (`Customer Number`) REFERENCES CUSTOMER (`Customer Number`)
);

-- Create Ordered Product Table

CREATE TABLE ORDEREDPRODUCT (
    `Order Number` INT,
    `Order Date` DATE,
    `Required Date` DATE,
    `Shipped Date` DATE,
    `Comments` VARCHAR(40),
    `Product Code` INT,
    `Order Status` VARCHAR(40),
    `Customer Number` INT,
    `Quantity` INT,
    `Price` DECIMAL(10, 2),
    `Product Line` VARCHAR(40),
    CONSTRAINT pk_orderedproduct PRIMARY KEY (`Order Number`),
    CONSTRAINT fk_orderedproduct_product FOREIGN KEY (`Product Code`, `Product Line`) REFERENCES PRODUCTINFO (`Product Code`, `Product Line`),
    CONSTRAINT fk_orderedproduct_customer FOREIGN KEY (`Customer Number`) REFERENCES CUSTOMER (`Customer Number`)
);
