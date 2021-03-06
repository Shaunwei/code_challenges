# coding=utf-8
"""http://projecteuler.net/problem=027

Quadratic primes

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula n² - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

Solution by jontsai <hello@jontsai.com>
"""
from utils import *

# a = -61, b = 971
EXPECTED_ANSWER = -59231

limit = 1000

max_consecutive_primes = 0
best_a = 0
best_b = 0

primes_below_limit = generate_primes(limit)[:]

# initial bounds:
# -1000 < a < 1000
# -1000 < b < 1000
#
# Initial search space is O(1999 * 1999)
# Or approximately O(2000 * 2000)
#
# However, b must be positive and odd, since:
# When n = 0:
#   n^2 + an + b
#   (0)^2 + a * 0 + b = b
#
# Now, search space has been reduced to O(2000 * 500)
#
# Let b be odd
# Suppose a is even
# When n is even:
#   n^2 + an + b
#   (even * even) + (even * even) + odd
#   even + even + odd = odd
#
# When n is odd:
#   (odd * odd) + (even * odd) + odd
#   odd + even + odd = even
#
# So when a is even:
# the most consecutive primes that can be generated is 2 (n = 0, n = 1)
#
# So a must be odd
# Now, search space has been reduced to O(1000 * 500)

for a in xrange(-limit + 1, limit, 2):
    for b in primes_below_limit:
        unbroken_prime_chain = True
        n = 0
        consecutive_primes = 0
        while unbroken_prime_chain:
            candidate = n * n + a * n + b
            if not is_prime(candidate):
                unbroken_prime_chain = False
            else:
                consecutive_primes += 1
            n += 1
        if consecutive_primes > max_consecutive_primes:
            max_consecutive_primes = consecutive_primes
            best_a = a
            best_b = b

print str(best_a), str(best_b), max_consecutive_primes 

answer = best_a * best_b

print 'Expected: %s, Answer: %s' % (EXPECTED_ANSWER, answer)
