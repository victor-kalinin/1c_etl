import sys
from os import environ
from os.path import join

from app.main import main, PARSER
from app.core.consts import LOG_FILE, LOGFILE_KEY

if len(sys.argv) == 1:
    print('\nERROR! Вы должны выбрать хотя бы тип рабочего окружения [-e].\n')
    PARSER.print_help()
else:
    parsed_arguments = PARSER.parse_args(sys.argv[1:])
    environ[LOGFILE_KEY] = join(parsed_arguments.log_path, LOG_FILE)
    main(parsed_arguments)
