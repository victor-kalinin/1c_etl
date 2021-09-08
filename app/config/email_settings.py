from typing import List


class EmailSettings:
    """
    Класс с настройками для отправки e-mail

    MAILHOST : str
        Строка с адресом сервера отправки e-mail
    PORT : int
    FROM : str
        Адрес отправителя
    TO : List[str]
        Список с получателями
    SUBJECT : str
        Тема сообщения
    """

    MAILHOST: str = 'mail-msk.corp.mango.ru'
    PORT: int = None
    FROM: str = 'DWH@mangotele.com'
    TO: List = ['v.kalinin@mangotele.com', ]     # Удалить в production
    # TO: List = ['t.babahanov@mangotele.com', 'r.shapkov@mangotele.com', 'ek.smirnova@mangotele.com',
    #             'a.leonisov@mangotele.com', 'v.kalinin@mangotele.com', 'a.mihneva@mangotele.com',
    #             'b.sadovskiy@mangotele.com', 'a.vinichenko@mangotele.com']
    SUBJECT: str = 'Logfile from 1CETL'
