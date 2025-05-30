from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __eq__(self, targetTextNode):
        return self.text == targetTextNode.text and self.text_type == targetTextNode.text_type and self.url == targetTextNode.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    textType = text_node.text_type
    if textType == TextType("text"):
        return LeafNode(None, text_node.text)
    if textType == TextType("bold"):
        return LeafNode("b", text_node.text)
    if textType == TextType("italic"):
        return LeafNode("i", text_node.text)
    if textType == TextType("code"):
        return LeafNode("code", text_node.text)
    if textType == TextType("link"):
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if textType == TextType("image"):
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    