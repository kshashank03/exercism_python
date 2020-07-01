import re
class PhoneNumber:
    def __init__(self, number):
        self.number = number
        return re.findall("\n+", self.number)


