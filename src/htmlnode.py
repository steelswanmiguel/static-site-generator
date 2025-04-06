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

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        # Call the parent class's __init__ method
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
    
        if self.tag == None:
            return self.value
        
        props_html = ""
        if self.props:
            props_html = " " + self.props_to_html()
            
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    
class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
    
        if self.children == None:
            raise ValueError("Children parameter missing")
        
        props_html = ""
        if self.props:
            props_html = " " + self.props_to_html()

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
            
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"