import csv

class RainFallRecord:
    def __init__(self, city_file, months, year):
        self.city_file = city_file
        self.months = months
        self.year = year
        
        #Validate that the number of months entered is within the specified range
        if not (1 <= self.months <= 12):
            raise ValueError("Number of months must be between 1 and 12")
        
        #Validate that the year entered is within the specified range
        if not (1800 <= self.year <= 9999):
            raise ValueError("Year must be between 1800 and 9999")
        
        #Read the data from the CSV file and store it in the records list
        try:
            with open(city_file, 'r') as file:
                reader = csv.reader(file)
                self.records = [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        
        #Validate that the data in the CSV file has the correct number of columns
        for record in self.records:
            if len(record) != 7:
                raise ValueError("Data in the file is not in the correct format")
    
    def average_rainfall(self):
        #Calculate the sum of rainfall for the specified number of months and year
        rainfall_sum = 0
        count = 0
        for record in self.records:
            if int(record[0]) == self.year and record[2:2+self.months]:
                rainfall_sum += sum(map(float, record[2:2+self.months]))
                count += self.months
        
        #Returns the average rainfall
        if count == 0:
            raise ValueError("No data found for the specified year and number of months")
        else:
            return rainfall_sum / count

class Driver:
    @staticmethod
    def run_tests():
        #Test1
        record = RainFallRecord("Oxford.csv", 6, 1941)
        avg_rainfall = record.average_rainfall()
        print("Average rainfall:", avg_rainfall)
        
        #Test2
    try:
        record = RainFallRecord("invalid_city_data.csv", 5, 2020)
    except FileNotFoundError as error:
        print(error)
Driver.run_tests()