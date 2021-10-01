#!/usr/bin/env python3
import numpy

try:                                                                                #Error handling  
    x = input("Please enter the value of x:")                                       #Ask for x value
    y = input("Please enter the value of y:")                                       #Ask for y value
    print("The value of x raised to the power of y is:",float(x)**float(y))
    print("The log of x is:",numpy.log2(float(x)))
    print("My student id is: 0077808")
except ValueError as e:
    print("Please only input numbers")                                              #Crash message
except KeyboardInterrupt as e:
    print("\n(×_×)")                                                                #Poor little program it was just doing it's job
except:
    print("Ouch! you broke the universe!")                                          #Quite dead isn't it
