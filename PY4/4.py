"""
The build_xml_element function receives the following parameters:
tag, content, and key-value elements given as name-parameters.
Build and return a string that represents the corresponding XML element.
Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
"""


def build_xml_element(tag, content, **elements):
    return "<{} {}>{}</{}>".format(
        tag, ' '.join(["{}={bs}{}{bs}".format(key, value, bs=r'\"') for key, value in elements.items()]),
        content,
        tag
    )


if __name__ == '__main__':
    print(build_xml_element("a", "Hello there", href=" https://python.org ", _class=" my-link ", id= " someid "))
