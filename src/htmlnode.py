class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return " ".join([f"{key}=\"{value}\"" for key, value in self.props.items()])
    
    def __repr__(self):
        props_str = self.props_to_html() if self.props else ""
        children_str = f"children={self.children}" if self.children else ""
        value_str = f"value={self.value}" if self.value else ""

        return f"HtmlNode(tag='{self.tag}'{value_str}{children_str}, props={{{props_str}}})"
