def collatz(number):
    if(number % 2 == 0):
        return number // 2
    else:
        return 3 * number + 1
    
def user_input():
    num = input('Enter number: ')
    while True:
        try:
            return int(num)
            break
        except ValueError:
            print('Please enter an integer.')
            num = input('Enter number: ')

num = user_input()
while(num != 1):
    num = collatz(num)
    print(num)