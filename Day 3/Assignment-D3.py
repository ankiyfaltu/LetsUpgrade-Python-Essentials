# Problem 1-Pilot Problem
currentalt = int(input('Enter your Current Altitude '))
if currentalt <= 5000 and currentalt > 1000:
    print('Bring your plane further down to 1000 alt.')
elif currentalt <= 1000:
    print('You can land safely. Proceed with the Landing.')
else:
    print('Take a round and try again.')

# Problem 2-Prime Number b/w 1-200
x = 0
for n in range(2, 201):
    if n == 2:
        print(n, 'is prime number')
    else:
        for i in range(2, n+1):
            if n % i == 0:
                x += 1
        if x == 1:
            print(n, 'is prime number')
        else:
            x = 0
