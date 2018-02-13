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
# * knows [], (), list(), set() and comprehensions.
# TODO add support for more types of collections.
# * (kind of) DONE

# 5. One dot per line
import checkers.one_dot_per_line
# TODO deal with imports with a dot, e.g. os.path -> put "path" into imported list.
# * DONE

# 6. Don't abbreviate
# TODO add rule to avoid short names (<=3 characters).
# * good-names=reset

# 7. Keep all entities small
import checkers.small_entities
# * no class over 45 statements, no module over 10 classes, no module over 45 statements.
# * (kind of) DONE

# 8. No classes with more than two instance variables
import checkers.two_instance_variables
# * also Pylint's "checkers.design_analysis", max-attributes=2
# * DONE

# 9. No getters/setters/properties
import checkers.no_properties
# TODO do not use manual getters/setters
# * (kind of) DONE
