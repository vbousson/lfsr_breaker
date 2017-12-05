from .fibonacci_lfsr import FibonacciLFSR

def solve(entry):
  return 1, 0, 0

class LFSRAnalyser:
    def __init__(self, seq):
        self.m_input = seq
        self.m_res = solve(seq)

    def getInitialFiboLFSR(self):
        L, mask, seed = self.m_res
        return FibonacciLFSR(L, mask, seed)

