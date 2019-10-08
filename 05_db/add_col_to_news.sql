-- ALTER TABLE news 
-- ADD COLUMN created_at DATETIME NOT NULL;  -- 기존에 있던 데이터는 추가된 컬럼의 데이터가 없기 때문에 에러가 발생한다.

ALTER TABLE news 
ADD COLUMN created_at DATETIME NOT NULL DEFAULT 1;

