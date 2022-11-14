#!/bin/python

import math

# Evaluate expression shown on the tv as an integer
result = int( math.pow(2, 38) )

# Add the result to the url and display
url = f"http://www.pythonchallenge.com/pc/def/{result}.html"
print(url)
with open('output', 'w') as file: file.write(url)
