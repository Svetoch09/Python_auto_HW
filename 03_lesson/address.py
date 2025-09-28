class Address:
    def __init__(self, index, city, street, building_number, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.building_number = building_number
        self.apartment = apartment

    def __str__(self):
        return (f"{self.index},{self.city},{self.street},"
                f"{self.building_number} - {self.apartment}")
