name=input("name:")
age=input("age:")
hobbie=input("hobbil:")

msg=f'''
-----------------input alex--------------
Name      :{name}
Age       :{age}
Hobbie    :{hobbie}
-----------------out alex----------------
'''
print(msg)

if age<18:
    print(f"{name} is not old enough")