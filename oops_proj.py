class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()  # calling method under constructor

    def menu(self):
        user_input = input(
            """welcome to chatbook! how would you like to proceed
                            1. press 1 to signup
                            2. press 2 to signin
                            3. press 3 to write a post
                            4. press 4 to msg a friend
                            5. press any other key to exit"""
        )
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


obj1 = chatbook()  # consturctor called as obj is made here
