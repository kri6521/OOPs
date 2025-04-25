class employee:
    def __init__(self):
        print("started constructor")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"

    # andr wale func me b self jata h
    def travel(self, destination):
        print("called manually")
        print(f"employee is now travelling to {destination}")


# obj
sam = employee()
# print(sam.salary)
sam.travel("patna")  # ye likhne pr travel k andr ka sb print hoga
print(type(sam))
