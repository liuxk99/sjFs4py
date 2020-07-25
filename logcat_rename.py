# -*- coding: utf-8 -*-
import getopt
import os
import re
import sys

import sjFs

NAME_REG = r".*logcat\.log\.([0-9]+)?"


def parse_file(filename):
    no = -1
    m = re.compile(NAME_REG).match(filename)
    if m and len(m.groups()):
        no = int(m.group(1))
    return no


def parse_dir(log_dir):
    count = 0
    fn_list = sjFs.list_files(log_dir)
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

def help(exec_cmd):
    print "%s --logcat-dir=$dir" % exec_cmd
    sys.exit(1)

    pass


def do_main(log_dir):
    count = parse_dir(log_dir)
    old_names, new_names = mv_files(count)
    for i in range(0, count + 1):
        old_name = os.path.join(log_dir, old_names[i])
        new_name = os.path.join(log_dir, new_names[i])

        print "mv %s -> %s" % (old_name,
                               new_name)
        os.rename(old_name, new_name)
    pass


if __name__ == '__main__':
    # sys.setdefaultencoding('utf8')
    exec_cmd = sys.argv[0]

    print sys.argv[1:]
    if len(sys.argv) < 2:
        help(exec_cmd)

    # parse parameters
    opts = []
    try:
        opts, arg = getopt.getopt(sys.argv[1:], "",
                                  ["logcat-dir="])
    except getopt.GetoptError:
        print("syntax error")
        help(exec_cmd)

    logcat_dir = None

    for opt, arg in opts:
        if opt in '--logcat-dir':
            logcat_dir = arg
        elif opt in '--help':
            help(exec_cmd)
    if logcat_dir is None:
        print("syntax error")
        help(exec_cmd)

    do_main(logcat_dir)