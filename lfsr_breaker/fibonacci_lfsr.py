# Fibonacci LFSR structure

# Exemple of a LFSR of size 8
#    +----+   +----+   +----+   +----+   +----+   +----+   +----+   +----+
#    |    |   |    |   |    |   |    |   |    |   |    |   |    |   |    |
# +--> a7 +---> a6 +-+-> a5 +---> a4 +---> a3 +---> a2 +---> a1 +-+-> a0 +-+---->
# |  |    |   |    | | |    |   |    |   |    |   |    |   |    | | |    | |
# |  +----+   +----+ | +----+   +----+   +----+   +----+   +----+ | +----+ |
# |          m7=0    |m6=1     m5=0     m4=0     m3=0     m2=0    |m1=1    |m0=1
# |                  v                                            v        |
# +-----------------xor<-----------------------------------------xor<------+

# L = 8
#  mask = base2(m7m6m5m4m3m2m1m0)
# state = base2(a7a6a5a4a3a2a1a0)


class TrivialFibonacciLFSR(object):
  def checkRange(self, v):
    assert(0 <= v < 2**self.m_L)

  def __init__(self, L, mask, seed = 0):
    self.m_L = L
    self.checkRange(mask)
    self.m_mask = mask
    self.checkRange(seed)
    self.m_state = seed

  def next(self):
    lsb = self.m_state % 2
    def chained_xor(v):
        return 0 if v == 0 else (v % 2) ^ chained_xor(v >> 1)
    new_msb = chained_xor(self.m_state & self.m_mask)
    self.m_state = (new_msb << (self.m_L - 1)) | (self.m_state >> 1)
    self.checkRange(self.m_state)
    return lsb


