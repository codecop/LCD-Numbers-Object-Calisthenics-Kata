import astroid
from first_class_collections import FirstClassCollectionsChecker
from pylint.testutils import CheckerTestCase, Message


class TestFirstClassCollectionsChecker(CheckerTestCase):
    """Unit tests for the first class collections."""
    CHECKER_CLASS = FirstClassCollectionsChecker

    def test_allow_single_collection(self):
        node = astroid.parse("""
        class GoodCollectionSample(object):
            def __init__(self):
                self._a = []
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_allow_single_collection_initialisation(self):
        """Bug during workshop"""
        node = astroid.parse("""
        class GoodCollectionSample(object):
            def __init__(self):
                self._a = self._init()

            def _init(self):
                return []
        """)

        with self.assertNoMessages():
            self.walk(node.root())

    def test_find_array(self):
        node = astroid.parse("""
        class BadCollectionSample1(object):
            def __init__(self):
                self._a = []
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
                Message('collection-not-first-class', node=class_def, args=('BadCollectionSample1',), )):
            self.walk(node.root())

    def test_find_list_comprehension(self):
        node = astroid.parse("""
        class BadCollectionSample2(object):
            def __init__(self):
                self._a = [a for a in [1, 2, 3]]
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
                Message('collection-not-first-class', node=class_def, args=('BadCollectionSample2',), )):
            self.walk(node.root())

    def test_find_list(self):
        node = astroid.parse("""
        class BadCollectionSample3(object):
            def __init__(self):
                self._a = list()
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
                Message('collection-not-first-class', node=class_def, args=('BadCollectionSample3',), )):
            self.walk(node.root())

    def test_find_set(self):
        node = astroid.parse("""
        class BadCollectionSample4(object):
            def __init__(self):
                self._a = set()
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
                Message('collection-not-first-class', node=class_def, args=('BadCollectionSample4',), )):
            self.walk(node.root())

    def test_find_tuple(self):
        node = astroid.parse("""
        class BadCollectionSample5(object):
            def __init__(self):
                self._a = (1, 'a')
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
                Message('collection-not-first-class', node=class_def, args=('BadCollectionSample5',), )):
            self.walk(node.root())

    def test_find_hash(self):
        node = astroid.parse("""
        class BadCollectionSample6(object):
            def __init__(self):
                self._a = {'a': 1}
                self._b = 0
        """)

        class_def = list(node.get_children())[0]

        with self.assertAddsMessages(
                Message('collection-not-first-class', node=class_def, args=('BadCollectionSample6',), )):
            self.walk(node.root())
