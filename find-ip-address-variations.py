#Question:
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# For example:
# Given "25525511135" 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#Observations:
# 1. There are 3 periods in an IP address
# 2. Numeric value between periods do not exceed 255
# 3. # numeric digits between periods is no more than 3
# 4. IP address don't start with 0

#Source: http://www.cnblogs.com/zuoyuan/p/3768112.html
def ValidIPAddresses(s,sub,ips,ip):
    if sub == 4:  # IP address has 4 parts
        if s == '':
            ips.append(ip[1:])                          # remove first '.'
        return
    for i in range(1, 4): #subnet length is not more than 3                               
        if i <= len(s):                                 # if i > len(s), s[:i] will make false!!!!
            if int(s[:i]) <= 255:
                ValidIPAddresses(s[i:], sub+1, ips, ip+'.'+s[:i])
            if s[0] == '0': break                       # make sure that res just can be '0.0.0.0' and remove like '00'        
    return ips

series = ["192216811","25525511135"]
for ip in series:
    print(ip,"===> ", end="")
    print(ValidIPAddresses(ip,0,[],''))                 
