from kumochan.kumochan import create_html_kumo

async def test_kumochan():
    kumo = create_html_kumo(url="https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movie_Quotes", query={"quetes": {
        "css": ".wikitable tr td:nth-child(2)",
        "result_type": "text",
    }})

    await kumo.fetch()
    quote = await kumo.first()
    assert quote == "\"Frankly, my dear, I don't give a damn.\""
