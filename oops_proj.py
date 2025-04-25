class chatbook:

    __user_id = 0  # static method

    def __init__(self):
        self.id = chatbook.__user_id  # to access static method
        chatbook.__user_id += 1
        self.__name = "Default user"  # now name is a hidden attribute (encapsulation)
        self.user_id = 0
        self.user_id += 1
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()  # calling method under constructor

    def get_name(self):  # getter
        return self.__name

    def set_name(self, value):  # setter
        self.__name = value

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
            self.write_post()
        elif user_input == "4":
            self.sendmsg()
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

    def write_post(self):
        if self.loggedin == False:
            print("please signup/signin first")
        else:
            txt = input("enter your msg here: ")
            print(f"follwing content has been posted {txt}")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("enter your msg: ")
            frnd = input("whom to send msg: ")
            print(f"your msg has been sent to {frnd}")
        else:
            print("please signup/signin first")
        print("\n")
        self.menu()


# obj1 = chatbook()  # consturctor called as obj is made here
