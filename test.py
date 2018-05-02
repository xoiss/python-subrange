from subrange import subrange, subrangef


r = subrange(1, 5)          # subrange of integers 1..5

print r                     # 1..5
print r.min, r.max          # 1 5
print repr(r)               # subrange(1, 5)
print "{:04b}".format(r)    # 0001..0101
print 4 in r                # True
print [i for i in r]        # [1, 2, 3, 4, 5]
print r < 6                 # True

f = subrangef(0, 127,
              str_spec="0x{value:02X} {id!r}",  # format string
              id="ASCII_CHARSET",               # annotation
              brief="ASCII character codes")    # annotation

print f     # 0x00..7F 'ASCII_CHARSET'

print "{brief}: {min} to {max}".format(**f.__dict__)
# ASCII character codes: 0 to 127

raise SystemExit

###############################################################################

r = subrange(3, 12)
s = subrange(3, 12)
t = subrange(13, 18)

print r.min, r.max                  # 3 12

print repr(r)                       # subrange(3, 12)
print r                             # 3..12
print "{}".format(r)                # 3..12
print "0x{:02X}".format(r)          # 0x03..0C

print r == s, r != t                # True True
print t > s, s >= r                 # True True
print 2 < r < 13                    # True

print len(r)                        # 10
print r[6], r[-2]                   # 9 11

print [i for i in t]                # [13, 14, 15, 16, 17, 18]
print [i for i in reversed(t)]      # [18, 17, 16, 15, 14, 13]

print 7 in r                        # True

print

d = {r: 111, t: 222}
e = {r}

print d[r], d[s], d[t]              # 111 111 222
print r in e, s in e, t in e        # True True False

print

p = subrange(2, 2)                  # single-value subrange 2..2
q = subrange(8)                     # single-value subrange 8..8

print p == 2                        # True
print p >= 2, 7 < q <= 8            # True True

print int(p), int(q)                # 2 8
print bool(p)                       # True

d = {p: 111, q: 222}
e = {p, 8}

print d[p], d[2], d[q], d[8]        # 111 111 222 222
print 2 in e, q in e, 9 in e        # True True False

print

a = subrangef(2, 4, str_spec="{min}-{max}")

print a                             # 2-4
print "{}".format(a)                # 2-4
print "{:d}".format(a)              # 2..4

b = subrangef(2, 4, brief="B-subrange", name="B_SUBRANGE",
              str_spec="0x{value:04X} {brief!r}")

print b                             # 0x0002..0004 'B-subrange'
print "{}".format(b)                # 0x0002..0004 'B-subrange'
print "{:d}".format(b)              # 2..4

print "{value} <{name}>".format(**b.__dict__)  # 2..4 <B_SUBRANGE>

print a == b                        # True

raise SystemExit

###############################################################################

a = subrangef(10)
print a     # 10

b = subrangef(10, str_spec="{min}..{max}")
print b     # 10..10

c = subrangef(10, 20)
print c     # 10..20

d = subrangef(10, 20, str_spec="0x{value:04X}")
print d     # 0x000A..0014

e = subrangef(10, 20, str_spec="{value} {brief!r}",
              brief="my subrange")
print e     # 10..20 'my subrange'

f = subrangef(10, 20,
              str_spec="0b{value:06b} <{id}> -- {comm}",
              id="VALID_RNG",
              comm="valid range")
print f     # 0b001010..010100 <VALID_RNG> -- valid range

print "0x{:04X}".format(f)
# 0x000A..0014

print "{id}: 0x{value:04X}".format(**f.__dict__)
# VALID_RNG: 0x000A..0014

print "{id} = {value!r}".format(**f.__dict__)
# VALID_RNG = subrange(10, 20)

print "min of {comm} is {value.min}".format(**f.__dict__)
print "min of {comm} is {min}".format(**f.__dict__)
# min of valid range is 10

print

print "0x{:02X}".format(subrangef(10, 20))    # 0x0A..14
print "0x{:02X}".format(subrangef(10))        # 0x0A

r = subrangef(10, 20, str_spec="0x{value:04X}")
s = subrangef(10, 10, str_spec="0x{value:04X}")
print "{}".format(r)      # 0x000A..0014
print "{}".format(s)      # 0x000A

raise SystemExit

###############################################################################

print subrange(3, 12)     # subrange 3..12, contains 10 items
print subrange(-7, 4)     # subrange -7..4, contains 12 items
print subrange(2, 2)      # subrange 2..2, contains one item
print subrange(8)         # subrange 8..8, contains one item
print subrange(3, 12)
print subrange(8)
print subrange((3, 12))
print subrange([3, 12])
print subrange({'min': 3, 'max': 12})
print subrange(subrange(3, 12))
print

try:
    subrange()
    raise AssertionError()
except ValueError as e:
    print e     # initializer omitted
try:
    subrange(1, 2, 3)
    raise AssertionError()
except ValueError as e:
    print e     # too many initializers
try:
    subrange(dict(min=1))
    raise AssertionError()
except TypeError as e:
    print e     # initializing dictionary does not define 'max'
try:
    subrange(dict(max=1))
    raise AssertionError()
except TypeError as e:
    print e     # initializing dictionary does not define 'min'
try:
    subrange(dict(mmm=1))
    raise AssertionError()
except TypeError as e:
    print e     # initializing dictionary does not define 'max', 'min'
try:
    subrange((1,))
    raise AssertionError()
except TypeError as e:
    print e     # initializing 'tuple' contains 1 item(s), must be 2
try:
    subrange([1, 2, 3])
    raise AssertionError()
except TypeError as e:
    print e     # initializing 'list' contains 3 item(s), must be 2
try:
    subrange('a')
    raise AssertionError()
except TypeError as e:
    print e     # invalid limits: min='a', max='a'
try:
    subrange(1, 'a')
    raise AssertionError()
except TypeError as e:
    print e     # invalid limits: min=1, max='a'
try:
    subrange(dict(min='a', max=2))
    raise AssertionError()
except TypeError as e:
    print e     # invalid limits: min='a', max=2
try:
    subrange((10, 2))
    raise AssertionError()
except ValueError as e:
    print e     # reversed limits: min=10, max=2
print

#------------------------------------------------------------------------------

r = subrange(0)
r.myattr = 123   # Ok
try:
    r.min = 111      # exception is raised
    raise AssertionError()
except AttributeError as e:
    print e
print

try:
    del r.myattr2     # exception is raised
    raise AssertionError()
except AttributeError as e:
    print e
try:
    del r.min        # exception is raised
    raise AssertionError()
except AttributeError as e:
    print e
print

print repr(subrange(1, 2))    # subrange(1, 2)
print repr(subrange(3))       # subrange(3, 3)
print

print str(subrange(1, 2))    # 1..2
print str(subrange(3))       # 3
print

print "0x{:02X}".format(subrange(10, 20))     # 0x0A..14
print "0x{:02X}".format(subrange(10))         # 0x0A
print "{}".format(subrange(10, 20))           # 10..20
print "{}".format(subrange(10))               # 10
print

print hash(subrange(1, 2)) == hash(subrange(1, 2))    # True
print hash(subrange(1, 2)) == hash(subrange(1, 3))    # False
print hash(subrange(3, 3)) == hash(3)     # True
print hash(subrange(3, 3)) == hash(3.0)   # True
print

r = subrange(3, 12)
s = subrange(3, 12)
t = subrange(13, 18)

d = {r: 111, t: 222}
e = {r}

print d[r], d[s], d[t]            # 111, 111, 222
print r in e, s in e, t in e      # True, True, False

p = subrange(2)
q = subrange(8)

d = {p: 111, 8: 222}
e = {p, 8}

print d[p], d[2], d[q], d[8]      # 111, 111, 222, 222
print 2 in e, q in e, 9 in e      # True, True, False

print

print subrange(1, 2) == subrange(1, 2)    # True
print subrange(1, 2) == subrange(1, 3)    # False
print subrange(3, 3) == 3         # True
print subrange(3, 3) == 3.0       # True
print 3 == subrange(3, 3)         # True
print subrange(3, 4) == 3         # False
print subrange(3, 4) == '3..4'    # False
print

print subrange(1, 2) != subrange(1, 2)    # False
print subrange(1, 2) != subrange(1, 3)    # True
print subrange(3, 3) != 3         # False
print subrange(3, 3) != 3.0       # False
print 3 != subrange(3, 3)         # False
print subrange(3, 4) != 3         # True
print subrange(3, 4) != '3..4'    # True
print

print subrange(1, 2) < subrange(3, 4)     # True
print subrange(1, 2) < 3                  # True
print subrange(1, 2) < 2.5                # True
print 3 > subrange(1, 2)                  # True
print subrange(1, 2) < subrange(2, 4)     # False
print subrange(1, 3) < subrange(2, 4)     # False
print subrange(2, 3) < subrange(1, 4)     # False
print subrange(1, 2) < 2                  # False
print 2 > subrange(1, 2)                  # False
print

print subrange(3, 4) > subrange(1, 2)     # True
print subrange(1, 2) > 0                  # True
print subrange(1, 2) > 0.5                # True
print 0 < subrange(1, 2)                  # True
print subrange(2, 4) > subrange(1, 2)     # False
print subrange(2, 4) > subrange(1, 3)     # False
print subrange(1, 4) > subrange(2, 3)     # False
print subrange(1, 2) > 1                  # False
print 1 < subrange(1, 2)                  # False
print

print subrange(1, 2) <= 2                 # False
print subrange(1, 2) <= subrange(2, 2)    # False
print subrange(1, 2) <= subrange(2, 3)    # False
print

print subrange(1, 2) >= 1                 # False
print subrange(1, 2) >= subrange(1, 1)    # False
print subrange(1, 2) >= subrange(0, 1)    # False
print

print int(subrange(3, 3))     # 3
try:
    print int(subrange(1, 2))     # raises exception
    raise AssertionError()
except TypeError as e:
    print e
print

print bool(subrange(0, 0))    # False
print bool(subrange(0, 1))    # True
print bool(subrange(1, 1))    # True
print

print len(subrange(3, 12))    # 10
print len(subrange(-7, 4))    # 12
print len(subrange(2, 2))     # 1
print len(subrange(8))        # 1
print

print subrange(3, 12)[0]      # 3
print subrange(3, 12)[1]      # 4
print subrange(3, 12)[9]      # 12
print subrange(3, 12)[-1]     # 12
print subrange(3, 12)[-2]     # 11
print

print [i for i in subrange(3, 5)]     # [3, 4, 5]
print [i for i in subrange(3)]        # [3]
print

print [i for i in reversed(subrange(3, 5))]   # [5, 4, 3]
print [i for i in reversed(subrange(3))]      # [3]
print

print 3 in subrange(3, 5)         # True
print 4 in subrange(3, 5)         # True
print 6 in subrange(3, 5)         # False
print 3.75 in subrange(3, 5)      # True
print 5.0 in subrange(3, 5)       # True
print
