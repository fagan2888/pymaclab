#!/usr/bin/env python

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info
    config = Configuration('dattrans', parent_package, top_path)
    config.add_subpackage('fred')
    return config

if __name__ == '__main__':
    print('This is the wrong setup.py file to run')
