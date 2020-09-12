# Problem 1

'''isprimenumber.py is the python file containing following code'''

'''
"""Tells whether a given number is prime or not"""

def isprime(input_num):

    """Function for determining whether a number is prime or not"""
    
    if input_num > 1:
        for num in range(2, input_num):
            if input_num % num==0:
                return 'Number is not a Prime number'
                break
        else:
            return 'Number is a Prime number'
    else:
        return 'Number is not a Prime number'
'''
# we need to run following in terminal in order to test our code using pylint
# Change directory to one containing the python file.
# run following command in it
'''    pylint "isprimenumber.py"   '''
# alternatively we can use pylint as following

from pylint import epylint
epylint.py_run('isprimenumber.py')

# part 2 of problem 1

import isprimenumber, unittest

class prime_number(unittest.TestCase):
    def testing_two_digit_number(self):
        num_ber = 28
        result = isprimenumber.isprime(num_ber)
        self.assertEqual(result, 'Number is not a Prime number')

    def testing_three_digit_number(self):
        num_ber1 = 107
        result = isprimenumber.isprime(num_ber1)
        self.assertEqual(result, 'Number is a Prime number')

    def testing_four_digit_number(self):
        num_ber = 1077
        result = isprimenumber.isprime(num_ber)
        self.assertEqual(result, 'Number is not a Prime number')

if __name__ == "__main__":
    unittest.main()


# Problem 2

def armstrong():
    start = 1
    end = 1000
    for i in range(start, end+1):
        sum = 0
        temp_numb = i
        power = len(str(i))
        while temp_numb > 0:
            number = temp_numb % 10
            sum += number ** power
            temp_numb //= 10
        if i == sum:
            yield i

print(list(armstrong()))

