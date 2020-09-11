# Problem 1
def Input(variable_input):
    def enter_number():
        a = int(input("Enter first Number - "))
        b = int(input("Enter second Number - "))
        variable_input(a,b)
    return enter_number

@Input
def power(number, to_the_power):
    print(number**to_the_power)
@Input
def area(sideA, sideB):
    print(sideA*sideB)

power()
area()

# Problem 2
file = open('text.txt','r')
try:
    file.write('Hey!! Is everything fine there?')
except:
    print('An error occured while trying to write. Check whether you\'ve given written mode as a second argument')
finally:
    file.close()
