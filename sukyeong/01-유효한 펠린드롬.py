# "A man, a plan, a canal: Panama"
# "race a car"

class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        result = list(filter(lambda x: x.isalpha() == True or x.isdigit() == True, s))
        reverse_result = list(reversed(result))
        if result == reverse_result:
            return True
        else:
            return False
