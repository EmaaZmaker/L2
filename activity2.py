class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("THE DESTRUCTOR HAS AWAKENED")
def create_object():
    print("Making Item...")
    obj=Employee()
    print("Function End :p")
    return obj
obj=create_object()