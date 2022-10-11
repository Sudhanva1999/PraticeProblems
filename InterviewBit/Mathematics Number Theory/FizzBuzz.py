# Given a positive integer A, return an array of strings with all the 
# integers from 1 to N. But for multiples of 3 the array should have
#  “Fizz” instead of the number. For the multiples of 5, the array 
#  should have “Buzz” instead of the number. For numbers which are 
#  multiple of 3 and 5 both, the array should have “FizzBuzz” instead 
#  of the number.
def fizzBuzz(A):
        resArr = []
        i = 1 
        while(i <= A):
            if(i % 15 == 0):
                resArr.append("FizzBuzz")
            elif(i % 3 == 0):
                resArr.append("Fizz")
            elif(i % 5 == 0):
                resArr.append("Buzz")
            else:
                resArr.append(i)
            i += 1
        return resArr
print(fizzBuzz(int(input("Enter a number to find fizz buzz array\n"))))