# -*- coding: utf-8 -*-
import os

filelist = []


def walk_through_dir(rootDir):
    for filename in os.listdir(rootDir):
        # print filename
        path = os.path.join(rootDir, filename)
        filelist.append(path)
        # print path
        if os.path.isdir(path):
            walk_through_dir(path)


def list_files(root_dir):
    fn_list = []

    for filename in os.listdir(root_dir):
        path = os.path.join(root_dir, filename)
        fn_list.append(path)

    return fn_list
