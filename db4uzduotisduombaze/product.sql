CREATE TABLE product (
    id integer PRIMARY KEY,
    name VARCHAR(50),
    price FLOAT,
    FOREIGN KEY (id) REFERENCES product_order(product_id)
    );