class Bus:
    __counter = 0
    __ticket_id = None

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination

    def validate_source_destination(self):
        if self.__source == "delhi" and (self.__destination == "mumbai" or "chennai" or "pune" or "kolkata"):
            return True
        else:
            return False

    def generate_ticket(self):
        if self.validate_source_destination() == True:
            self.__ticket_id = self.__source[0] + \
                self.__destination[0] + str(Bus.__counter)
            Bus.__counter += 1
            return self.__ticket_id
        else:
            return "None"

    def get_count():
        return Bus.__counter


Suresh = Bus('Suresh', 'delhi', 'mumbai')
print(Suresh.validate_source_destination())
print(Suresh.generate_ticket())
print(Suresh.generate_ticket())

Kumar = Bus('kumar', 'delhi', 'pne')
print(Kumar.generate_ticket())
print(Bus.get_count())
