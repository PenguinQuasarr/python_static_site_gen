class HTMLNode:
    def __init__(self, 
                 html_tag: str | None = None,
                 html_value: str | None = None,
                 html_children: list | None = None,
                 html_props: dict | None = None):

        self.tag = html_tag
        self.value = html_value
        self.children = html_children
        self.props = html_props


    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        formatted_string: str
        for key, value in self.props:
            formatted_string += f'{key}="{value}" '
        return formatted_string
