Task 


Grade D Python coding exercise
Coding Exercise: Flight Data Processor
Objective
 Implement a robust Python class that processes flight data and demonstrates clean coding practices while incorporating unit testing.

Task Description
You are given a list of flight data in JSON format. Each flight entry consists of several details. Your goal is to implement a FlightDataProcessor class with advanced features that include handling data transformations and deriving insights from the data.
    1. Attributes:
        ◦ flights: A list of dictionaries, where each dictionary represents a flight with the following keys: 
            ▪ flight_number (string)
            ▪ departure_time (string in "YYYY-MM-DD HH:MM" format)
            ▪ arrival_time (string in "YYYY-MM-DD HH:MM" format)
            ▪ duration_minutes (integer)
            ▪ status (enum, e.g. "ON_TIME", "DELAYED", "CANCELLED")
    2. Methods:
        ◦ add_flight(data: dict) -> None: Adds a new flight to the list, ensuring no duplicates (by flight number).
        ◦ remove_flight(flight_number: str) -> None: Removes a flight based on the flight number.
        ◦ flights_by_status(status: str) -> List[dict]: Returns all flights with a given status.
        ◦ get_longest_flight() -> dict: Returns the flight with the longest duration in minutes.

Requirements
    • Implement the class with clean coding practices.
    • Use Python's type hinting feature across all methods and method arguments.

Unit Testing Requirements
    • Use the unittest library to write comprehensive tests for all methods, covering a range of inputs and scenarios.
    • Ensure the tests validate the correctness, performance, and stability of each method in the FlightDataProcessor class.

Example Data
flight_data = [
    {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"},
    {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "status": "DELAYED"},
]

Bonus Challenge
    • Implement a method, update_flight_status(flight_number: str, new_status: str) -> None, that updates the status of a flight and ensure it reflects in the overall data.

Instructions for Submission
    1. Implement the FlightDataProcessor class in a script named flight_data_processor.py.
    2. Write unit tests in a separate script test_flight_data_processor.py.
    3. Ensure tests run and pass without errors.
    4. Submit both scripts for review. If you are conducting this test in an interview, demonstrate your code to your interviewer. If you are conducting this exercise prior to interview, please push it to your personal GitHub account and give the repo URL to your recruiter.
