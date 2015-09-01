__author__ = 'markers'
# -*- coding: utf-8 -*-

'''
참조 : http://book.algospot.com/19-7.html
'''


'''
신호생성 1
'''
def signal_generator(n_length):
    a = [1983]
    signal = list()

    for index in xrange(n_length):
        a.append( (a[index] * 214013 + 2531011) % 2**32 )
        signal.append( int(a[index] % 10000 + 1) )
        #print signal[index]

    return signal

'''
신호생성2
'''
class signalGenerator():

    def __init__(self):
        self.a = 1983
        self.signal = 0

    def next(self):
        self.signal = self.a % 10000 + 1
        self.a = ( self.a * 214013 + 2531011 ) % 2**32
        return self.signal



def signal_generator2(n_length):
    a = [1983]
    signal = list()

    for index in xrange(n_length):
        a.append( (a[index] * 214013 + 2531011) % 2**32 )
        signal.append( int(a[index] % 10000 + 1) )
        #print signal[index]

    return signal


'''
단순 알고리즘
'''
def generator1(k_sum, signal):
    ret = 0
    for head_index in xrange(len(signal)):
        sum = 0
        #for tail in enumerate(signal, start=signal.index(head)):
        for tail_index in xrange(head_index, len(signal)):
            sum += signal[tail_index]
            if sum == k_sum:
                ret += 1
            elif sum > k_sum:
                break

    return ret



'''
오프라인알고리즘
'''
def generator2(k_sum, signal):
    #ret = 0,  range_sum = signal[0], tail_index = 0
    ret, range_sum, tail_index = 0, signal[0], 0
    for head_index in xrange(len(signal)):

        while range_sum < k_sum and tail_index + 1 < len(signal):
            tail_index += 1
            range_sum += signal[tail_index]

        if range_sum == k_sum:
            ret += 1
        range_sum -= signal[head_index]

    return ret


'''
온라인알고리즘
'''
def generator3(k_sum, n_length):

    signal = signalGenerator();
    ret, range_sum = 0, 0

    queue = []

    for index in xrange(n_length):

        new_signal = signal.next()
        range_sum += new_signal
        queue.insert(0, new_signal)

        while range_sum > k_sum:
            range_sum -= queue.pop()

        if range_sum == k_sum:
            ret += 1

    return ret



if __name__ == "__main__":
    testCase = int(raw_input())
    for index in xrange(testCase):
        k_sum, n_length = map(int, raw_input().split())
        signal = signal_generator(n_length)
        #print generator2(k_sum, signal)
        print generator3(k_sum, n_length)


