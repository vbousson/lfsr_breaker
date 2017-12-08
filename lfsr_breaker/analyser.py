from .fibonacci_lfsr import FibonacciLFSR

def toInt(v):
    return 0 if v == [] else v[0] + 2*toInt(v[1:])

def BerlekampMassey(entry):
    # 1.
    n = len(entry)
    s = [int(entry[i]) for i in range(n)]

    # 2.
    b = [1] + [0]*(n-1)
    c = [1] + [0]*(n-1)

    # 3.
    L = 0
    m = -1

    # 4.
    for N in range(n):
        d = sum([c[i]*s[N-i] for i in range(L+1)]) % 2

        if d == 0:
            #Ok
            pass
        else:
            t = [e for e in c]

            for i in range(n-N+m):
                c[N-m+i] ^=  b[i]

            if L <= N/2:
                L = N + 1 - L
                m = N
                b = [e for e in t]

    #print(L)
    if L == 0:
        L = 1
    #print(c)
    #print(b)
    #print(s)
    mask = toInt(c[:L][::-1])
    seed = toInt(s[:L])
    return L, mask, seed

class LFSRAnalyser:
    def __init__(self, seq):
        self.m_input = seq
        self.m_res = BerlekampMassey(seq)
        print("Analyse output : ", self.m_res)

    def getInitialFiboLFSR(self):
        L, mask, seed = self.m_res
        return FibonacciLFSR(L, mask, seed)

