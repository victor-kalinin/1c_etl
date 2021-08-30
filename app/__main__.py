import sys

from app.main import main, PARSER

if len(sys.argv) == 1:
    print('\nERROR! Вы должны выбрать хотя бы тип рабочего окружения [-e].\n')
    PARSER.print_help()
else:
    parsed_arguments = PARSER.parse_args(sys.argv[1:])
    main(parsed_arguments)
