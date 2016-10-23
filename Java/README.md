LCD Numbers Kata with PMD Object Calisthenics Check
===================================================

This is a template for the [LCD Numbers Kata](http://rubyquiz.com/quiz14.html).
The language is Java with JUnit.

### Constraints ###

[Jeff Bay's Object Calisthenics](http://williamdurand.fr/2013/06/03/object-calisthenics/).
# Only One Level Of Indentation Per Method.
# Don't Use The `else` Keyword.
# Wrap All Primitives And Strings.
# First Class Collections.
# One Dot/Arrow (dereference) Per Line.
# Don't Abbreviate (long names).
# Keep All Entities Small. (50 LoC per class)
# Not More Than Two Instance Variables.
# No Getters/Setters/Properties.

Using the Maven PMD Plugin the code is checked for compliance with the Object Calisthenics' rules
using the [Code Cop Custom PMD Rules}(https://bitbucket.org/pkofler/pmd-rules).
The rules are checked on each `mvn test`.

### License ###
This work is licensed under a [New BSD License](http://opensource.org/licenses/bsd-license.php), see `license.txt` in repository.
