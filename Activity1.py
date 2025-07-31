class EAstring():
    def __init__(self): #<---constructor
        self.str1=""
    def get_string(self):
        self.str1=input("ËNTER YOUR KEYWORD/STRING")
    def print_string(self):
        print(self.str1.upper())
str1=EAstring()
str1.get_string()
str1.print_string()
        