class user:
    name=''
    email=''
    password=''
    login=True

    def login(self):
        email=input('enter your email:')
        password=input('input your password:')

        if email==self.email and password==self.password:
            login=True
            print('login successful')
        else:
            print('login fail')


    def logout(self):
        login=False
        print('logout')


    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False
    

user1