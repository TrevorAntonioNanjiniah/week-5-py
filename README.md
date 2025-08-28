# Week 5 Python Assignments 🐍

This repository contains my solutions for **Week 5 Python assignments**.  
It covers **Object-Oriented Programming (OOP)** concepts such as **Classes, Constructors, Inheritance, and Polymorphism**.  

---

## 📘 Assignment 1: Design Your Own Class

I created a `Smartphone` class with attributes and methods, and then extended it with a `GamingSmartphone` class using **inheritance**.

### 🔑 Key Concepts:
- **Classes & Objects**
- **Constructors (`__init__`)**
- **Encapsulation**
- **Inheritance**

### 📂 Code Example
```python
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery
    
    def call(self, number):
        if self.battery > 5:
            print(f"{self.brand} {self.model} is calling {number} 📞...")
            self.battery -= 5
        else:
            print("Battery too low to make a call! 🔋")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}% ⚡")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery, gpu_power):
        super().__init__(brand, model, battery)
        self.gpu_power = gpu_power
    
    def play_game(self, game):
        if self.battery > 20:
            print(f"Playing {game} on {self.brand} {self.model} 🎮 (GPU: {self.gpu_power})")
            self.battery -= 20
        else:
            print("Battery too low to play games! 😢")
