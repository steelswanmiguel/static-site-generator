import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_basic(self):
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("p", "Second paragraph")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(parent.to_html(), "<div><p>First paragraph</p><p>Second paragraph</p></div>")

    def test_parent_to_html_with_props(self):
        child = LeafNode("a", "Click me", {"href": "https://example.com"})
        parent = ParentNode("nav", [child], {"class": "menu"})
        self.assertEqual(parent.to_html(), '<nav class="menu"><a href="https://example.com">Click me</a></nav>')

    def test_parent_to_html_nested(self):
        leaf1 = LeafNode("li", "Item 1")
        leaf2 = LeafNode("li", "Item 2")
        inner_parent = ParentNode("ul", [leaf1, leaf2])
        outer_parent = ParentNode("div", [inner_parent], {"class": "container"})
        self.assertEqual(outer_parent.to_html(), 
                        '<div class="container"><ul><li>Item 1</li><li>Item 2</li></ul></div>')

    def test_parent_to_html_no_tag(self):
        parent = ParentNode(None, [LeafNode("p", "Test")])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parent_to_html_no_children(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()