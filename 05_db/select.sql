-- SELECT name, age FROM classmates;
-- SELECT id FROM classmates;

-- SELECT * FROM classmates;

-- LIMIT & OFFSET
-- SELECT * FROM classmates LIMIT 2;  -- 앞에서 두개만
-- SELECT * FROM classmates LIMIT 1 OFFSET 2;  -- 앞에 두개 띄고 한개만 

-- WHERE
-- SELECT * FROM classmates WHERE name='최솔지';
-- SELECT * FROM classmates WHERE address='광명';  -- 만약 광명이 2개이면 2개다 가져온다. 
-- SELECT * FROM classmates WHERE name='광명' LIMIT 1;  -- 대전이 여러개면 그 중에 하나만 가져온다. 
-- 어떤 DB인지에 따라 순서가 다르다. 그래서 일단 지금 순서에 따라서 가세요~ 

--DISTINCT
SELECT DISTINCT age FROM classmates;

