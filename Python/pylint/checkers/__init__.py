"""Jeff Bay's Object Calisthenics Rules."""

# 1. One level of indentation per method
# * Pylint's "checkers.refactoring", max-nested-blocks=1
# * Pylint's "checkers.design_analysis", max-branches=1
# * DONE

# 2. Don't use the ELSE keyword
import checkers.no_else
# * also Pylint's "checkers.refactoring", max-nested-blocks=1
# * DONE

# 3. Wrap all primitives and Strings

# 4. First class collections
import checkers.first_class_collections
# * currently knows [], (), list(), set() and comprehensions, add more types of collections
# * (kind of) DONE

# 5. One dot per line

# 6. Don't abbreviate
# TODO short names
# * good-names=reset

# 7. Keep all entities small (no class over 50 lines, no package over 10 files)
import checkers.small_entities
# TODO max 10 toplevel things in module
# * (kind of) DONE

# 8. No classes with more than two instance variables
import checkers.two_instance_variables
# * also Pylint's "checkers.design_analysis", max-attributes=2
# * DONE

# 9. No getters/setters/properties
import checkers.no_properties
# TODO property constructor/class method
# TODO do not use manual getters/setters
