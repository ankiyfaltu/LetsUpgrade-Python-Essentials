# Problem 1 - Identify whether [1,1,5] exist in given list in given order or not.
def identify(li):
    x=0
    for i in range(len(li)):
        if li[i]==1:
            for j in range(i+1, len(li)):
                if li[j]==1:
                    for k in range(j+1, len(li)):
                        if li[k]==5:
                            x=3
    if x==3:
        print('Hurrah!! 1 1 5 exist in given order')
    else:
        print('Given number doesn\'t exist in given order')
trial = [0, 1, 2, 3, 2, 5, 4, 5, 1, 7, 8, 1, 5]
identify(trial)
print("")

# Problem 2 - Prime Number using filter
def isprime(num):
    if num > 1:
        for n in range(2, num):
            if num % n == 0:
                return False
        else:
            return True

numbers = list(range(2500))
primenumbers = filter(isprime, numbers)
prime_numbers_are = list(primenumbers)
print(prime_numbers_are)
print('There are total of ', len(prime_numbers_are), ' prime number in range of 1 to 2500')
print("")

# Problem 3 -
capitalize_string = lambda string: string.upper()   # As per what sai has said "capitalize each and every letter".
capitalize_firstletter = lambda string: string.title()  # As per the output shown in assignment pdf.
letsUpgrade = ['Hey there!', 'Let\'s start coding and have some fun', 'Are you ready for this?']
letsUpgradeConverted = list(map(capitalize_string, letsUpgrade))
letsUpgradeConvertedV2 = list(map(capitalize_firstletter, letsUpgrade))
print(letsUpgradeConverted)
print(letsUpgradeConvertedV2)
