# -*- coding: utf-8 -*-
import re

import sjFs

NAME_REG = r".*logcat\.log\.([0-9]+)?"


def parse_file(filename):
    no = -1
    m = re.compile(NAME_REG).match(filename)
    if m and len(m.groups()):
        no = int(m.group(1))
    return no


def parse_dir(logcat_dir):
    count = 0
    fn_list = sjFs.list_files(logcat_dir)
    for fn in fn_list:
        print fn
        i = parse_file(fn)
        if i > count:
            count = i
    return count


def mv_files(count):
    # logcat.log logcat.log.1 logcat.log.2
    # logcat.03.log logcat.02.log logcat.01.log

    old_names = []
    new_names = []
    old_names.append("logcat.log")
    new_name = "logcat.%02d.log" % (count + 1)
    new_names.append(new_name)

    for i in range(1, count + 1):
        old_name = "logcat.log.%d" % i
        new_name = "logcat.%02d.log" % (count + 1 - i)
        old_names.append(old_name)
        new_names.append(new_name)

    return old_names, new_names

