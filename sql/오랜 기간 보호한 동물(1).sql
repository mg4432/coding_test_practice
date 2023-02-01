SELECT A.name, A.datetime
FROM animal_ins A
    LEFT JOIN animal_outs B ON A.animal_id = B.animal_id
WHERE B.animal_id is null
ORDER BY A.datetime
LIMIT 3;