class Vehicle:
    def __init__(self, top_speed=100):
        self.top_speed = top_speed
        self.__warings = []

    def drive(self):
        print('I am driving but certenly ont faster than {}'.format(self.top_speed))

    def __repr__(self):
        print("Printing...")
        return f'Top speed: {self.top_speed} Warings: {len(self.__warings)}'

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warings.append(warning_text)

    def get_warning(self):
        return self.__warings