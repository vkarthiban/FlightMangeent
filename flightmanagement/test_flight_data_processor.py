import unittest
from flight_data_processor import FlightDataProcessor, FlightStatus

class TestFlightDataProcessor(unittest.TestCase):
    
    def setUp(self):
        self.processor = FlightDataProcessor([
            {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "duration_minutes": 375, "status": "ON_TIME"},
            {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "duration_minutes": 300, "status": "DELAYED"},
        ])

    def test_add_flight(self):
        new_flight = {"flight_number": "AZ003", "departure_time": "2025-02-22 06:00", "arrival_time": "2025-02-22 10:00", "duration_minutes": 240, "status": "ON_TIME"}
        self.processor.add_flight(new_flight)
        self.assertIn(new_flight, self.processor.flight_data)

    def test_remove_flight(self):
        self.processor.remove_flight("AZ001")
        self.assertNotIn({"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "duration_minutes": 375, "status": "ON_TIME"}, self.processor.flight_data)

    def test_flights_by_status(self):
        on_time_flights = self.processor.flights_by_status("ON_TIME")
        self.assertEqual(len(on_time_flights), 1)
        self.assertEqual(on_time_flights[0]["flight_number"], "AZ001")

    def test_get_longest_flight(self):
        longest_flight = self.processor.get_longest_flight()
        self.assertEqual(longest_flight["flight_number"], "AZ001")
        self.assertEqual(longest_flight["duration_minutes"], 375)

    def test_update_flight_status(self):
        self.processor.update_flight_status("AZ002", "CANCELLED")
        cancelled_flights = self.processor.flights_by_status("CANCELLED")
        self.assertEqual(len(cancelled_flights), 1)
        self.assertEqual(cancelled_flights[0]["flight_number"], "AZ002")
        self.assertEqual(cancelled_flights[0]["status"], "CANCELLED")

    def test_add_duplicate_flight(self):
        duplicate_flight = {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "duration_minutes": 375, "status": "ON_TIME"}
        self.processor.add_flight(duplicate_flight)
        self.assertEqual(len(self.processor.flight_data), 2)  # Duplicate shouldn't add another entry.

if __name__ == '__main__':
    unittest.main()
