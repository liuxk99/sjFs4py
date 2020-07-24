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
