from aiogram import types, Dispatcher
import wikipedia
from pprint import pprint
import hashlib

def finder(text):
    return wikipedia.page(text).content

async def inline_wiki_handler(query: types.InlineQuery):
    text = query.query or "pishi normalno"
    links = finder(text)
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(f"{link['id']}".encode()).hexdigest(),
        title=link['title'],
        url=f"https://ru.wikipedia.org/wiki/{link['url_suffix']}",
        thumb_url=f"{link['thumbnails'][0]}",
        input_message_content=types.InputMessageContent(
            message_text=f"твоя ссылкa https://ru.wikipedia.org/wiki/{link['url_suffix']}"
        )
    ) for link in links]
    await query.answer(articles, cache_time=60)

wiks = inline_wiki_handler
pprint(wiks)
def register_handler_inline(dp: Dispatcher):
    dp.register_inline_handler(inline_wiki_handler)