## LCD Numbers Kata with PMD Object Calisthenics Check ##

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
1. Keep All Entities Small. (50 LoC per class)
1. Not More Than Two Instance Variables.
1. No Getters/Setters/Properties.

Using the Maven PMD Plugin the code is checked for compliance with the Object Calisthenics' rules above.
Using the [Code Cop Custom PMD Rules](https://bitbucket.org/pkofler/pmd-rules) the rules are checked on each `mvn test`.
You can check the rule on their own with `mvn pmd:check`. By using the [Maven Shell](https://github.com/jdillon/mvnsh) the
time to run the check can be reduced by 50%. 

### License ###
This work is licensed under a [New BSD License](http://opensource.org/licenses/bsd-license.php), see `license.txt` in repository.