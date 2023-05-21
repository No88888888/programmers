-- 문제 설명
-- 다음은 중고거래 게시판 정보를 담은 USED_GOODS_BOARD 테이블과 중고거래 게시판 첨부파일 정보를 담은 USED_GOODS_REPLY 테이블입니다. USED_GOODS_BOARD 테이블은 다음과 같으며 BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

-- Column name	Type	Nullable
-- BOARD_ID	VARCHAR(5)	FALSE
-- WRITER_ID	VARCHAR(50)	FALSE
-- TITLE	VARCHAR(100)	FALSE
-- CONTENTS	VARCHAR(1000)	FALSE
-- PRICE	NUMBER	FALSE
-- CREATED_DATE	DATE	FALSE
-- STATUS	VARCHAR(10)	FALSE
-- VIEWS	NUMBER	FALSE
-- USED_GOODS_REPLY 테이블은 다음과 같으며 REPLY_ID, BOARD_ID, WRITER_ID, CONTENTS, CREATED_DATE는 각각 댓글 ID, 게시글 ID, 작성자 ID, 댓글 내용, 작성일을 의미합니다.

-- Column name	Type	Nullable
-- REPLY_ID	VARCHAR(10)	FALSE
-- BOARD_ID	VARCHAR(5)	FALSE
-- WRITER_ID	VARCHAR(50)	FALSE
-- CONTENTS	VARCHAR(1000)	TRUE
-- CREATED_DATE	DATE	FALSE
-- 문제
-- USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요. 결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.

-- 예시
-- USED_GOODS_BOARD 테이블이 다음과 같고

-- BOARD_ID	WRITER_ID	TITLE	CONTENTS	PRICE	CREATED_DATE	STATUS	VIEWS
-- B0001	kwag98	반려견 배변패드 팝니다	정말 저렴히 판매합니다. 전부 미개봉 새상품입니다.	12000	2022-10-01	DONE	250
-- B0002	lee871201	국내산 볶음참깨	직접 농사지은 참깨입니다.	3000	2022-10-02	DONE	121
-- B0003	goung12	배드민턴 라켓	사놓고 방치만 해서 팝니다.	9000	2022-10-02	SALE	212
-- B0004	keel1990	디올 귀걸이	신세계강남점에서 구입. 정품 아닐시 백퍼센트 환불	130000	2022-10-02	SALE	199
-- B0005	haphli01	스팸클래식 팔아요	유통기한 2025년까지에요	10000	2022-10-02	SALE	121
-- USED_GOODS_REPLY 테이블이 다음과 같을 때

-- REPLY_ID	BOARD_ID	WRITER_ID	CONTENTS	CREATED_DATE
-- R000000001	B0001	s2s2123	구매하겠습니다. 쪽지 드립니다.	2022-10-02
-- R000000002	B0002	hoho1112	쪽지 주세요.	2022-10-03
-- R000000003	B0006	hwahwa2	삽니다. 연락주세요.	2022-10-03
-- R000000004	B0007	hong02	예약중	2022-10-06
-- R000000005	B0009	hanju23	구매완료	2022-10-07
-- SQL을 실행하면 다음과 같이 출력되어야 합니다.

-- TITLE	BOARD_ID	REPLY_ID	WRITER_ID	CONTENTS	CREATED_DATE
-- 반려견 배변패드 팝니다	B0001	R000000001	s2s2123	구매하겠습니다. 쪽지 드립니다.	2022-10-02
-- 국내산 볶음참깨	B0002	R000000002	hoho1112	쪽지 주세요.	2022-10-03
-- 주의사항
-- CREATED_DATE의 포맷이 예시의 포맷과 일치해야 정답처리 됩니다.

-- SELECT
-- TITLE,
-- BOARD.BOARD_ID,
-- REPLY_ID,
-- REPLY.REPLY_ID,
-- REPLY.CONTENTS,
-- DATE_FORMAT(REPLY.CREATED_DATE, '%Y-%m-%d') AS CREATE_DATE
-- FROM USED_GOODS_BOARD AS BOARD
-- LEFT JOIN USED_GOODS_REPLY AS REPLY
-- ON BOARD.BOARD_ID = REPLY.BOARD_ID
-- WHERE REPLY.CREATE_DATE LIKE '2022-10-%'
-- ORDER BY REPLY.CREATE_DATE, TITLE



select ugb.title, 
ugb.board_id, 
ugr.reply_id, 
ugr.writer_id,
ugr.contents, 
date_format(ugr.created_date, '%Y-%m-%d')
from used_goods_board ugb
join used_goods_reply ugr
where ugb.created_date like '2022-10-%'
order by ugr.created_date, ugb.title;


SELECT 
TITLE,
BOARD.BOARD_ID, 
REPLY_ID, 
REPLY.WRITER_ID, 
REPLY.CONTENTS, 
DATE_FORMAT(REPLY.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_REPLY AS REPLY 
LEFT JOIN USED_GOODS_BOARD AS BOARD 
ON REPLY.BOARD_ID = BOARD.BOARD_ID
WHERE DATE_FORMAT(BOARD.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY REPLY.CREATED_DATE, TITLE