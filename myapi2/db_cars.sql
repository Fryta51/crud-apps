create table car (
id int AUTO_INCREMENT PRIMARY KEY, 
manufacturer varchar(30) NOT NULL, 
modelName varchar(30) NOT NULL,
cc int NOT NULL, 
onRoadPrice int NOT NULL, 
seatingCapacity int NOT NULL, 
gearBox int NOT NULL, 
fuelType enum ('Petrol', 'Diesel') NOT NULL
);
