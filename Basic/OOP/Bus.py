from Vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, top_speed=100):
        super().__init__(top_speed)
        self.passergers = []


    def add_group(self, passergers):
        self.passergers.extend(passergers)


bus1 = Bus(80)
bus1.add_warning('warning form bus')
bus1.add_group(['triss', 'jenni', 'lovato'])
print(bus1.passergers)
bus1.drive()
