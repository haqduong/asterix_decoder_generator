#!/usr/bin/env/python2

import sys

data = sys.stdin.readlines()
enum = data[0].rstrip()
enum_value = data[1].rstrip()

#enum = "DI___"
#enum_value = "___, ___, ___, ___"

for field in enum_value.split(', '):
    print "case " + enum + "::" + field + ":"
    print 's += "' +  field + '";'
    print 'break;'
