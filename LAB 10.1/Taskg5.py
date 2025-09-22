#refactor the code below to use list comprehension instead of a for loop.
import time
start_time = time.time()# refactored code following PEP 8 guidelines.
nums = [i for i in range(1,1000000)]
squares = [n**2 for n in nums]#using list comprehension to create a list of squares.
print(len(squares))
end_time = time.time()
print("Execution Time:", end_time - start_time)
