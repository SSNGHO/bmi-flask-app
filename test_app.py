import unittest

from app import app, calculate_bmi, classify_bmi


class BmiLogicTests(unittest.TestCase):
    def test_calculate_bmi(self):
        # 키 170cm, 몸무게 65kg -> BMI 22.49
        self.assertEqual(calculate_bmi(170, 65), 22.49)

    def test_calculate_bmi_normal_case(self):
        # 키 180cm, 몸무게 75kg -> BMI 23.15
        self.assertEqual(calculate_bmi(180, 75), 23.15)

    def test_classify_underweight(self):
        self.assertEqual(classify_bmi(17.0), "저체중")

    def test_classify_normal(self):
        self.assertEqual(classify_bmi(20.0), "정상")

    def test_classify_overweight(self):
        self.assertEqual(classify_bmi(24.0), "과체중")

    def test_classify_obese(self):
        self.assertEqual(classify_bmi(30.0), "비만")


class BmiRouteTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("BMI 계산기".encode("utf-8"), response.data)

    def test_post_valid_data(self):
        response = self.client.post("/", data={"height": "170", "weight": "65"})
        self.assertEqual(response.status_code, 200)
        html = response.data.decode("utf-8")
        self.assertIn("22.49", html)
        self.assertIn("정상", html)

    def test_post_invalid_data(self):
        response = self.client.post("/", data={"height": "abc", "weight": "65"})
        self.assertEqual(response.status_code, 200)
        html = response.data.decode("utf-8")
        self.assertIn("올바른 숫자로 입력해주세요", html)

    def test_post_negative_values(self):
        response = self.client.post("/", data={"height": "-170", "weight": "65"})
        self.assertEqual(response.status_code, 200)
        html = response.data.decode("utf-8")
        self.assertIn("0보다 큰 값을 입력해주세요", html)


if __name__ == "__main__":
    unittest.main()
