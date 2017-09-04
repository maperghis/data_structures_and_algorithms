

class IntegerPairSum(cls):
    '''Given an integer array, output all the unique pairs that
    sum up to a specific value k'''

    def pair_sum1(cls, arr, k):
        '''My solution O(n^2)'''
        if len(arr) < 2:
            return 0
        pairs = []
        for index, num1 in enumerate(arr):
            new_arr = arr[:index] + arr[index+1:]
            for num2 in new_arr:
                if num1 + num2 == k:
                    new_tup = (min(num1, num2), max(num1, num2))
                    pairs.append(new_tup)
        return len(set(pairs))

    def pair_sum2(cls, arr, k):
        '''Better alogorithm O(n) linear'''
        if len(arr) < 2:
            return 0
        seen = set()
        output = set()
        for num in arr:
            target = k - num
            if target not in seen:
                seen.add(num)
            else:
                output.add((min(num, target), max(num, target)))
        return len(output)
