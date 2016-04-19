import sys
import re
from sets import Set

def prettifier(code_name):
	name_part = re.split("([A-Z][a-z]+)", code_name)
	name_part = [part for part in name_part if len(part) > 0]
	return " ".join(name_part)


data = sys.stdin.readlines()

result = []
item = Set()

for line in data:
	line = line.strip()
	last_field = []
	if re.match(r"// .*", line) is None:
		m = re.match(r"(?P<type>\S+) (?P<name>get[^(]+).+;", line)
		# gen name
		if m is None:
			continue
		name = m.group('name')[4:]
		name_part = re.split('_', name)
		name_part = [part for part in name_part if len(part) > 0]

		current = ""
		parent = "twDetail"
		for part in name_part[:-1]:
			if len(current) > 0:
				parent = current
			else:
				parent = "twDetail"
			if len(current) > 0:
				current = "_".join([current, part])
			else:
				current = part
			if current not in item:
				result.append("QTreeWidgetItem *" + current + ";")
				result.append(current + " = new QTreeWidgetItem(" + parent + ", QStringList(\"" + prettifier(part) + "\"));")
				item.add(current)
		if len(name_part) < 2:
			parent = "twDetail"
		else:
			parent = current

		display_name = prettifier(name_part[-1])
		if m.group('type') != "QString":
			value = 'QString::number(trackInfo->' + m.group('name') + '())'
		else:
			value = 'trackInfo->' + m.group('name') + '()'

		result.append('addItemToParent(' + parent + ', "' + display_name + '", ' + value + ');')


print "\n".join(result)

# e->append(QString("Time: ") + ret);