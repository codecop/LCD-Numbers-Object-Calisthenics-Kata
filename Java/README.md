## LCD Numbers Kata Object Calisthenics with PMD Check ##

This is a template for the [LCD Numbers Kata](http://rubyquiz.com/quiz14.html).
The language is Java with JUnit.

### Constraints ###

[Jeff Bay's Object Calisthenics](http://williamdurand.fr/2013/06/03/object-calisthenics/).

1. Only One Level Of Indentation Per Method.
1. Don't Use The `else` Keyword.
1. Wrap All Primitives And Strings.
1. First Class Collections.
1. One Dot/Arrow (dereference) Per Line.
1. Don't Abbreviate (long names).
1. Keep All Entities Small. (50 lines of code per class)
1. Not More Than Two Instance Variables.
1. No Getters/Setters/Properties.

### Checking Code for Compliance ###

The [Code Cop Custom PMD Rules](https://bitbucket.org/pkofler/pmd-rules) contain PMD rules to check code for compliance with the Object Calisthenics'.
This project is set up to check the code using the Maven PMD Plugin on each `mvn test`.
You can also check the rules on their own with `mvn pmd:check`.
By using the [Maven Shell](https://github.com/jdillon/mvnsh) the time to run the check can be reduced by 50%.

To check the setup run `mvn test` on the sample code. It will show two violations:

  [INFO] PMD Failure: SampleClass.java:2 Rule:TooManyFields Priority:3 Too many fields.
  [INFO] PMD Failure: SampleClass:9 Rule:NoElseKeyword Priority:3 No else keyword.

### Limitations of Checking Code ###
Obviously code analysis cannot find everything.
For example the `PrimitiveObsession` rule (Wrap All Primitives And Strings) allows primitive values in constructors and getters because they are needed to implement [Value Objects](http://martinfowler.com/bliki/ValueObject.html).
On the other hand these getters are getters, so `NoGetterAndSetter` will flag them resulting in false positives.
Rule #5 (One Dot Per Line) is checked using PMD's own `LawOfDemeter` rule, which checks for the [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter). Now the LoD is not a dot counting exercise.
Sometimes a single dot in a line will already violate LoD.
It is very difficult to check for abbreviations, so rule #6 is not enforced.

You can use `// NOPMD` comments and `@SuppressWarnings("PMD")` annotations to suppress false positives.
I recommend using exact suppressions, e.g. `@SuppressWarnings("PMD.TooManyFields")` to skip issues because other issues at the same line will still be found. Use your good judgement. The goal of this exercise it to follow all eleven rules, not suppressing them.

### License ###
This work is licenced under a [New BSD License](http://opensource.org/licenses/bsd-license.php), see `license.txt` in repository.
