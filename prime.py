import math

#source: https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
def get_primes(input_list):
    result_list = list()
    for element in range(len(input_list)):
        if is_prime(input_list[element]):
            result_list.append(input_list[element])

    return result_list

# or better yet...

def get_primes2(input_list):
    return (element for element in input_list if is_prime(element))

# not germane to the example, but here's a possible implementation of
# is_prime...

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

input = [3,4,8,15,25,11,55]
print("input ====>", input)
print("primes ===>", get_primes(input))
