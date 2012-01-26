import math
import time
import sys

IPS = 10 ** 9 # instructions per second

if len(sys.argv) > 1:
    IPS = int(sys.argv[1])

N_VALUES = (10, 20, 30, 100, 1000, 10 ** 6, 10 ** 9)

def pretty_format(t):
    # turn it into miliseconds initially
    t *= 1000
    if t < 0.01: return '~0'
    if t < 1: return '%.2f ms.' % t
    # miliseconds
    if t < 1000: return '%d ms.' % int(t)
    # seconds
    t /= 1000
    if t < 60: return '%d sec.' % int(t)
    # minutes 
    t /= 60
    if t < 60: return '%d min.' % int(t)
    # hours
    t /= 60
    if t < 24: return '%d hour(s)' % int(t)
    # days
    t /= 24
    if t < 30: return '%d day(s)' % int(t)
    # months
    t /= 30
    if t < 12: return '%d month(s)' % int(t)
    # year 
    t /= 12
    if t < 1000: return '%d year(s)' % int(t)
    return '%e year(s)' % t
        

def benchmark(name, f):
    print
    print name.upper()
    print '=' * len(name)
    print
    print 'n value\t\ttime:'
    print '----------\t-----'
    for n in N_VALUES:
        start = time.time()
        t = f(n) / float(IPS)
        print "%10d\t%s" % (n, pretty_format(t))
        if t > 60 * 60 * 24 * 30 * 12 * 1000:
            break
    print

if __name__ == '__main__':
    benchmark('constant', lambda n: 1)
    benchmark('log', lambda n: math.log(n, 2)),
    benchmark('sqw_root', lambda n: n ** 0.5),
    benchmark('linear', lambda n: n),
    benchmark('n-log n', lambda n: n * math.log(n, 2)),
    benchmark('square', lambda n: n ** 2),
    benchmark('cubic', lambda n: n ** 3),
    benchmark('exponential', lambda n: 2 ** n),
    benchmark('factorial', lambda n: math.factorial(n)),


