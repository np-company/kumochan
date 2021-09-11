from enum import Enum, unique

@unique
class Choices(Enum):
    pass


class AttributeChoices(Choices):
    TAG = "tag"
    ATTRS = "attrs"
    TEXT = "text"

