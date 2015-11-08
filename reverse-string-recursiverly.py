#Reverse a string recursively

input = 'Hello World!'

def reverse(input, result):
    if ( len(input) == 1):
        return result + input
    result += input[-1]
    result = reverse(input[:-1],result)
    return result

result = reverse(input,"")
print(input , " ==> ", result)


