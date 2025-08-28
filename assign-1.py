# Assignment 1: Smartphone Example

class Smartphone:
    def __init__(self, brand, model, battery):
        # constructor initializes attributes
        self.brand = brand
        self.model = model
        self.battery = battery  # percentage (0–100)
    
    def call(self, number):
        if self.battery > 5:
            print(f"{self.brand} {self.model} is calling {number} 📞...")
            self.battery -= 5
        else:
            print("Battery too low to make a call! 🔋")
    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}% ⚡")

# Inheritance: GamingSmartphone extends Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery, gpu_power):
        # call parent constructor
        super().__init__(brand, model, battery)
        self.gpu_power = gpu_power
    
    def play_game(self, game):
        if self.battery > 20:
            print(f"Playing {game} on {self.brand} {self.model} 🎮 (GPU: {self.gpu_power})")
            self.battery -= 20
        else:
            print("Battery too low to play games! 😢")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S21", 50)
phone1.call("0712345678")
phone1.charge(30)

gaming_phone = GamingSmartphone("Asus", "ROG Phone", 80, "Adreno 730")
gaming_phone.play_game("PUBG Mobile")
gaming_phone.call("0798765432")
