## LCD Numbers Kata Object Calisthenics with Pylint Check ##

This is a template for the [LCD Numbers Kata](http://rubyquiz.com/quiz14.html).
This is a Python project. Run the script `./run_tests` to run your tests.

## Requirements (copied from Ruby Quiz) ##

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

## Constraints ##

[Jeff Bay's Object Calisthenics](http://williamdurand.fr/2013/06/03/object-calisthenics/).

1. Only One Level Of Indentation Per Method.
1. Don't Use The `else` Keyword.
1. Wrap All Primitives And Strings.
1. One Dot/Arrow (dereference) Per Line.
1. Don't Abbreviate (long names).
1. Keep All Entities Small. (50 lines of code per class)
1. Not More Than Two Instance Variables.
1. First Class Collections.
1. No Getters/Setters/Properties.

### Checking Code for Compliance ###

The project contains [Pylint](https://www.pylint.org/) rules to check code for compliance with Object Calisthenics'.
To check the setup run `./run_tests` on the sample code. It will run the tests and show two violations:

    ************* Module lcd.sample
    R:  1, 0: More than two instance variables in class "Sample" (more-than-two-instance-variables)
    R:  8, 8: Don't use the ELSE keyword (if-has-else)

You can also check the rules on their own with `./run_pylint`.

### Limitations of Checking Code ###
Obviously code analysis cannot find everything.
For example the `PrimitiveObsession` rule (Wrap All Primitives And Strings) allows primitive values in constructors and getters because they are needed to implement [Value Objects](http://martinfowler.com/bliki/ValueObject.html).
On the other hand these getters are getters, so `NoGetterAndSetter` will flag them.
Rule #4 (One Dot Per Line) is checked using PMD's own `LawOfDemeter`, which checks for the [Law Of Demeter](http://www.ccs.neu.edu/home/lieber/LoD.html). Now the LoD is not about counting dots per line, it is about used types.
So sometimes a single dot in a line will already violate the LoD.
Finally it is very difficult to check for abbreviations, so rule #5 is not enforced.

You can use `# pylint: disable=<rule name>` comments to suppress false positives.
I recommend using this rarely. Use your good judgement. The goal of this exercise is to follow all nine rules, not to suppress them.

See my blog post about [Object Calisthenics and how to enforce it](http://blog.code-cop.org/2018/01/compliance-with-object-calisthenics.html) for more details.

### License ###
This work is licensed under a [New BSD License](http://opensource.org/licenses/bsd-license.php), see `license.txt` in repository.
