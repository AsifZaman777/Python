# When an assert statement is failed, an Assertion Error is raised.
# Let's take an example to understand the assertion error. Let's say you have two variables a and b,
# which you need to compare. To check whether a and b are equal or not, you apply an assert keyword before that,
# which will raise an Assertion exception when the expression will return false.

# assert() ----> comparing two values
var1 = input()
var2 = input()
try:
    assert var1==var2
except:
    print("They are not similar")
else:
    print("They are similar ")

