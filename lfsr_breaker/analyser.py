from .fibonacci_lfsr import FibonacciLFSR

def toInt(v):
    return 0 if v == [] else v[0] + 2*toInt(v[1:])

class BMLFSRAnalyser:
    def __init__(self):
        init_s = []
        init_b = [1]
        init_c = [1]
        init_L = 0
        init_m = -1
        init_count = 0
        self.m_state = (init_s, init_b, init_c, init_L, init_m, init_count)

    def getCurrentInitialFiboLFSRParams(self):
        (s,_,c,L,_,_) = self.m_state
        L = max(L,1)
        mask = toInt(c[L:0:-1])
        seed = toInt(s[:L])
        return L, mask, seed

    def getConfidenceIndex(self):
        (s,_,_,_,_,count) = self.m_state
        return count / len(s)

    @staticmethod
    def nextState(state, bit):
        (s,b,c,L,m,count) = state
        s += [bit]
        b += [0]
        c += [0]
        N = len(s) - 1
        d = sum([c[i]*s[N-i] for i in range(L+1)]) % 2
        if d == 0:
            count += 1
        else:
            t = c[:]
            for i in range(m):
                c[N-m+i] ^= b[i]
            if L <= N/2:
                L = N+1-L
                m = N
                b = t[:]
            count = 1
        return (s,b,c,L,m,count)

    def processBit(self, b):
        self.m_state = BMLFSRAnalyser.nextState(self.m_state, int(b,2))

    def processSequence(self, seq):
        for b in seq:
            self.processBit(b)


class LFSRAnalyser:
    def __init__(self, seq):
        self.m_input = seq
        analyser = BMLFSRAnalyser()
        analyser.processSequence(seq)
        self.m_res = analyser.getCurrentInitialFiboLFSRParams()
        print("Analyse output : ", self.m_res)

    def getInitialFiboLFSR(self):
        L, mask, seed = self.m_res
        return FibonacciLFSR(L, mask, seed)

