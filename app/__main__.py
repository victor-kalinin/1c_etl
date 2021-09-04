import sys
from os import environ

from app.main import main, PARSER
from app.core.consts import ENV_KEYNAME


if len(sys.argv) == 1:
    print('\nERROR! Вы должны выбрать хотя бы тип рабочего окружения [-e].\n')
    PARSER.print_help()
else:
    parsed_arguments = PARSER.parse_args(sys.argv[1:])
    environ[ENV_KEYNAME] = parsed_arguments.env
    main(parsed_arguments)
