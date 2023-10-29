import requests
from bs4 import BeautifulSoup
from .schemas_parsers import OGParser, SOParser, NoSchemaParser

# постоянная переменная для запроса в requests, можно добавить n 'user-agent'
# и делать рандомную выборку из них для уменьшения вероятности блокировки

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


class ParseResult:
    title = None
    description = None
    favicon = None
    _soup = None

    def __init__(self, url):
        self.url = url

    def _get_bs4_from_html(self, url) -> None:
        """Получает html с получаемого значения url, создает экземпляр класса soup для последующего парсинга"""
        response = requests.get(url, headers=HEADER).text
        self._soup = BeautifulSoup(response, 'html.parser')
        return

    def _title_setter(self) -> None:
        """Устанавливает значение title"""
        title = OGParser.parse_title(self._soup)
        if title is None:
            title = SOParser.parse_title(self._soup)
            if title is None:
                title = NoSchemaParser.parse_title(self._soup)
                if title is None:
                    title = 'Информация не была найдена'

        self.title = title
        return

    def _description_setter(self) -> None:
        """Устанавливает значение description"""
        description = OGParser.parse_description(self._soup)
        if description is None:
            description = SOParser.parse_description(self._soup)
            if description is None:
                description = NoSchemaParser.parse_description(self._soup)
                if description is None:
                    description = 'Информация не была найдена'

        self.description = description
        return

    def _favicon_setter(self) -> None:
        """Ссылка на favicon с сайта по адресу self.url"""
        self.favicon = f"https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url={self.url}&size=6"

    def _worker(self) -> None:
        """Собирает все элементы парсинга в определенной последовательности"""
        self._get_bs4_from_html(self.url)
        self._title_setter()
        self._description_setter()
        self._favicon_setter()
        return

    def get_tags(self) -> dict:
        """Возвращает ранее спаршенные данные"""
        self._worker()
        return {'title': self.title, 'description': self.description, 'favicon': self.favicon}

# url = 'some url'
# instance = ParseResult(url)
# print(instance.get_tags())
