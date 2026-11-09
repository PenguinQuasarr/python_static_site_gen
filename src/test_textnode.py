import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is not equal", TextType.BOLD_TEXT)
        node2 = TextNode("This is not equal", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_has_none(self):
        node = TextNode("has none", TextType.BOLD_TEXT, None)
        node2 = TextNode("has none", TextType.BOLD_TEXT, None)
        self.assertEqual(node, node2)

    def test_has_url(self):
        node = TextNode("has url", TextType.CODE_TEXT, "https")
        node2 = TextNode("has url", TextType.CODE_TEXT, "https")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
