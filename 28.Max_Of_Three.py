var1, var2, var3 = [raw_input() for i in range(3)]

#goal of this exrcise to find a maximum value without using max()
max_so_far = None
var_list = [var1, var2, var3]

#looping through the list in order to find maximum value and assign it to the variable max_so_far
for number in var_list:
    if number > max_so_far:
        max_so_far = number
print max_so_far

