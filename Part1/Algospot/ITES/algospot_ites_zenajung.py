def ites(k,n):

    num = 1983
    #num_sum = 0


    sig_list = [0] * 0x400
    #signal = signal_generator()
    bp = 0
    tp = 0
    count = 0
    gen_count = 0
    pop_limit = 1024
    s = 0
    while gen_count < n:
        #s = sig_list[tp]-sig_list[bp]
        #print("i=%d, s=%d" % (genCount,s))
        if s<k:
            #print("+")
            #sig_list.append(signal.next())
            gen_count += 1
            #tp += 1
            tp = (tp+1) &  0x3FF

            #num_sum += num % 10000 + 1
            num = (num*214013 + 2531011) & 0xFFFFFFFF

            sig_list[tp] = num % 10000 + 1
            s += sig_list[tp]

        elif s>k:
            #print("-")
            #list.pop(0)
            #bp+=1
            s -= sig_list[bp]
            bp = (bp+1) & 0x3FF

        else:
            #print("=")
            count += 1
            #sig_list.append(signal.next())
            gen_count += 1
            #tp += 1
            tp = (tp+1) & 0x3FF
            #num_sum += num % 10000 + 1
            num = (num*214013 + 2531011) & 0xFFFFFFFF

            sig_list[tp] = num % 10000 + 1
            s += sig_list[tp]

    return count



if __name__ == '__main__':

    tc = int(raw_input())
    for i in xrange(tc):
        ln = raw_input()
        ln_list = ln.split()
        k = int(ln_list[0])
        n = int(ln_list[1])
        print(ites(k,n))



