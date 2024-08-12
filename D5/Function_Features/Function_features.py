# max num function for the maximum number in a string
def max_num(a,b,c):
    return max([a,b,c])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

# mult_list to multiply all numbers in list
def mult_list(lst):
    # if empty list, return 0
    if len(lst) == 0:
        return 0
    #product starts with first element of list
    prod = lst[0]

    # go through list elements and multiply them together
    if len(lst) > 1:
        for i in lst[1:]:
            # lst[i:]: is skipping the first element
            prod = prod * i

    return prod

# Write a Python function called mult_list()  to multiply all the numbers in a list.
def mult_list(lst):
    #if empty list, return 0
    if len(lst) == 0:
        return 0
    #product starts with first element of list
    prod = lst[0]

    #go through list elements and multiply them together
    if len(lst) > 1:
        # lst[1:]: skips the first element of the list (to not multiply it by itself)
        for i in lst[1:]:
            prod = prod * i

    return prod
    
print(mult_list([1,2,3,100]))
print(mult_list([]))
print(mult_list([15]))

# Write python function with rev_string() to reverse a string
# start:stop:step
def rev_string(my_str):
    return my_str[::-1]

print(rev_string(""))
print(rev_string("apple"))
print(rev_string("the string"))

# Write function named num_within() to check whether a number falls within a given range
def num_within(x,a,b):
    # range is within a and b with x being the the value to see if it's within that range
    return x in range(a,b+1)
    # The b+1 part allows the end of the range to be inclusive.

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

# Python function called Pascal()
# Prints out the first row of Pascal's triangle
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)
pascal(50)