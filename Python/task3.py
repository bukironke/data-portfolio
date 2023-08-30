import csv

class Archive:
    def __init__(self):
        self.records = []
#Method to insert a record into the records list
    def insert(self, record):
        self.records.append(record)
#Method to delete a record from the records list
    def delete(self, record):
        self.records.remove(record)
#Method to calculate the moving average of rainfall data
    def sma(self, year_one, year_two, k):
        rainfall_sums = {}
        for record in self.records:
            if year_one <= record["year"] <= year_two:
                if record["year"] not in rainfall_sums:
                    rainfall_sums[record["year"]] = [0.0] * 12
                rainfall_sums[record["year"]][record["month"] - 1] += record["rainfall"]
#Dictionary to store the moving averages for each year
        moving_averages = {}
        for year, rainfall_sum in rainfall_sums.items():
            moving_averages[year] = []
            for i in range(12 - k + 1):
#Calculation for the moving average for the specified k-month period
                moving_averages[year].append(sum(rainfall_sum[i:i+k]) / k)

        return moving_averages

#Method to load data from the CSV file
    def load_records_from_csv(self, filename):
      with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = row["yyyy"]
            if year.isdigit():
               year = int(year)
            else:
               continue

            month = row["mm"]
            if month.isdigit():
               month = int(month)
            else:
               continue

            rainfall = row["rain"]
            if rainfall.replace(".", "").isdigit():
               rainfall = float(rainfall)
            else:
               continue

            record = {
               "year": year,
               "month": month,
               "rainfall": rainfall
            }
            self.insert(record)

if __name__ == "__main__":
    archive = Archive()
#Call the load_records_from_csv method on the archive object, passing in the specified CSV file
    archive.load_records_from_csv("Armagh.csv")

    year_one = int(input("Enter the first year: "))
    year_two = int(input("Enter the second year: "))
    k = int(input("Enter the number of months for the moving average: "))
#Call the sma method on the archive object, passing in the entered first n second year and months for the moving average
    moving_averages = archive.sma(year_one, year_two, k)
    for year, year_averages in moving_averages.items():
        print(f"Year: {year}")
        for i, average in enumerate(year_averages):
            print(f"Month {i + 1}: {average}")