from unittest import TestCase

import lfsr_breaker

class TestSequence(TestCase):
    def testTrivialSequences(self):
        def analyse_and_get_next(seq, expected):
            print("Input sequence : '{}', expected follow-up : '{}'".format(seq, expected))
            analyser = lfsr_breaker.LFSRAnalyser(seq)
            f = analyser.getInitialFiboLFSR()
            initialSeq = f.generate_n(len(seq), str, "".join)
            if initialSeq != seq:
                print("Not valid with command, first seqence generated is : {}".format(initialSeq))
            self.assertTrue(initialSeq == seq)
            generated = f.generate_n(len(expected), str, "".join)
            if expected != generated:
                print("Wrong guess, generated follow-up : {}".format(generated))
            self.assertTrue(expected == generated)
            print("OK")

        big = 10
        analyse_and_get_next("0", "0"*big)
        analyse_and_get_next("0"*big, "0"*big)
        analyse_and_get_next("1"*big, "1"*big)

