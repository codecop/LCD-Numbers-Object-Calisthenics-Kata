# LCD Numbers Kata Object Calisthenics with PMD Check

This is a template for the [LCD Numbers Kata](http://rubyquiz.com/quiz14.html).
This is an [Apache Maven](https://maven.apache.org/) project. Run `mvnw test` to
run your tests. [JUnit](http://junit.org/) and [Mockito](http://site.mockito.org/)
are provided as dependencies.

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

There are sample LCD outputs in the `src/test/resources` folder.

## Constraints

[Jeff Bay's Object Calisthenics](https://williamdurand.fr/2013/06/03/object-calisthenics/).

1. Only One Level Of Indentation Per Method.
1. Don't Use The `else` Keyword.
1. Wrap All Primitives And Strings.
1. One Dot/Arrow (dereference) Per Line.
1. Don't Abbreviate (long names). *)
1. Keep All Entities Small. (50 lines of code per class)
1. Not More Than Two Instance Variables.
1. First Class Collections.
1. No Getters/Setters/Properties.

\*) rule not enforced.

### Checking Code for Compliance

The [Code Cop Custom PMD Rules](https://bitbucket.org/pkofler/pmd-rules) contain PMD rules to check code for compliance with Object Calisthenics.
This project is set up to check the code using the Maven PMD Plugin on each `mvnw test`.

To check the setup run `mvnw test` on the sample code. It will show two violations:

    [INFO] PMD Failure: SampleClass.java:2 Rule:TooManyFields Priority:3 Too many fields.
    [INFO] PMD Failure: SampleClass:9 Rule:NoElseKeyword Priority:3 No else keyword.

You can also check the rules on their own with `mvnw pmd:check`.
By using the [Maven Shell](https://github.com/jdillon/mvnsh) the time to run the check can be reduced by 50%.

### Limitations of Checking Code

Obviously code analysis cannot find everything.
For example the `PrimitiveObsession` rule (Wrap All Primitives And Strings) allows primitive values in constructors and getters because they are needed to implement [Value Objects](http://martinfowler.com/bliki/ValueObject.html).
On the other hand these getters are getters, so `NoGetterAndSetter` will flag them.
Rule #4 (One Dot Per Line) is checked using PMD's own `LawOfDemeter`, which checks for the [Law Of Demeter](http://www.ccs.neu.edu/home/lieber/LoD.html). Now the LoD is not about counting dots per line, it is about used types.
So sometimes a single dot in a line will already violate the LoD.
Finally it is very difficult to check for abbreviations, so rule #5 is not enforced.

You can use `// NOPMD` comments and `@SuppressWarnings("PMD")` annotations to suppress false positives.
I recommend using exact suppressions, e.g. `@SuppressWarnings("PMD.TooManyFields")` to skip issues because other issues at the same line will still be found. Use your good judgement. The goal of this exercise is to follow all nine rules, not to suppress them.

See my blog post about [Object Calisthenics and how to enforce it](https://blog.code-cop.org/2018/01/compliance-with-object-calisthenics.html) for more details.
