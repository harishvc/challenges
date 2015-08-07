#Question: Say as you see. Example an input 123 will read One 1 One two One three and will generate an output 111213 

input = ["123", "21"]
tmp = ""
output = []
for x in input:
    times = 0
    result = ""
    tmp = ""
    for i in x:
        if len(tmp) == 0: #New character, first time
            tmp = i
            times = 1
            continue
        elif tmp == i:  #New character same as last character
            times += 1
            continue
        else: #New character not same a last character
            result += str(times) + tmp
            tmp = i
            times = 1
    result += str(times) + tmp #Last character
    output.append(result)
print(input)
print(output)