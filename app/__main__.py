import sys

from app import main

if len(sys.argv) == 1:
    print('\nERROR! Вы должны выбрать хотя бы одну опцию.\n')
    main.PARSER.print_help()
else:
    parsed_arguments = main.PARSER.parse_args(sys.argv[1:])
    main.main(parsed_arguments)
