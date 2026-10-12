import csv

class DataPipeline:
    def __init__(self, source, destination):
        self.source= source
        self.destination= destination

    # Extraxt Data
    def extract_data(self):
        print(f"Extracting data from {self.source}")
        data = []

        with open(self.source, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                data.append(row)
        return data

    # Transforming Data
    def transform_data(self, data):
        print("Tranforming the data")
        cleaned_data=[]
        for row in data:
            if row["amount"] not in [None, "", "Null"]:
                row["amount"] = float(row["amount"])
                cleaned_data.append(row)
        return cleaned_data

    # Loading the data to destination
    def load_data(self, data):
        print(f"Loading {len(data)} records to {self.destination}")
        if not data:
            print("No data to write.")
            return 
        with open(self.destination, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    # Orchestrate Flow
    def run(self):
        data = self.extract_data()
        transformed_data = self.transform_data(data)
        self.load_data(transformed_data)

pipeline = DataPipeline(
    source="data/raw/messy_orders.csv", 
    destination="data/cleaned/cleaned_orders.csv"
    )
pipeline.run()





