CREATE TABLE order_(
    id integer PRIMARY KEY,
    customer_id INTEGER,
    date VARCHAR (50),
    status_id VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customer (id)
);
