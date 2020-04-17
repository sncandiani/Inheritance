class Vehicle: 
    def __init__(self, name, color, speed): 
        self.name = name
        self.color = color 
        self.speed = speed
    def drive(self):
        print(f"The {self.color} {self.name} drives past. RRrrrrrummbbble!")
    def turn(self, direction): 
        print(f"{self.name} turns {direction}")
    def stop(self): 
        print(f"{self.name} rolls to a stop after rolling a mile down the runway.")