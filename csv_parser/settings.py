import os

token = os.environ.get('CSV_PARSER_TELE_TOKEN', False)
if not token:
    print('You must set env var CSV_PARSER_TELE_TOKEN')
    exit(1)

csv_file = os.environ.get('CSV_PARSER_FILE', False)
if not token:
    print('You must set env var CSV_PARSER_FILE')
    exit(1)
