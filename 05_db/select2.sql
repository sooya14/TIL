-- SELECT DISTINCT age FROM users;  -- 중복없이 나온다. 

-- SELECT * FROM users WHERE age=30;
-- SELECT * FROM users WHERE age >= 30;

-- SELECT first_name FROM users WHERE age >= 30;

-- -- users 에서 age 가 30이상, 성이 '김' 인 사람의 성과 나이만 가져온다면?
-- SELECT age, last_Name FROM users
-- WHERE age >= 30 AND last_Name= '김'
-- LIMIT 10;

-- COUNT
-- SELECT COUNT(*) FROM users; -- 카운트 안에 컬럼명이 넣는 것이 좋다. 

-- AVG, SUM, MIN, MAX (숫자 컬럼만 가능)
-- 30살 이상인 사람들의 평균 나이 
-- SELECT AVG(age) from users
-- where age >= 30;

-- users 에서 잔액이 가장 높은 사람과 잔액 
-- SELECT first_name, MAX(balance) from users;

-- users 에서 30살 이상인 사람의 계좌 평균 잔액은?
-- SELECT AVG(balance) FROM users
-- WHERE age >= 30;

-- wild cards
-- SELECT * FROM users WHERE age LIKE '2_';

-- users 에서 지역번호가 02 인 사람만
-- SELECT * FROM users WHERE phone LIKE '02-%';

-- 이름이 준 으로 끝나는 사람만
-- SELECT first_name FROM users WHERE first_name LIKE '%준';

-- 중간 번호가 5114 인 사람만
-- SELECT phone FROM users WHERE phone LIKE '%-5114-%';

--ODER

-- 나이순으로 오름차순 상위 10개
-- SELECT age, first_name FROM users
-- ORDER BY age ASC LIMIT 10;
-- 고령 10명
-- SELECT age, first_name FROM users
-- ORDER BY age DESC LIMIT 10;

-- SELECT age, last_name FROM users 
-- ORDER BY last_name, age LIMIT 10;  -- order by 에 무엇이 먼저 오냐에 따라 우선순위가 달라진다. (먼저 적힌 것이 우선순위)

-- SELECT age, balance FROM users 
-- ORDER BY age, balance LIMIT 10;  -- balance 가 text 로 입력값이 설정되어있기 때문에 

-- 계좌 잔액 순으로 내림차순해서 사람 성과 이름 10개만만 
SELECT first_name, balance FROM users 
ORDER BY balance DESC LIMIT 10;