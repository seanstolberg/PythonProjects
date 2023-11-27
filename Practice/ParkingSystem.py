class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_slots = big
        self.medium_slots = medium
        self.small_slots = small

    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                if self.big_slots > 0:
                    self.big_slots -= 1
                    return True
                else:
                    return False
            case 2:
                if self.medium_slots > 0:
                    self.medium_slots -= 1
                    return True
                else:
                    return False
            case 3:
                if self.small_slots > 0:
                    self.small_slots -= 1
                    return True
                else:
                    return False
            case _:
                return False

obj = ParkingSystem(1,1,0) 
print(obj.addCar(1)) # true
print(obj.addCar(2)) # true
print(obj.addCar(3)) # false
print(obj.addCar(1)) # false
