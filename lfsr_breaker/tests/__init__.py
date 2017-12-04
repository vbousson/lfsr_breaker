from unittest import TestCase

import lfsr_breaker


class TestFIBO(TestCase):
    def test_construction(self):
        s = lfsr_breaker.FibonacciLFSR(16, 42)
        self.assertTrue(isinstance(s, lfsr_breaker.FibonacciLFSR))
        self.assertTrue(isinstance(s, lfsr_breaker.BaseLFSR))

    def test_known_fibo_sequences(self):
        def test_one(L, mask, seed, result):
            s = lfsr_breaker.FibonacciLFSR(
                L, mask, seed).generate_n(len(result), str, "".join)
            if s != result:
                print(" Expected : {}".format(result))
                print("Generated : {}".format(s))
            self.assertTrue(s == result)
        big = 100
        all0 = "0" * big
        all1 = "1" * big

        test_one(1, 0, 0, all0)
        test_one(1, 0, 1, "1" + all0)
        test_one(1, 1, 0, all0)
        test_one(1, 1, 1, all1)

        test_one(2, 1, 1, "10" * big)
        test_one(2, 1, 2, "01" * big)
        test_one(2, 1, 3, all1)

        mask = 0b1011010100000001
        seed = 0b0011010101111010
        test_one(16, mask, seed, "0101111010101100000000110101011011010001010101100101111110101111100001001011100110100110001111011111")

    def tests_period_extractor(self):
        def test_one(L, mask, seed, res_prefix, res_loop):
            prefix, loop = lfsr_breaker.FibonacciLFSR(
                L, mask, seed).get_period(str, "".join)
            if (prefix, loop) != (res_prefix, res_loop):
                print(" Expected : {}[{}]".format(res_prefix, res_loop))
                print("Generated : {}[{}]".format(prefix, loop))
            self.assertTrue(prefix == res_prefix)
            self.assertTrue(loop == res_loop)

        test_one(1, 0, 0, "", "0")
        test_one(1, 0, 1, "1", "0")
        test_one(1, 1, 0, "", "0")
        test_one(1, 1, 1, "", "1")

        test_one(2, 1, 1, "", "10")
        test_one(2, 1, 2, "", "01")
        test_one(2, 1, 3, "", "1")

    def test_long_period(self):
        L = 8
        mask = 0b10101001
        seed = 0b10001011
        prefix, loop = lfsr_breaker.FibonacciLFSR(
            L, mask, seed).get_period(str, "".join)
        print("Prefix : {}".format(prefix))
        print("  Loop : {}".format(loop))
        print("Length of cycle : {}".format(len(loop)))
        self.assertTrue(len(prefix) == 0)
        self.assertTrue(len(loop) == 2**L - 1)

        prefix, loop = lfsr_breaker.FibonacciLFSR(
            L, mask, 0).get_period(str, "".join)
        self.assertTrue(len(prefix) == 0)
        self.assertTrue(len(loop) == 1)
        self.assertTrue(loop == "0")
