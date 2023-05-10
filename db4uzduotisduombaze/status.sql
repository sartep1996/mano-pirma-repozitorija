CREATE TABLE status(
id integer PRIMARY KEY,
name VARCHAR(50),
FOREIGN KEY (id) REFERENCES ordeder (status_id)
)