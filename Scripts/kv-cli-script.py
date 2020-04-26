#!E:\PycharmProjects\TestConstructor\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'kv==0.3','console_scripts','kv-cli'
__requires__ = 'kv==0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('kv==0.3', 'console_scripts', 'kv-cli')()
    )
