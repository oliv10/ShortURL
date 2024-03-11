import uvicorn
import argparse
import shorturl

def run():

    PARSER = argparse.ArgumentParser(description=shorturl.__doc__)

    PARSER.add_argument('--version', action='version', version=f'{shorturl.__name__} {shorturl.__version__}')

    PARSER.add_argument('--host', nargs='?', default='127.0.0.1', type=str, help='host listening address')
    PARSER.add_argument('--port', nargs='?', default=5000, type=int, help='host listening port')

    # Add this functionalty at a later date.
    # PARSER.add_argument('--dbhost', nargs='?', default='redis', type=str, help='redis database host listening address')
    # PARSER.add_argument('--dbport', nargs='?', default=6379, type=int, help='redis database host listening port')

    PARSER.add_argument('--reload', action='store_true', help=argparse.SUPPRESS)
    PARSER.add_argument('--test', action='store_true', help=argparse.SUPPRESS)

    parsedArguments = PARSER.parse_args()

    HOST = parsedArguments.host
    PORT = parsedArguments.port
    
    RELOAD = parsedArguments.reload
    TEST = parsedArguments.test

    if not TEST:
        uvicorn.run("shorturl.app:app", host=HOST, port=PORT, log_level="info", reload=RELOAD)
