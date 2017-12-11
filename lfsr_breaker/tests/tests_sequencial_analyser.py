from unittest import TestCase

import lfsr_breaker
import random

random.seed("toto");

def analyseAndGetNext(seq, expected):
    print("Input sequence : '{}', expected follow-up : '{}'".format(seq, expected))
    analyser = lfsr_breaker.LFSRAnalyser(seq)
    f = analyser.getInitialFiboLFSR()
    initialSeq = f.generate_n(len(seq), str, "".join)
    if initialSeq != seq:
        print("Not valid with command, first seqence generated is : {}".format(initialSeq))
        return False
    generated = f.generate_n(len(expected), str, "".join)
    if expected != generated:
        print("Wrong guess, generated follow-up : {}".format(generated))
        return False
    return True


def generateRandomLFSRTestSequence():
    L = random.randint(1,512)
    mask = random.randint(1,2**L-1) | 1;
    seed = random.randint(1,2**L-1)
    print (L, mask, seed)

    lfsr = lfsr_breaker.FibonacciLFSR(L, mask, seed);
    n = random.randint(L*2,L*10)
    known = lfsr.generate_n(n, str, "".join)
    m = random.randint(L*100, L*200)
    expected = lfsr.generate_n(m, str, "".join)
    return known, expected

class TestSequence(TestCase):
    def testTrivialSequences(self):
        big = 10
        self.assertTrue(analyseAndGetNext("0", "0"*big))
        self.assertTrue(analyseAndGetNext("0"*big, "0"*big))
        self.assertTrue(analyseAndGetNext("1"*big, "1"*big))

    def testRandomSequences(self):
        for i in range(5):
            print ("Test {} :".format(i+1))
            known, expected = generateRandomLFSRTestSequence();
            self.assertTrue(analyseAndGetNext(known, expected))




