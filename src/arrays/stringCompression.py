

class StringCompression(object):
    '''Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become
    'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of
    single or double letters. For instance, it is okay for 'AAB' to return
    'A2B1' even though this technically takes more space.'''

    def compress(cls, s):
        result = ""
        length = len(s)

        if len(s) == 0:
            return ""

        if len(s) == 1:
            return s[0] + "1"

        i = 1
        count = 1

        while i < length:
            if s[i] == s[i - 1]:
                count += 1
            else:
                result = result + s[i - 1] + str(count)
                count = 1
            i += 1
        result = result + s[i - 1] + str(count)
        return result
