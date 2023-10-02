from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from .views import diabetes_prediction_model
from django.test import TestCase
from .forms import checkdiabetesForm

class DiabetesPredictionTests(TestCase):
    def test_diabetes_prediction_model(self):
        f1, f2, f3, f4, f5, f6, f7, f8 = 1, 85, 66, 29, 0, 26.6, 0.351, 31
        prediction = diabetes_prediction_model(None, f1, f2, f3, f4, f5, f6, f7, f8)
        self.assertIn(int(prediction), [1,0])
    def test_index_view(self):
        url=reverse('index')
        response = self.client.post(url, {'Pregnancies': 1, 'Glucose': 85, 'BloodPressure': 66,
                                               'SkinThickness': 29, 'Insulin': 0, 'BMI': 26.6,
                                               'DiabetesPedigreeFunction': 0.351, 'age': 31})
        self.assertEqual(response.status_code, 200)

class IndexViewTest(TestCase):

    def test_index_view_get(self):
        response = self.client.get('') 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsInstance(response.context['form'], checkdiabetesForm)
        self.assertIsNone(response.context['predict'])

    def test_index_view_post_diabetes(self):
        data = {
            'Pregnancies': 3,
            'Glucose': 150,
            'BloodPressure': 76,
            'SkinThickness': 40,
            'Insulin': 0,
            'BMI': 33.5,
            'DiabetesPedigreeFunction': 0.25,
            'age': 28
        }
        response = self.client.post('', data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsInstance(response.context['form'], checkdiabetesForm)
    def test_index_view_post_no_diabetes(self):
        data = {
            'Pregnancies': 1,
            'Glucose': 85,
            'BloodPressure': 66,
            'SkinThickness': 29,
            'Insulin': 0,
            'BMI': 26.6,
            'DiabetesPedigreeFunction': 0.351,
            'age': 31
        }
        response = self.client.post('', data) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIsInstance(response.context['form'], checkdiabetesForm)





