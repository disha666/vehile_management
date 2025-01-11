import json
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# Vehicle Class Hierarchy
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def calculate_fuel_efficiency(self):
        pass

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @model.setter
    def model(self, value):
        self.__model = value

    @abstractmethod
    def get_details(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.__number_of_doors = number_of_doors

    def start_engine(self):
        return f"Car engine of {self.brand} {self.model} started."

    def stop_engine(self):
        return f"Car engine of {self.brand} {self.model} stopped."

    def calculate_fuel_efficiency(self):
        return f"Car fuel efficiency: 25 MPG."

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        self.__number_of_doors = value

    def get_details(self):
        return f"Car: {self.brand} {self.model}, Doors: {self.__number_of_doors}"


class Truck(Vehicle):
    def __init__(self, brand, model, payload_capacity):
        super().__init__(brand, model)
        self.__payload_capacity = payload_capacity

    def start_engine(self):
        return f"Truck engine of {self.brand} {self.model} started."

    def stop_engine(self):
        return f"Truck engine of {self.brand} {self.model} stopped."

    def calculate_fuel_efficiency(self):
        return f"Truck fuel efficiency: 15 MPG considering payload capacity of {self.__payload_capacity} tons."

    @property
    def payload_capacity(self):
        return self.__payload_capacity

    @payload_capacity.setter
    def payload_capacity(self, value):
        self.__payload_capacity = value

    def get_details(self):
        return f"Truck: {self.brand} {self.model}, Payload Capacity: {self.__payload_capacity} tons"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.__has_sidecar = has_sidecar

    def start_engine(self):
        return f"Motorcycle engine of {self.brand} {self.model} started."

    def stop_engine(self):
        return f"Motorcycle engine of {self.brand} {self.model} stopped."

    def calculate_fuel_efficiency(self):
        return f"Motorcycle fuel efficiency: 50 MPG."

    @property
    def has_sidecar(self):
        return self.__has_sidecar

    @has_sidecar.setter
    def has_sidecar(self, value):
        self.__has_sidecar = value

    def get_details(self):
        return f"Motorcycle: {self.brand} {self.model}, Sidecar: {'Yes' if self.__has_sidecar else 'No'}"


# Function to save vehicle data to JSON
def save_to_json(vehicle_details):
    try:
        with open("vehicle_data.json", "a") as file:
            json.dump(vehicle_details, file)
            file.write("\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving data: {e}")


# Tkinter GUI setup
class VehicleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Management System")

        self.vehicle = None

        self.main_interface()

    def main_interface(self):
        # First Interface to select vehicle type
        self.clear_window()

        tk.Label(self.root, text="Select Vehicle Type", font=("Arial", 16)).pack(pady=20)

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        self.car_button = tk.Button(button_frame, text="Car", command=self.select_car, width=20, bg="lightblue")
        self.car_button.grid(row=0, column=0, padx=10)

        self.truck_button = tk.Button(button_frame, text="Truck", command=self.select_truck, width=20, bg="lightgreen")
        self.truck_button.grid(row=0, column=1, padx=10)

        self.motorcycle_button = tk.Button(button_frame, text="Motorcycle", command=self.select_motorcycle, width=20, bg="lightcoral")
        self.motorcycle_button.grid(row=1, column=0, padx=10)

    def select_car(self):
        self.vehicle = Car("", "", 4)
        self.vehicle_details_interface()

    def select_truck(self):
        self.vehicle = Truck("", "", 0)
        self.vehicle_details_interface()

    def select_motorcycle(self):
        self.vehicle = Motorcycle("", "", False)
        self.vehicle_details_interface()

    def vehicle_details_interface(self):
        # Second Interface to enter vehicle details
        self.clear_window()

        tk.Label(self.root, text="Enter Vehicle Details", font=("Arial", 16)).pack(pady=20)

        self.license_no_label = tk.Label(self.root, text="License Number:")
        self.license_no_label.pack()
        self.license_no_entry = tk.Entry(self.root)
        self.license_no_entry.pack()

        self.make_label = tk.Label(self.root, text="Make:")
        self.make_label.pack()
        self.make_entry = tk.Entry(self.root)
        self.make_entry.pack()

        self.model_label = tk.Label(self.root, text="Model:")
        self.model_label.pack()
        self.model_entry = tk.Entry(self.root)
        self.model_entry.pack()

        self.year_label = tk.Label(self.root, text="Year:")
        self.year_label.pack()
        self.year_entry = tk.Entry(self.root)
        self.year_entry.pack()

        self.save_button = tk.Button(self.root, text="Save", command=self.save_vehicle, width=20, bg="lightgreen")
        self.save_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app, width=20, bg="lightcoral")
        self.exit_button.pack()

    def save_vehicle(self):
        license_no = self.license_no_entry.get()
        make = self.make_entry.get()
        model = self.model_entry.get()
        year = self.year_entry.get()

        if not all([license_no, make, model, year]):
            messagebox.showerror("Error", "Please fill all the details")
            return

        # Set the details for the vehicle object
        self.vehicle.brand = make
        self.vehicle.model = model

        vehicle_details = {
            "license_no": license_no,
            "make": make,
            "model": model,
            "year": year,
            "vehicle_type": self.vehicle.__class__.__name__,
            "details": self.vehicle.get_details()
        }

        save_to_json(vehicle_details)
        messagebox.showinfo("Success", "Vehicle details saved successfully")
        self.main_interface()

    def exit_app(self):
        self.root.quit()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Tkinter window initialization
def run_app():
    root = tk.Tk()
    app = VehicleGUI(root)
    root.geometry("400x600")
    root.mainloop()

# Run the app
if __name__ == "__main__":
    run_app()
