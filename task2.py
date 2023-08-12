import csv

class RainFallRecord:
    def __init__(self, year):
        self.year = year
        self.months = {}
 #Open the CSV file and extract the data for the given year
        with open('Oxford.csv') as f:
            reader = csv.reader(f)
            next(reader)
#Iterate through each row of the CSV file
            for row in reader:
#Check if the year in the current row matches the given year
                if int(row[0]) == year:
# Store the rainfall value for the corresponding month
                    self.months[int(row[1])] = float(row[5])
#Method to return the rainfall for a given month
    def rainfall(self, month):
        return self.months.get(month, 'Invalid Month')
#Method to delete the rainfall data for a given month    
    def delete(self, month):
        if month in self.months:
            del self.months[month]
#Method to insert a new rainfall value for a given month
    def insert(self, month, rainfall_value):
        self.months[month] = rainfall_value
#Method to insert rainfall values for a given quarter
    def insert_quarter(self, quarter, rainfall_values):
#Check the quarter and insert the corresponding rainfall values for each month in the quarter
        if quarter == 'winter':
            self.months[1] = rainfall_values[0]
            self.months[2] = rainfall_values[1]
            self.months[12] = rainfall_values[2]
        elif quarter == 'spring':
            self.months[3] = rainfall_values[0]
            self.months[4] = rainfall_values[1]
            self.months[5] = rainfall_values[2]
        elif quarter == 'summer':
            self.months[6] = rainfall_values[0]
            self.months[7] = rainfall_values[1]
            self.months[8] = rainfall_values[2]
        elif quarter == 'autumn':
            self.months[9] = rainfall_values[0]
            self.months[10] = rainfall_values[1]
            self.months[11] = rainfall_values[2]

#Testing the implementation
rf = RainFallRecord(1854)
print(rf.rainfall(1)) #Prints the rainfall data for January
rf.delete(1) #Deletes the rainfall data for January
print(rf.rainfall(1))  #Prints 'Invalid Month' as the data for January has been deleted
rf.insert(1, 10.5) #Inserts a new rainfall value of 10.5 for January
print(rf.rainfall(1)) 
rf.insert_quarter('winter', [1, 2, 3])
print(rf.rainfall(1))