"""Unit tests for Object Calisthenics rule 4: First class collections."""

import astroid
from pylint.testutils import CheckerTestCase, Message
from checkers.first_class_collections import FirstClassCollectionsChecker


class TestFirstClassCollectionsChecker(CheckerTestCase):
    """Unit tests for the first class collections."""
    CHECKER_CLASS = FirstClassCollectionsChecker

    def test_single_array(self):
        node = astroid.parse("""
        class GoodCollectionSample(object):
            def __init__(self):
                self._a = []
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_collection_initialisation(self):
        """Bug during workshop"""
        node = astroid.parse("""
        class Foo(object):
            def __init__(self):
                self._a = self._init()

            def _init(self):
                return []
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_find_array(self):
        node = astroid.parse("""
        class BadCollectionSample(object):
            def __init__(self):
                self._a = []
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
            Message('collection-not-first-class', node=class_def,
                    args=('BadCollectionSample',), )):
            self.walk(node.root())

    def test_find_list_comprehension(self):
        node = astroid.parse("""
        class BadCollectionSample(object):
            def __init__(self):
                self._a = [a for a in [1, 2, 3]]
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
            Message('collection-not-first-class', node=class_def,
                    args=('BadCollectionSample',), )):
            self.walk(node.root())

    def test_find_list(self):
        node = astroid.parse("""
        class BadCollectionSample(object):
            def __init__(self):
                self._a = list()
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
            Message('collection-not-first-class', node=class_def,
                    args=('BadCollectionSample',), )):
            self.walk(node.root())

    def test_find_set(self):
        node = astroid.parse("""
        class BadCollectionSample(object):
            def __init__(self):
                self._a = set()
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
            Message('collection-not-first-class', node=class_def,
                    args=('BadCollectionSample',), )):
            self.walk(node.root())

    def test_find_tuple(self):
        node = astroid.parse("""
        class BadCollectionSample(object):
            def __init__(self):
                self._a = (1, 'a')
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
            Message('collection-not-first-class', node=class_def,
                    args=('BadCollectionSample',), )):
            self.walk(node.root())

    def test_find_hash(self):
        node = astroid.parse("""
        class BadCollectionSample(object):
            def __init__(self):
                self._a = {'a': 1}
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
            Message('collection-not-first-class', node=class_def,
                    args=('BadCollectionSample',), )):
            self.walk(node.root())
