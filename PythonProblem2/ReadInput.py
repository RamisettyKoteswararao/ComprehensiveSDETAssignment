import csv


class ReadAndWriteData:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = self.read_data()

    def read_data(self):
        data = []
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Assuming the first row contains headers
            for row in reader:
                data.append(dict(zip(headers, row)))
        return data

    def display_data(self):
        for record in self.data:

            print(f"Name: {record['Name']}, Cources: {record['Cources']}, Experience: {record['Experience']}")


# Example Usage:
csv_file_path = './PythonDataNew.csv'
data_reader = ReadAndWriteData(csv_file_path)
data_reader.display_data()
