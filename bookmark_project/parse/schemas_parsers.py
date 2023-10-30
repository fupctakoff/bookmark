from bs4 import BeautifulSoup


### Представленных классов достаточно для парсинга Open Graph, Shema org, JSON-LD (отправленные сайты проходят) схем
class OGParser:
    @classmethod
    def parse_title(cls, soup: BeautifulSoup) -> str | None:
        """Парсинг title со схемой open graph"""
        title = soup.find(attrs={'property': 'og:title'})
        if title:
            title = title.get('content')
        return title

    @classmethod
    def parse_description(cls, soup: BeautifulSoup) -> str | None:
        """Парсинг description со схемой open graph"""
        description = soup.find(attrs={'property': 'og:description'})
        if description:
            description = description.get('content')
        return description


class SOParser:
    @classmethod
    def parse_title(cls, soup: BeautifulSoup) -> str | None:
        """Парсинг title со схемой schema org"""
        title = soup.find(attrs={'itemprop': 'title'})
        if title:
            title = title.get('content')
        return title

    @classmethod
    def parse_description(cls, soup: BeautifulSoup) -> str | None:
        """Парсинг description со схемой schema org"""
        description = soup.find(attrs={'itemprop': 'description'})
        if description:
            description = description.get('content')
        return description


class NoSchemaParser:
    @classmethod
    def parse_title(cls, soup: BeautifulSoup) -> str | None:
        """Парсинг title, если у сайта нет поддерживаемой разметки"""
        title = soup.find('title')
        if title:
            title = title.text
        return title

    @classmethod
    def parse_description(cls, soup: BeautifulSoup) -> str | None:
        """Парсинг description, если у сайта нет поддерживаемой разметки"""
        description = soup.find(attrs={'name': 'description'})
        if description:
            description = description.get('content')
        return description
