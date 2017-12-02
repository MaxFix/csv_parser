import os

token = os.environ.get('CSV_PARSER_TELE_TOKEN', False)
if not token:
    print('You must set env var CSV_PARSER_TELE_TOKEN')
    exit(1)