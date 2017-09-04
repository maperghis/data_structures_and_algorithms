

class Anagram(object):

    def anagram1(cls, s1, s2):
        '''My solution using string indexes'''
        s1 = s1.replace(" ", "").lower()
        s2 = s2.replace(" ", "").lower()
        if len(s1) != len(s2):
            return False
        new_str = s1
        for char in s2:
            if char not in new_str:
                return False
            else:
                index = new_str.index(char)
                new_str = new_str[:index] + new_str[index+1:]
        return True

    def anagram2(cls, s1, s2):
        '''Given solution using sorted lists'''
        s1 = s1.replace(" ", "").lower()
        s2 = s2.replace(" ", "").lower()
        return sorted(s1) == sorted(s2)

    def anagram3(cls, s1, s2):
        '''Given solution using dictionary of counts'''
        s1 = s1.replace(" ", "").lower()
        s2 = s2.replace(" ", "").lower()
        if len(s1) != len(s2):
            return False
        count = {}
        for char in s1:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in s2:
            if char in count:
                count[char] -= 1
            else:
                count[char] = 1
        for k in count:
            if count[k] != 0:
                return False
        return True
