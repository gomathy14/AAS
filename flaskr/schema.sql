
DROP TABLE IF EXISTS income;
DROP TABLE IF EXISTS payment;



CREATE TABLE income (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Block TEXT NOT NULL,
    UnitNo INTEGER NOT NULL,
    MaintenanceFee INTEGER NOT NULL,
    Due INTEGER NOT NULL
);

CREATE TABLE Payment(

	id INTEGER PRIMARY KEY AUTOINCREMENT,
	income_id INTEGER NOT NULL,
	amount INTEGER NOT NULL,
	Pdate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (income_id) REFERENCES income(id)
   
);
