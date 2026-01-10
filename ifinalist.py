print('Exercise 5-8\n')
user_name = ['admin', 'ca', 'phuong', 'dieu', 'thong']

for name in user_name:
    if name == "admin":
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for logging in again.')

print('\nExercise 5-9\n')
nguoi_dung =[]

if nguoi_dung:
    for name in nguoi_dung:
        if name == "admin":
            print(f'Hello admin, thank you for logging in again.')
        else:
            print(f"Hello {name}, thank you for logging in again.")

else:
    print('We need to find some users!')

