# -*- coding: UTF-8 -*-
import argparse
from sys import stdout

MAX_ITER = 1000000L


def collatz(n, maxiter=MAX_ITER):
    i = 1
    yield n
    while (n > 1 and i < maxiter):
        i += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        yield n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maxiter", help="maximum number of iterations", type=long, default=MAX_ITER)
    args = parser.parse_args()
    print "\n====Collatz sequence generator===="
    print "[MAX_ITER: %d]\n" % args.maxiter
    while True:
        try:
            n = int(raw_input("Input an integer value: "));
            if (n <= 0):
                raise ValueError("negative numbers are not allowed")
            break
        except ValueError as e:
            print "Invalid input value: {}\n".format(e)
    # print ' -> '.join([str(el) for el in collatz(n)])
    gen = collatz(n, args.maxiter)
    stdout.write("%d" % gen.next())
    for el in gen:
        stdout.write(" -> %d" % el)
    print "\ndone."


if __name__ == "__main__":
    main()
