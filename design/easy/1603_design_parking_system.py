"""
You need to design a parking system for a parking lot. The parking lot has three types of parking spaces: big, medium, and small, each with a fixed number of slots.

Implement the class ParkingSystem:
    + ParkingSystem(int big, int medium, int small): Initializes the ParkingSystem object. The number of available slots for each type of parking space is given in the constructor;
    + bool addCar(int carType): Checks whether there is an available parking space for the incoming car:
        + carType = 1 → big car (needs a big slot);
        + carType = 2 → medium car (needs a medium slot);
        + carType = 3 → small car (needs a small slot);
If there is no space available for the given type, return false. Otherwise, allocate a slot and return true.

Example:
Input: ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"], [[1, 1, 0], [1], [2], [3], [1]]  
Output: [null, true, true, false, false]

Нужно разработать систему парковки для стоянки. На парковке есть три вида мест: большие, средние и маленькие, при этом для каждого типа задано фиксированное количество мест.

Реализуйте класс ParkingSystem:
    + ParkingSystem(int big, int medium, int small): конструктор, инициализирует объект. В нём задаётся количество доступных мест каждого типа;
    + bool addCar(int carType): проверяет, есть ли свободное место для машины данного типа:
        + carType = 1 → большая машина (требует большое место);
        + carType = 2 → средняя машина (требует среднее место);
        + carType = 3 → маленькая машина (требует маленькое место);
Если места нет — возвращается false. Если место есть — машина паркуется, и возвращается true.

Пример:
Ввод: ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"], [[1, 1, 0], [1], [2], [3], [1]]  
Вывод: [null, true, true, false, false]
"""

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False