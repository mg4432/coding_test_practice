SELECT A.animal_id, A.animal_type, A.name 
FROM animal_ins A 
    JOIN animal_outs B ON A.animal_id = B.animal_id 
WHERE substring_index(A.sex_upon_intake, ' ', 1) NOT IN ('Spayed', 'Neutered') 
and substring_index(B.sex_upon_outcome, ' ', 1) IN ('Spayed', 'Neutered')
ORDER BY A.animal_id;