SELECT * FROM mokytojai WHERE specialybe = 'Matematika';

SELECT vardas, pavarde, specialybe FROM mokytojai
WHERE (2023 - patirtis_metais) > 8 OR (2023 - patirtis_metais) > 9;

UPDATE mokytojai Set pavarde = "Zoliene"  WHERE pavarde = "Rasaite"

DELETE FROM mokytojai WHERE id = 4;