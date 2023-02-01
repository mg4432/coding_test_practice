SELECT A.animal_id, A.name
FROM animal_ins A
    JOIN animal_outs B ON A.animal_id = B.animal_id
WHERE A.datetime > B.datetime
ORDER BY A.datetime
;