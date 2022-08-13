import unittest
import json
from unittest import TestCase
from unittest.mock import patch, mock_open

from main import BMI


class TestMain(unittest.TestCase):
    def test_fetch_data_from_file(self):
        result = BMI.fetch_data_from_file("input.txt")
        self.assertEqual(6, len(result))

    def test_bmi_calculator(self):
        result = BMI.bmi_calculator(96, 1.71)
        self.assertEqual(32.83, round(result, 2))

    def test_count_overweight(self):
        output_array= [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96, "bmi_category": "Moderately obese", "bmi_range": "30 - 34.9", "health_risk": "Medium risk"},
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85, "bmi_category": "Moderately obese", "bmi_range": "30 - 34.9", "health_risk": "Medium risk"},
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77, "bmi_category": "Normal weight", "bmi_range": "18.5 - 24.9", "health_risk": "Low risk"},
            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62, "bmi_category": "Normal weight", "bmi_range": "18.5 - 24.9", "health_risk": "Low risk"},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70, "bmi_category": "Moderately obese", "bmi_range": "30 - 34.9", "health_risk": "Medium risk"},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82, "bmi_category": "Overweight", "bmi_range": "25 - 29.9", "health_risk": "Enhanced risk"}
        ]
        result = BMI.countOverweight(output_array)
        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()
