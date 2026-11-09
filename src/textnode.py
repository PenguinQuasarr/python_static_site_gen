from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"


class TextNode:
    def __init__(self, node_text: str, type_text: str, link_text: str | None = None):
        self.text = node_text
        self.text_type = TextType(type_text)
        self.url = link_text

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
        


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
