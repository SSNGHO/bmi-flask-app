# 테트리스 (Flask)

Flask로 정적 페이지를 서빙하고, 캔버스(Canvas)와 순수 JavaScript로 구현한 테트리스 게임입니다.

## 기능

- 표준 7종 테트로미노 (I, J, L, O, S, T, Z)
- 좌우 이동, 회전(간단한 벽차기 포함), 소프트 드롭, 하드 드롭
- 점수 / 레벨 / 지운 줄 수 표시, 레벨에 따라 낙하 속도 증가
- 다음 블록 미리보기
- 게임 오버 후 다시 시작

## 조작법

| 키 | 동작 |
|---|---|
| ← / → | 좌우 이동 |
| ↑ | 회전 |
| ↓ | 소프트 드롭 |
| Space | 하드 드롭 |
| P | 일시정지 |

## 설치 및 실행

```bash
pip install -r requirements.txt
python app.py
```

브라우저에서 접속:

```
http://127.0.0.1:5000
```

## 테스트

```bash
python -m unittest test_app.py -v
```

## 파일 구조

```
bmi_flask_app/
├── app.py              # Flask 앱 (정적 페이지 서빙)
├── templates/
│   └── index.html      # 테트리스 게임 (Canvas + JS)
├── test_app.py          # 단위 테스트
├── requirements.txt
├── vercel.json          # Vercel 배포 설정
└── .gitignore
```
