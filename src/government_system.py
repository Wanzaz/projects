from random import randint

print("This is program for vaccination registration")
print("Follow orders and answer truthfully")
age = float(input("Enter your age here:  "))


if age <= 0:
    print("please enter your real age")
elif age <= 18:
    print("you are a child so you will get vaccinations only among the last so in November")
    first_name = input("Enter your firstname:  ")
    last_name = input("Enter your last name:  ")
    pin = input("Enter your personal identification number here:  ")
    initials = ((first_name[0] + last_name[0]).upper())
    vac_day = randint(1, 30)
    try:
        int(pin)
    except:
        print("NOT NUMBER")
        pin = " "
    while len(pin) < 9:
        pin = input("It is too short, write it again:  ")
        try:
            int(pin)
            pin = pin
        except:
            print("Not number!")
            pin = " "
            print(pin)
    print(f"""
                  Hello {initials},
                  your date for vaccinations is 11. 9. 2021 at 11:00.
                  Best regards,
                  your government
                  """)
elif age <= 24:
    print("you are student that means you will ger vaccinations before kids in September ")
    first_name = input("Enter your firstname:  ")
    last_name = input("Enter your last name:  ")
    pin = input("Enter your personal identification number here:  ")
    initials = ((first_name[0] + last_name[0]).upper())
    vac_day = randint(1, 30)
    try:
        int(pin)
    except:
        print("NOT NUMBER")
        pin = " "
    while len(pin) < 9:
        pin = input("It is too short, write it again:  ")
        try:
            int(pin)
            pin = pin
        except:
            print("Not number!")
            pin = " "
            print(pin)
    print(f"""
                  Hello {initials},
                  your date for vaccinations is {vac_day}. 9. 2021 at 16:00.
                  Best regards,
                  your government
                  """)
elif age <= 50:
    print("you are young person that means you will ger vaccinations before students in July ")
    first_name = input("Enter your firstname:  ")
    last_name = input("Enter your last name:  ")
    pin = input("Enter your personal identification number here:  ")
    initials = ((first_name[0] + last_name[0]).upper())
    vac_day = randint(1, 30)
    try:
        int(pin)
    except:
        print("NOT NUMBER")
        pin = " "
    while len(pin) < 9:
        pin = input("It is too short, write it again:  ")
        try:
            int(pin)
            pin = pin
        except:
            print("Not number!")
            pin = " "
            print(pin)
    print(f"""
                  Hello {initials},
                  your date for vaccinations is {vac_day}. 6. 2021 at 13:00.
                  Best regards,
                  your government
                  """)
elif age >= 50:
    print("you are senior that means you will ger vaccinations before young people in April ")
    first_name = input("Enter your firstname:  ")
    last_name = input("Enter your last name:  ")
    pin = input("Enter your personal identification number here:  ")
    initials = ((first_name[0] + last_name[0]).upper())
    vac_day = randint(1, 30)
    try:
        int(pin)
    except:
        print("NOT NUMBER")
        pin = " "
    while len(pin) < 9:
        pin = input("It is too short, write it again:  ")
        try:
            int(pin)
            pin = pin
        except:
            print("Not number!")
            pin = " "
            print(pin)
    print(f"""
                  Hello {initials},
                  your date for vaccinations is {vac_day}. 4. 2021 at 9:00.
                  Best regards,
                  your government
                  """)
else:
    print("something is wrong please try it again")
