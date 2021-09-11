from typing import Dict, List, Union
from kumochan.core.consts import AttributeChoices
from kumochan.core.query.query import Query
import requests
from bs4.element import Tag
from bs4 import BeautifulSoup


class Kumo:
    return_result: List[Union[Tag, str, Dict[str, str]]]
    return_type: AttributeChoices

    def __init__(self, url: str, query: Query):
        self.url = url
        self.query = query

    async def fetch(self):
        pass

    
    async def return_result(self):
        pass

    async def first(self):
        pass
