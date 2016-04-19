import sys
import re

data = sys.stdin.readlines()

for line in data:
    line = line.strip()
    if re.match(r"// .*", line) is None:
        m = re.match(r"(?P<type>\S+) (?P<name>.+);", line)
        if m is not None:
            if m.group('type') != "QString":
                print m.group('name') + " = 0;"
            else:
                print m.group('name') + ' = "";'
