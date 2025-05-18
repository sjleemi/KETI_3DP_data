import os
from dotenv import load_dotenv
import psycopg2
import psycopg2.extras

# 🔹 .env 파일에서 환경변수 불러오기
load_dotenv()

# 🔹 .env에서 PostgreSQL 정보 가져오기
DB_CONFIG = {
    "host": os.getenv("PG_HOST"),
    "port": int(os.getenv("PG_PORT")),
    "dbname": os.getenv("PG_DBNAME"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD")
}

# 🔹 레이어 키 기반 데이터 조회 함수
def get_data_by_layer(layer_num):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    layer_key = f"CurrentLayer{layer_num}/225"
    query = """
        SELECT * FROM build_process_log_v2
        WHERE TRIM("Layer") = %s
        ORDER BY "Time" ASC
    """
    cur.execute(query, (layer_key,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [dict(row) for row in rows]
