def user_reg(user,password):
    config_file='config.txt' 
    try:
        with open(config_file,'a') as file:
            file.write(f"Username {user}")
            file.write(f"Password {password}")
        print("Registration Successfull !!")
    except Exception as e:
        print(f"An error occured {e}")
if __name__== "__main__" :
    user="test_username"
    password="test_password"
    print("Welcome to Registration Page")
    user_reg(user,password) 
