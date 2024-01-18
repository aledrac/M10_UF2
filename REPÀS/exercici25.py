import json

class Vehicle:
    def __init__(self, make, model, year, color, fuel_type, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.mileage = mileage

    # Getters
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_fuel_type(self):
        return self.fuel_type

    def get_mileage(self):
        return self.mileage

    # Setters
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_color(self, color):
        self.color = color

    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type

    def set_mileage(self, mileage):
        self.mileage = mileage

    def parts(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Mileage: {self.mileage}")

    def to_dict(self):
        return {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "fuel_type": self.fuel_type,
            "mileage": self.mileage
        }

if __name__ == "__main__":
    # Ejemplo de uso
    vehicle1 = Vehicle("Toyota", "Camry", 2022, "Blue", "Gasolina", 15000)
    vehicle1.parts()

    # Convertir a formato JSON
    vehicle_dict = vehicle1.to_dict()
    vehicle_json = json.dumps(vehicle_dict, indent=2)
    print("\nVehicle as JSON:")
    print(vehicle_json)
