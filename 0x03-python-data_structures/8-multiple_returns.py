#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
       tup = tuple((0, "")) 
    else:
        tup = tuple((len(sentence), sentence[0]))
    return tup
