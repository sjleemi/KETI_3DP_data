import os
from dotenv import load_dotenv
from minio import Minio

# .env 파일에서 환경변수 로드
load_dotenv()

# 환경변수에서 접속 정보 불러오기
MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET = os.getenv("MINIO_BUCKET")

# MinIO 클라이언트 생성
client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

def get_image_urls(layer_num: int):
    first_key = f"{layer_num} Layer_FirstShot.jpg"
    second_key = f"{layer_num} Layer_SecondShot.jpg"

    first_url = client.presigned_get_object(MINIO_BUCKET, first_key)
    second_url = client.presigned_get_object(MINIO_BUCKET, second_key)

    return first_url, second_url


print("[DEBUG] MINIO_ENDPOINT:", MINIO_ENDPOINT)
