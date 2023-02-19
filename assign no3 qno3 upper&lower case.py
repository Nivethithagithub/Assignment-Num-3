# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def string_test(s):
    t={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           t["UPPER_CASE"]+=1
        elif c.islower():
           t["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", t["UPPER_CASE"])
    print ("No. of Lower case Characters : ", t["LOWER_CASE"])

string_test('Information Technology')
