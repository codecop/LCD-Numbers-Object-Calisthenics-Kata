# LCD Numbers

## Requirements

Write a program that creates an LCD string representation of any integer value 
    using a 4x7 grid of space each, 
using minus and pipe characters for each digit. 
The bar size should be adjustable. 
The default value is 2

## Thoughts

Each digit has 7 elements.

* 1 pixel left |, center part (scaleable), 1 pixel right |
* top/middle/bottom line (scaleable), only contains "-"
* the crossings are allways 1x1 and empty

There are any number of digits next to each other.
Printing is line by line, so lines need to be concatinated.

Column is minimum 5.
Printing will be
* 1st line
* n times 2nd line
* 3rd line
* n times 4th line
* 5th line

Line is minimum 3.
First column will be
* 1st entry = empty 
* n times 2nd entry = empty or "|"
* last entry = empty

So a digit ideal for scaling is
1) empty, bar(y/n) scaled, empty
2) pipe(y/n), empty scaled, pipe(y/n)
again 2) for scaling  
another 1)
another 2)
again 2) for scaling  
another 1)

Everything must be return line by line for printing.

class HoricontalBar = 1) 
class VerticalBar = Pipes and empty

## Findings

* Size knows the number something has to loop but it cannot
  do the looping over Strings or lines because they are primitive.
  So it needs to export a loop construct.

* In Java I can escape the getters with tricks like equals or 
  Iterable which do not look like getting.

## Times

* Analyse the problem ... 30'
* Code the infrastructure, LcdDigit, Digit, Lookup, all but main ... 2h'
* Main (not working) - started hacking ... 30'
* Create further elements like `Number` and `LcdNumber` which are first class collections and 
  contain looping code. Original Main would have worked, used wrong API. - 1h15'

Total Kata 4h
