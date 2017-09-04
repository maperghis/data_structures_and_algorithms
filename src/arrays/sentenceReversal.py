

class SentenceReversal(object):
    '''Given a string of words, reverse all the words, removing white spaces'''

    def rev_word(cls, s):
        '''My solution using built in split and array reveral'''
        return " ".join(s.split()[::-1])

    def rev_word2(cls, s):
        '''Solution without the built in split function'''
        words = []
        length = len(s)
        spaces = [' ']
        i = 0
        while i < length:
            if s[i] not in spaces:
                word_start = i
                while i < length and s[i] not in spaces:
                    i += 1
                words.append(s[word_start:i])
            i += 1
        return " ".join(words[::-1])
