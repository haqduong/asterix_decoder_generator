import sys
import re

data = sys.stdin.readlines()

for line in data:
    line = line.strip()
    if re.match(r"// .*", line) is None:
        m = re.match(r"(?P<type>\S+) (?P<name>get[^(]+).+;", line)
        # gen name
        if m is None:
            continue
        name = m.group('name')[4:]
        name_part = re.split("([A-Z][a-z]+)", name)
        name_part = [part for part in name_part if len(part) > 0]
        display_name = " ".join(name_part)
        if m is not None:
            if m.group('type') != "QString":
                print 'e->append(QString("' + display_name + ': ") + QString::number(mTrackInfo->' + m.group('name') + '()));'
            else:
                print 'e->append(QString("' + display_name + ': ") + mTrackInfo->' + m.group('name') + '());'

# e->append(QString("Time: ") + ret);
