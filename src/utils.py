import logging

from requests import RequestException
from exceptions import ParserFindTagException
from constants import EXPECTED_STATUS


def get_response(session, url):
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def status_comparison(status1, status2):
    if status2 not in EXPECTED_STATUS[status1]:
        info_msg = (f'Несовпадающие статусы:\n'
                    f'Статус в карточке: {status2}\n'
                    f'Ожидаемые статусы: {EXPECTED_STATUS[status1]}')
        logging.info(info_msg)
