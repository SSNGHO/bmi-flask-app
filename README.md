# BMI 계산기 (Flask)

키와 몸무게를 입력하면 BMI(체질량지수)와 비만도 분류를 계산해주는 간단한 Flask 웹 애플리케이션입니다.

## 기능

- 키(cm), 몸무게(kg) 입력 폼
- BMI 계산: `체중(kg) / 키(m)^2`
- 결과 분류: 저체중 / 정상 / 과체중 / 비만
- 잘못된 입력(숫자가 아닌 값, 0 이하 값)에 대한 오류 메시지 표시

## 설치 및 실행

```bash
pip install -r requirements.txt
python app.py
```

서버가 실행되면 브라우저에서 아래 주소로 접속합니다.

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
├── app.py              # Flask 앱 (라우트, BMI 계산/분류 로직)
├── templates/
│   └── index.html      # 입력 폼 및 결과 화면
├── test_app.py          # 단위 테스트
├── requirements.txt
└── .gitignore
```

## BMI 분류 기준

| BMI 범위 | 분류 |
|---|---|
| 18.5 미만 | 저체중 |
| 18.5 ~ 22.9 | 정상 |
| 23 ~ 24.9 | 과체중 |
| 25 이상 | 비만 |
