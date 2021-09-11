from kumochan.core.kumo import HtmlKumo
from kumochan.core.query.query import HtmlQuery
from typing import Dict, NewType

QueryArgs = NewType("QueryArgs", Dict[str, str])
QueryName = NewType("QueryName", str)


def create_html_kumo(url: str, query: Dict[QueryName, QueryArgs]) -> HtmlKumo:
    return HtmlKumo(url, HtmlQuery(query))