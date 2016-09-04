class Palindrome:

    @staticmethod
    def is_palindrome(text):
        x = 0
        while x < len(text):
            if ord(text[x]) > 122 or ord(text[x]) < 65 or ( ord(text[x])  < 97 and ord(text[x])  > 90 ):
                text = text[:x] + text[x+1:]
            else:
                x += 1
        length = len(text)
        i = 0
        flag = False
        while i < length//2:
            a = text[i]
            b = text[length-i-1]
            if ord(text[i]) > 96:
                if ord(text[i]) == ord(text[length-i-1]) or ord(text[i])-32 == ord(text[length-i-1]):
                    flag = True
                else:
                    return False
            elif ord(text[i]) < 96:
                if ord(text[i]) == ord(text[length-i-1]) or ord(text[i])+32 == ord(text[length-i-1]):
                    flag = True
                else:
                    return False
            i += 1
        return flag

print(Palindrome.is_palindrome('ABcd../,/DcBa'))
