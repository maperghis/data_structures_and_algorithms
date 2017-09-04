

class StringPermutation(object):
    '''Given a string, write a function that uses recursion to output a list of
    all the possible permutations of that string.
    For example, given s='abc' the function should return ['abc', 'acb', 'bac',
    'bca', 'cab', 'cba']
    '''

    def permute(cls, s):
        '''Solution'''
        if len(s) == 1:
            return s

        out = []
        for i, char in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [char + perm]
        return out
