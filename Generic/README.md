# LCD Numbers Kata Object Calisthenics (without Check)

This is a generic template for the [LCD Numbers Kata](http://rubyquiz.com/quiz14.html).

## Requirements (copied from Ruby Quiz)

Write a program that creates an LCD string representation of an integer value
using a 4x7 grid of space each, using minus and pipe characters for each digit.
Each digit is shown below:

     --      --  --      --  --  --  --  --
    |  |   |   |   ||  ||   |      ||  ||  |
    |  |   |   |   ||  ||   |      ||  ||  |
             --  --  --  --  --      --  --
    |  |   ||      |   |   ||  |   ||  |   |
    |  |   ||      |   |   ||  |   ||  |   |
     --      --  --      --  --      --  --

The bar size should be adjustable. The default value is 2 - as shown above.
Read more about it at [RubyQuiz](http://rubyquiz.com/quiz14.html).

There are sample LCD outputs in the `test/resources` folder.

## Constraints

[Jeff Bay's Object Calisthenics](https://williamdurand.fr/2013/06/03/object-calisthenics/).

1. Only One Level Of Indentation Per Method.
1. Don't Use The `else` Keyword.
1. Wrap All Primitives And Strings.
1. One Dot/Arrow (dereference) Per Line.
1. Don't Abbreviate (long names).
1. Keep All Entities Small. (50 lines of code per class)
1. Not More Than Two Instance Variables.
1. First Class Collections.
1. No Getters/Setters/Properties.
