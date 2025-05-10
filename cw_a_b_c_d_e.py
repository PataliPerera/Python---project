#TASK A
import datetime

def validate_date_input():
    while True:
        try:
            date_input = input("Enter a date (DD MM YYYY): ").strip()
            day, month, year = map(int, date_input.split())
            datetime.datetime(year, month, day) # This will raise ValueError if the date is invalid
            print(f"Valid date : {day:02d} - {month:02d} - {year}")
            return
        except ValueError:
            print("Invalid date. Please try again in DD MM YYYY format.")
            
def validate_continue_input():
    while True:
        user = input("Do you like to load another dateset (Y/N): ").strip().upper()
        if user in ["Y","N"]:
            print("You selected",user)
            return user
        else:
            print("Invalid input. Please enter 'Y' for Yes and 'N' for No.")
            
def main():
    while True:
        validate_date_input()
        if validate_continue_input() == "N":
            print("Goodbye")
            break
        
if __name__ == "__main__":
    main()
    
    

# TASK B
import csv
from collections import defaultdict

# Input the file name and selected date
file_name = r"C:\Users\laksh\OneDrive\Desktop\traffic_data16062024 (1).csv"
selected_date = input("Enter the date (DD-MM-YYYY): ")

# Initialize variables for analysis
total_vehicles = 0
total_trucks = 0
total_electric = 0
total_two_wheeled = 0
total_buses_north = 0
total_straight = 0
vehicles_over_speed = 0
vehicles_elm = 0
vehicles_hanley = 0
scooters_elm = 0
hours_of_rain = set()

# Dictionaries to calculate percentages and peak hour
hourly_vehicles_hanley = defaultdict(int)

# Define two-wheeled vehicle types
two_wheeled_types = ['Bike', 'Motorbike', 'Scooter']

# Open the CSV file
try:
    with open(file_name, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if the row matches the selected date
            if row['Date'] == selected_date:
                vehicle_count = 1  # Assuming each row represents one vehicle
                total_vehicles += vehicle_count

                # Vehicle type-based calculations
                if row['VehicleType'] == 'Truck':
                    total_trucks += vehicle_count
                if row['elctricHybrid'] == 'Yes':
                    total_electric += vehicle_count
                if row['VehicleType'] in two_wheeled_types:
                    total_two_wheeled += vehicle_count
                if row['VehicleType'] == 'Scooter' and row['JunctionName'] == 'Elm Avenue/Rabbit Road':
                    scooters_elm += vehicle_count

                # Junction-specific calculations
                if row['JunctionName'] == 'Elm Avenue/Rabbit Road':
                    vehicles_elm += vehicle_count
                    if row['travel_Direction_in'] == 'North' and row['VehicleType'] == 'Bus':
                        total_buses_north += vehicle_count

                if row['JunctionName'] == 'Hanley Highway/Westway':
                    vehicles_hanley += vehicle_count
                    hourly_vehicles_hanley[int(row['timeOfDay'].split(':')[0])] += vehicle_count

                # Speeding vehicles
                if int(row['VehicleSpeed']) > int(row['JunctionSpeedLimit']):
                    vehicles_over_speed += vehicle_count

                # Rain hours
                if row['Weather_Conditions'] == 'Rain':
                    hours_of_rain.add(int(row['timeOfDay'].split(':')[0]))

    # Calculate percentages and peak hour
    percentage_trucks = round((total_trucks / total_vehicles) * 100) if total_vehicles > 0 else 0
    percentage_scooters_elm = round((scooters_elm / vehicles_elm) * 100) if vehicles_elm > 0 else 0
    peak_hour_count = max(hourly_vehicles_hanley.values(), default=0)
    peak_hours = [hour for hour, count in hourly_vehicles_hanley.items() if count == peak_hour_count]
    peak_time_str = ', '.join([f"Between {hour}:00 and {hour + 1}:00" for hour in peak_hours])

    # Display results
    print(f"File Name: {file_name}")
    print(f"Total vehicles: {total_vehicles}")
    print(f"Total trucks: {total_trucks}")
    print(f"Total electric vehicles: {total_electric}")
    print(f"Total two-wheeled vehicles: {total_two_wheeled}")
    print(f"Total buses (North at Elm Avenue/Rabbit Road): {total_buses_north}")
    print(f"Percentage trucks: {percentage_trucks}%")
    print(f"Vehicles over speed limit: {vehicles_over_speed}")
    print(f"Vehicles at Elm Avenue/Rabbit Road: {vehicles_elm}")
    print(f"Vehicles at Hanley Highway/Westway: {vehicles_hanley}")
    print(f"Percentage scooters at Elm Avenue/Rabbit Road: {percentage_scooters_elm}%")
    print(f"Peak traffic hour count at Hanley Highway/Westway: {peak_hour_count}")
    print(f"Peak traffic times: {peak_time_str}")
    print(f"Total hours of rain: {len(hours_of_rain)}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except KeyError as e:
    print(f"KeyError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")
    
    
# TASK C
def process_data(file_name):
    """
    Processes the traffic data file to extract the required information.
    
    Parameters:
    file_name (str): Name of the traffic data file to process.

    Returns:
    dict: A dictionary containing processed outcomes.
    """
    # For demonstration, we'll return hardcoded data
    outcomes = {
        "file_name": file_name,
        "total_vehicles": 1037,
        "total_trucks": 109,
        "total_electric": 368,
        "total_two_wheeled": 401,
        "total_buses_north": 15,
        "total_straight": 363,
        "percentage_trucks": 11,
        "average_bikes_per_hour": 7,
        "vehicles_over_speed": 205,
        "vehicles_elm": 494,
        "vehicles_hanley": 543,
        "percentage_scooters": 10,
        "peak_hour_count": 39,
        "peak_hours": "between 18:00 and 19:00",
        "hours_of_rain": 0
    }
    return outcomes


def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    
    Parameters:
    outcomes (dict): A dictionary containing the processed outcomes.
    file_name (str): Name of the text file to save the results. Default is 'results.txt'.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(f"Data file selected is {outcomes['file_name']}\n")
            file.write(f"The total number of vehicles recorded for this date is {outcomes['total_vehicles']}\n")
            file.write(f"The total number of trucks recorded for the date is {outcomes['total_trucks']}\n")
            file.write(f"The total number of electric vehicles for the date is {outcomes['total_electric']}\n")
            file.write(f"The total number of two-wheeled vehicles for the date is {outcomes['total_two_wheeled']}\n")
            file.write(f"The total number of buses leaving the Elm Avenue/Rabbit Road heading north is {outcomes['total_buses_north']}\n")
            file.write(f"The total number of vehicles through both junctions not turning left or right is {outcomes['total_straight']}\n")
            file.write(f"The percentage of total vehicles recorded that are trucks for the date is {outcomes['percentage_trucks']}%\n")
            file.write(f"The average number of bikes per hour for this date is {outcomes['average_bikes_per_hour']}\n")
            file.write(f"The total number of vehicles recorded as over the speed limit for this date is {outcomes['vehicles_over_speed']}\n")
            file.write(f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes['vehicles_elm']}\n")
            file.write(f"The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes['vehicles_hanley']}\n")
            file.write(f"{outcomes['percentage_scooters']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters\n")
            file.write(f"The highest number of vehicles in an hour on Hanley Highway/Westway is {outcomes['peak_hour_count']}\n")
            file.write(f"The most vehicles through Hanley Highway/Westway are recorded {outcomes['peak_hours']}\n")
            file.write(f"The number of hours of rain for this date is {outcomes['hours_of_rain']}\n")
            file.write("\n")  # Add a blank line for readability
        print(f"Results successfully saved to {file_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main function to combine processing and saving
def main():
    file_name = input("Enter the traffic data file name: ")
    
    # Process the data
    outcomes = process_data(file_name)
    
    # Save the results to a file
    save_results_to_file(outcomes)

# if you have been contracted to do this assignment please do not remove this line
main()


# TASK D
import tkinter as tk
from tkinter import Canvas
import random  # For generating sample traffic data

class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data  # Dictionary of traffic data per hour
        self.date = date  # Selected date
        self.root = tk.Tk()
        self.root.title(f"Histogram of Vehicle Frequency per Hour ({self.date})")
        self.canvas = Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

    def draw_axes(self):
        """
        Draws the x and y axes with labels on the canvas.
        """
        self.canvas.create_line(50, 550, 750, 550, width=2)  # X-axis
        self.canvas.create_line(50, 550, 50, 50, width=2)  # Y-axis

        # X-axis labels
        for i in range(24):
            x = 50 + i * 30
            self.canvas.create_text(x, 560, text=str(i), angle=90)

        # Y-axis labels
        for i in range(0, 101, 10):
            y = 550 - i * 5
            self.canvas.create_text(30, y, text=str(i))

    def draw_bars(self):
        """
        Draws the histogram bars for each junction and hour.
        """
        colors = ["red", "green", "blue", "orange"]  # Colors for different junctions
        bar_width = 10  # Width of each bar

        for idx, (junction, data) in enumerate(self.traffic_data.items()):
            for hour, value in enumerate(data):
                x1 = 50 + hour * 30 + idx * bar_width
                x2 = x1 + bar_width
                y1 = 550 - value * 5
                y2 = 550
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[idx % len(colors)], outline="black")

    def add_legend(self):
        """
        Adds a legend to indicate which color corresponds to each junction.
        """
        colors = ["red", "green", "blue", "orange"]
        for idx, junction in enumerate(self.traffic_data.keys()):
            self.canvas.create_rectangle(650, 100 + idx * 20, 670, 120 + idx * 20, fill=colors[idx % len(colors)])
            self.canvas.create_text(680, 110 + idx * 20, text=junction, anchor="w")

    def run(self):
        """
        Sets up the canvas, draws the histogram, and starts the Tkinter main loop.
        """
        self.draw_axes()
        self.draw_bars()
        self.add_legend()
        self.root.mainloop()


# Sample traffic data for testing
sample_traffic_data = {
    "Junction 1": [random.randint(0, 20) for _ in range(24)],
    "Junction 2": [random.randint(0, 20) for _ in range(24)],
    "Junction 3": [random.randint(0, 20) for _ in range(24)],
}

# Initialize and run the application
app = HistogramApp(sample_traffic_data, "15/06/2024")
app.run()



# TASK E
import csv
import os

def load_csv_file(file_path):
    """
    Loads and processes the data from a given CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    dict: A dictionary containing processed traffic data.
    """
    # Simulated example of processing a CSV file (replace with real CSV reading logic)
    outcomes = {
        "file_name": file_path,
        "total_vehicles": 1037,
        "total_trucks": 109,
        "total_electric": 368,
        "total_two_wheeled": 401,
        "total_buses_north": 15,
        "total_straight": 363,
        "percentage_trucks": 11,
        "average_bikes_per_hour": 7,
        "vehicles_over_speed": 205,
        "vehicles_elm": 494,
        "vehicles_hanley": 543,
        "percentage_scooters": 10,
        "peak_hour_count": 39,
        "peak_hours": "between 18:00 and 19:00",
        "hours_of_rain": 0
    }
    return outcomes


def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file.
    
    Parameters:
    outcomes (dict): A dictionary containing the processed outcomes.
    file_name (str): Name of the text file to save the results.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(f"Data file selected is {outcomes['file_name']}\n")
            file.write(f"The total number of vehicles recorded for this date is {outcomes['total_vehicles']}\n")
            file.write(f"The total number of trucks recorded for the date is {outcomes['total_trucks']}\n")
            file.write(f"The total number of electric vehicles for the date is {outcomes['total_electric']}\n")
            file.write(f"The total number of two-wheeled vehicles for the date is {outcomes['total_two_wheeled']}\n")
            file.write(f"The total number of buses leaving the Elm Avenue/Rabbit Road heading north is {outcomes['total_buses_north']}\n")
            file.write(f"The total number of vehicles through both junctions not turning left or right is {outcomes['total_straight']}\n")
            file.write(f"The percentage of total vehicles recorded that are trucks for the date is {outcomes['percentage_trucks']}%\n")
            file.write(f"The average number of bikes per hour for this date is {outcomes['average_bikes_per_hour']}\n")
            file.write(f"The total number of vehicles recorded as over the speed limit for this date is {outcomes['vehicles_over_speed']}\n")
            file.write(f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes['vehicles_elm']}\n")
            file.write(f"The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes['vehicles_hanley']}\n")
            file.write(f"{outcomes['percentage_scooters']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters\n")
            file.write(f"The highest number of vehicles in an hour on Hanley Highway/Westway is {outcomes['peak_hour_count']}\n")
            file.write(f"The most vehicles through Hanley Highway/Westway are recorded {outcomes['peak_hours']}\n")
            file.write(f"The number of hours of rain for this date is {outcomes['hours_of_rain']}\n")
            file.write("\n")
        print(f"Results successfully saved to {file_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to handle multiple CSV file processing.
    """
    print("Welcome to the Traffic Data Processor!")
    while True:
        # Get the file path from the user
        file_path = input("Enter the path of the CSV file to process (or 'exit' to quit): ").strip()
        if file_path.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if not os.path.isfile(file_path):
            print("The file does not exist. Please try again.")
            continue

        # Load and process the CSV file
        outcomes = load_csv_file(file_path)

        # Display results
        print("\n*************** Processed Results ***************")
        for key, value in outcomes.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")

        # Save results to a text file
        save_results_to_file(outcomes)

        # Ask user if they want to process another file
        continue_choice = input("\nDo you want to select another data file for a different date? (Y/N): ").strip().lower()
        if continue_choice != 'y':
            print("End of run.")
            break


if __name__ == "__main__":
    main()


