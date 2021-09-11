from .kumo import Kumo
from kumochan.core.consts import AttributeChoices
from kumochan.core.query.query import Query
import requests
from bs4.element import Tag
from bs4 import BeautifulSoup

class HtmlKumo(Kumo):

    async def fetch(self):
        pass
