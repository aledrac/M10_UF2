import json

class User:
    def __init__(self, name, age, email, username, password, address):
        self.name = name
        self.age = age
        self.email = email
        self.username = username
        self.password = password
        self.address = address

    # Getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_address(self):
        return self.address

    # Setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_address(self, address):
        self.address = address

    def salutacion(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print(f"Dirección: {self.address}")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "address": self.address
        }

if __name__ == "__main__":
    # Ejemplo de uso
    user1 = User("Manolito Pepote", 30, "man.pep@example.com", "man_pepote", "13478", "123 Main St")
    user1.salutacion()

    # Convertir a formato JSON
    user_dict = user1.to_dict()
    user_json = json.dumps(user_dict, indent=2)
    print("\nUser en formato JSON:")
    print(user_json)
