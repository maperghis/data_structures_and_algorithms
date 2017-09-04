

class UniqueCharacters(object):
    '''Given a string,determine if it is compreised of all unique characters.
    For example, the string 'abcde' has all unique characters and should
    return True. The string 'aabcde' contains duplicate characters and should
    return false.'''

    def unique_chars(cls, s):
        '''My solution using sets'''
        return len(set(s)) == len(s)

    def unique_chars2(cls, s):
        '''Alternative solution'''
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
            else:
                return False
        return True
