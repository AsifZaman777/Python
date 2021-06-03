def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
tri_recursion(6)

# Recursion Example Results
#                          start loop k 6
#                      start loop k 5
#                  start loop k 4
#              start loop k 3
#          start loop k 2
#      start loop k 1
# i reached when k = 0
#  end loop 0
#      i am k( 1 )+previous result( 0 )= 1
#      end loop 1
#          i am k( 2 )+previous result( 1 )= 3
#          end loop 2
#              i am k( 3 )+previous result( 3 )= 6
#              end loop 3
#                  i am k( 4 )+previous result( 6 )= 10
#                  end loop 4
#                      i am k( 5 )+previous result( 10 )= 15
#                      end loop 5
#                          i am k( 6 )+previous result( 15 )= 21
#                          end loop 6

# ----------->Visualize the code(Recursion)

# http://pythontutor.com/visualize.html#mode=display


print("\nFactorial : ")

def fact(k):
  if(k>0):
    result=k*fact(k-1)
    print(result)
  else:
    result=1
  return result
fact(7)
