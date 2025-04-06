import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test with empty props
        node = HtmlNode("div", "content", [], {})
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HtmlNode("a", "Click me", [], {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), "href=\"https://example.com\"")
    
    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HtmlNode(
            "a",
            "Click me",
            [],
            {
                "href": "https://example.com",
                "target": "_blank",
                "class": "link-button"
            }
        )
        # Since dictionary order is not guaranteed, we need to check all props are included
        result = node.props_to_html()
        self.assertIn("href=\"https://example.com\"", result)
        self.assertIn("target=\"_blank\"", result)
        self.assertIn("class=\"link-button\"", result)
        
        # Check format of final string - each property is separated by a space
        # Count space characters - should be one fewer than the number of properties
        self.assertEqual(result.count(" "), 2)


if __name__ == "__main__":
    unittest.main()