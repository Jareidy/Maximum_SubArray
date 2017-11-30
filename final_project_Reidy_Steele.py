import unittest
import random
import time


class msa_pricing:

    def msa_brute_force(self, pricelist):
        msa_max = 0
        for i in range(len(pricelist)):
            current_price = pricelist[i]-pricelist[0]
            for x in range(i, len(pricelist)):
                sum = (pricelist[x]-pricelist[0]) - current_price
                if sum > msa_max:
                   msa_max = sum
        return msa_max


class MSATest(unittest.TestCase):
    timer = []
    test_type = []

    def setUp(self):
        self.msa = msa_pricing()

    def test_msa_bruteforce_fixed(self):
        pricelist = [100, 98, 102]
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertEqual(msa_max, 4)

    def test_msa_bruteforce_random_5(self):
        pricelist = [100]
        for x in range(5):
            pricelist.append(random.randint(50, 150))
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertIsNot(msa_max, 0)

    def test_msa_bruteforce_random_500(self):
        start_time = time.time()
        pricelist = [100]
        for x in range(500):
            pricelist.append(random.randint(50, 150))
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Brute force random 500")
        self.timer.append(time.time() - start_time)

    def test_msa_bruteforce_random_1000(self):
        start_time = time.time()
        pricelist = [100]
        for x in range(1000):
            pricelist.append(random.randint(50, 150))
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Brute force random 1000")
        self.timer.append(time.time() - start_time)

    def test_msa_bruteforce_random_1500(self):
        start_time = time.time()
        pricelist = [100]
        for x in range(1500):
            pricelist.append(random.randint(50, 150))
        msa_max = self.msa.msa_brute_force(pricelist)
        self.assertIsNot(msa_max, 0)
        self.test_type.append("Brute force random 1500")
        self.timer.append(time.time() - start_time)

    def runtimes(self):
        for i in range(len(self.timer)):
            print(self.test_type[i])
            print(self.timer[i])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
