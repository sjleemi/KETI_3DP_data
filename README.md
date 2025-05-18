<!-- 3DP Layer info -->

3D printing 공정 데이터의 각 레이어에 대한 이미지와 센서 데이터를 시각화하여 확인할 수 있습니다. 
아래와 같은 과정을 통해 진행됩니다. 
Layer 번호 입력 → 해당 이미지 2장 + 센서값 그래프 + 테이블 출력 → Detail Information → MongoDB 기반 산소/온도 그래프 출력


Python , Flask, PostgreSQL (layer 시계열 데이터), MongoDB (산소/온도 센서 상세 데이터), MinIO (이미지), Chart.js (그래프 시각화)

> 파일 구조는 다음과 같습니다. 
project/
├── app.py
├── utils/
│   ├── data_parsing.py
│   ├── postgres_client.py
│   ├── mongo_client.py
│   ├── minio_client.py
├── templates/
│   ├── index.html
│   └── details.html
├── static/
│   ├── script.js
│   └── style.css
├── README.md
└── requirements.txt

