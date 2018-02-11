"""Unit tests for Object Calisthenics rule 5: One dot per line."""

import astroid
from checkers.one_dot_per_line import OneDotPerLineChecker
from pylint.testutils import CheckerTestCase


class TestOneDotPerLineChecker(CheckerTestCase):
    """Unit tests for TODO."""
    CHECKER_CLASS = OneDotPerLineChecker

    def xtest_call_call(self):
        """Test that if is left alone."""

        node = astroid.parse("""
        get_x().get_y()
        """)

        assert True

    def test_field_call(self):
        """Test that if is left alone."""

        node = astroid.parse("""
        a.get_y()
        """)

        assert True
