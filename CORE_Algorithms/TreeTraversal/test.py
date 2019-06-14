import unittest
from typing import List
from CORE_Algorithms.TreeTraversal.BinaryTreeImpl import BinaryTree, BinaryTreeImpl


def str_compare(a: str, b: str) -> int:
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0


class TestBinaryTree(unittest.TestCase):
    __my_tree: BinaryTree[str]

    def setUp(self) -> None:
        self.__my_tree = BinaryTreeImpl(str_compare)

        self.__my_tree.add('B')
        self.__my_tree.add('A')
        self.__my_tree.add('D')
        self.__my_tree.add('E')
        self.__my_tree.add('C')
        self.__my_tree.add('F')

    def test_tree(self):
        print("My Binary Tree:{}".format(self.__my_tree))

    def test_pre_order(self):
        print("Pre Order Test")
        copy_tree: BinaryTree[str] = BinaryTreeImpl(str_compare)
        for v in self.__my_tree.pre_order():
            copy_tree.add(v)
            print(v, end=", ")
        print("")

        print("Pre-Order should create identical copies")
        print(copy_tree)
        print(self.__my_tree)
        self.assertEqual(self.__my_tree, copy_tree)

    def test_in_order(self):
        print("In Order Test")
        traversed: List[str] = self.__my_tree.in_order()
        last: str or None = None
        order_checked: int = 0
        for v in traversed:
            # Check this new value is more than or equal to the last one
            if last is not None:
                self.assertTrue(last < v)
                order_checked += 1
            print(v, end=", ")
            last = v
        print("")
        # Make sure we did actually compare values
        self.assertEqual(order_checked, len(traversed) - 1)

    def test_post_order(self):
        print("Post Order Test")
        traversed: List[str] = self.__my_tree.post_order()
        for v in traversed:
            print(v, end=", ")
        print("")
