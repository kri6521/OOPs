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
                            5. press any other key to exit\n"""
        )
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your email here: ")
        pwd = input("setup your password: ")
        self.username = email
        self.password = pwd
        print("you have signed up successfully\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("please signup first by pressing 1 in the main menu")

        else:
            uname = input("enter your email/username here: ")
            pwd = input("enter your password: ")
            if self.username == uname and self.password == pwd:
                print("signed in successfully")
                self.loggedin = True
            else:
                print("please input correct credentials")
        print("\n")
        self.menu()

    def signup(self):
        email = input("enter your email here: ")
        pwd = input("setup your password: ")
        self.username = email
        self.password = pwd
        print("you have signed up successfully\n")
        self.menu()


obj1 = chatbook()  # consturctor called as obj is made here
