from .fibonacci_lfsr import FibonacciLFSR

def toInt(v):
    return 0 if v == [] else v[0] + 2*toInt(v[1:])

def BerlekampMassey(entry):
    n = len(entry)
    s = [int(entry[i]) for i in range(n)]
    b = [1] + [0]*(n-1)
    c = [1] + [0]*(n-1)
    L = 0
    m = -1
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

    if L == 0:
        L = 1
    mask = toInt(c[L:0:-1])
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

