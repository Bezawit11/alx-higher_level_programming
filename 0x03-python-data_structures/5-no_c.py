#!/usr/bin/python3
def no_c(my_string):
   str1 = str(my_string)
   str1 = str1.translate({ ord("c"): None })
   str1 = str1.translate({ ord("C"): None })
   return str1
