input

def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("please enter palindrome"))
if(is_palindrome(a)==True):
    print("Given palindrome is true")
else:
    print("Given palindrome is false!")
    
    output
    please enter palindrome12321
Given palindrome is true
