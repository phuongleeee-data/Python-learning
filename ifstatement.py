print('Exercise 5-3\n')
ailen_color ='yellow'

if ailen_color == 'yellow':
    print('You have earned 5 points')
if ailen_color == 'red':
    print('You have no points')

print('\nExercise 5-4\n')
ailen_color = 'black'

if ailen_color == "green":
    print('You have earned 5 points')
else:
    print('You have earned 10 points')

print('\nExercise 5-6\n')
age = int(input('Enter your age: '))

if age < 2:
    print('Bạn là em bé bú bình')
elif age >= 2 and age < 4:
    print('Bạn đi mẫu giáo')
elif age >= 4 and age < 13:
    print('Bạn là học sinh cấp 1')
elif age >= 13 and age < 20:
    print('Bạn là trẻ vị thành niên')
elif age >= 20 and age < 65:
    print('Bạn là người lớn')
else:
    print('Bạn là cụ già')


