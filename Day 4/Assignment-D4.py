# Program for finding first Armstrong number in the given range
start = 1042000
end = 702648265
for i in range(start, end+1):
    sum = 0
    temp_numb = i
    power = len(str(i))
    while temp_numb > 0:
        number = temp_numb % 10
        sum += number ** power
        temp_numb //= 10
    if i == sum:
        print(i, 'is the first armstrong number')
        break
    else:   # Not neccessary, just for the sake of completing 'if' loop with 'else'.
        pass 
