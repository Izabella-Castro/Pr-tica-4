import os
import unittest
from dataProcessor import avgAgeCountry, read_json_file

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Christopher Wells')
        self.assertEqual(data[1]['age'], 32)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

    def test_avgAgeCountry_no_data_for_country(self):
        with open("empty_data.json", "w") as file:
            file.write("[]")
        data = read_json_file("empty_data.json")
        avg_age_us = avgAgeCountry(data, "US")
        self.assertEqual(avg_age_us, 0)
    
    def test_avgAgeCountry_with_missing_age(self):
        data = [
            {"name": "John Doe", "country": "US"},
            {"name": "Jane Smith", "age": None, "country": "US"},
            {"name": "Bob Johnson", "age": None, "country": "US"}
        ]
        
        avg_age_us = avgAgeCountry(data, "US")
        self.assertEqual(avg_age_us, 0) 

    def test_avgAgeCountry_with_missing_country(self):
        data = [
            {"name": "John Doe", "age": 30},
            {"name": "Jane Smith", "age": 25, "country": None},
            {"name": "Bob Johnson", "age": 35, "country": None}
        ]
        
        avg_age = avgAgeCountry(data, "US")
        self.assertEqual(avg_age, 0)

    def test_avgAgeCountry_with_age_in_months(self):
        data = [
            {"name": "John Doe", "age": 30, "country": "US"},
            {"name": "Jane Smith", "age": 60, "country": "US"},
            {"name": "Bob Johnson", "age": 120, "country": "US"}
        ]

        def age_in_months(age):
            return age * 12

        avg_age_us_in_months = avgAgeCountry(data, "US", age_in_months)
        self.assertEqual(avg_age_us_in_months, (30 * 12 + 60 * 12 + 120 * 12) / 3)


if __name__ == '__main__':
    unittest.main()