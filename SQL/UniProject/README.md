This is code for a university project.

This was the question:

In this question, you will create a full database schema for a pharmaceutical company. 


The following sections describe the full schema and components of the required database.
A pharmaceutical company includes full information about its employees.
 This covers the employee number, last name, first name, extension, email address, 
 office code, job title, and the other employee in which he/she reports to 
 (Hint: multiple employees can only report to one employee, however one/several employees cannot report
 to multiple employees at the same time). The company also stores information about their pharmaceutical
 retail customers, which covers the customer number, customer full name (last name and first name), 
 phone number, address line 1, address line 2, city, county, postal code, country, sales amount, 
 representative employee number (in which they deal with directly), and the credit limit number of that customer.


 Furthermore, the pharmaceutical company database stores information about the drugs they produce and prescription orders. 
 This covers the order number, order date, required date, shipped date, order status, comments, and the pharmaceutical 
 customer number that relates to this order.
In addition, information about the individual drugs should cover the product code, product name, product line, scale-weight,
vendor, description, quantity in stock, the buying price, and the MSRP (manufacturer's suggested retail price). 
In relation to the employees information mentioned previously, the employees are assigned to offices within the
pharmaceutical company, and this information includes the office code, City, phone number, address line 1, 
address line 2, county, country, postal code, and territory. 

In addition, with regards to the pharmaceutical retail customers, the payments information are stored in 
correspondence to each customer. This includes the customer number, cheque number, payment date, and the 
amount paid by each customer. The mutual information between the drugs/products and the orders include the
order number, product code, quantity ordered, price, and the order line number. 

Finally, this database stores the information about pharmaceutical product lines, which includes the product line text, 
description, website, and the product image. A product line can include multiple products, however, one product cannot
belong to more than one product line. 

Furthermore, an order can include many products, and a product could also be related to multiple orders. 
In addition, one retail customer can make multiple payments, however, one payment can only be related to
one customer at a given time. Several employees within the pharmaceutical company can report to one employee only, 
and they cannot report to multiple employees at once. One office can have more than one employee, yet one employee 
should not be assigned to more than one office.



Write SQL DDL commands to create the previous database schema. Make sure to represent your exact ER diagram from the previous task, and achieve the relationships, data types, and the correct attributes for the corresponding entities. You must also make sure that the order of your SQL commands is correct to ensure data integrity.
