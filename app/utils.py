import os
import re
import shlex


class Empty:
    pass


def load_dotenv(filename='.env'):
    """
    Read local default environment variables from a
    .env file located in the project root directory.
    """
    try:
        with open(filename) as f:
            content = f.read()
    except IOError:
        content = ''

    for line in content.splitlines():
        # name = value -> ['name', '=', 'value']
        lexer = shlex.shlex(line, posix=True)
        tokens = list(lexer)

        if len(tokens) < 3:
            continue

        # name = tokens[0], op = tokens[1], slice rest of tokens to value
        name, op = tokens[:2]
        value = ''.join(tokens[2:])

        if op != '=' or not re.match(r'[A-Za-z_][A-Za-z_0-9]*', name):
            continue

        os.environ.setdefault(name, value)


def get_env(key, default=Empty):
    strict = os.environ.get('STRICT_ENV_LOAD', 'true').lower() == 'true'
    try:
        return os.environ[key]
    except KeyError:
        if default is not Empty:
            return default
        if strict:
            print('Environment variable "{}" missing.'.format(key))
        return None


def parse_boolean(string):
    value = string.lower()
    if value == 'true':
        return True
    if value == 'false':
        return False
    raise ValueError('invalid boolean string value: {}'.format(string))
