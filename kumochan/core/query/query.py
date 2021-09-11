from typing import Dict
from ..consts import AttributeChoices
from dataclasses import dataclass, field

@dataclass
class Query:
    result_type: AttributeChoices

class HtmlQuery(Query):
    # def __init__(self, css: str, attrs: Dict[str, str] = {}, result_type: AttributeChoices = AttributeChoices.TEXT) -> None:
    css: str
    attrs: Dict[str, str] = field(default_factory=dict)
