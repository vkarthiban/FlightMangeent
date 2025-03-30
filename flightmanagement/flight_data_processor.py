
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime
class FlightStatus(Enum):
    ON_TIME = "ON_TIME"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"


class FlightDataProcessor:
    
    def __init__(self, flights):
        ''' sample data   flight_data = [
            {"flight_number": "AZ001", "departure_time": "2025-02-19 15:30", "arrival_time": "2025-02-20 03:45", "status": "ON_TIME"},
            {"flight_number": "AZ002", "departure_time": "2025-02-21 11:00", "arrival_time": "2025-02-21 16:00", "status": "DELAYED"},
            ]'''        
        self.flight_data = flights if flights else  []
        
    def add_flight(self, data: dict) -> None: 
        '''Adds a new flight to the list, ensuring no duplicates (by flight number).'''
        if not any(fdata['flight_number'] == data['flight_number'] for fdata in self.flight_data):
            self.flight_data.append(data)
        
    def remove_flight(self, flight_number: str) -> None: 
        '''Removes a flight based on the flight number.'''
        for elm in self.flight_data:
            if elm['flight_number'] == flight_number:
                self.flight_data.remove(elm)
                
    def flights_by_status(self, status: str) -> List[dict]: 
        '''Returns all flights with a given status.'''
        return [fdata for fdata in self.flight_data if fdata['status'] == status]
    
    def get_longest_flight(self) -> dict: 
        '''Returns the flight with the longest duration in minutes.'''
        return max(self.flight_data, key=lambda x: (datetime.strptime(x['arrival_time'], '%Y-%m-%d %H:%M') - datetime.strptime(x['departure_time'], '%Y-%m-%d %H:%M')).total_seconds() / 60)
    
    def update_flight_status(self, flight_number: str, new_status: str) -> None:
        '''that updates the status of a flight and ensure it reflects in the overall data.'''
        for fdata in self.flight_data:
            if fdata['flight_number'] == flight_number:
                fdata['status'] = new_status
