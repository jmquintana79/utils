#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 12:07:27 2019

@author: admin
"""

import yaml

## load yml file
def load(path_input:str)->dict:
    """
    Load yml file.
    path_input -- path of yml file to be parsed.
    return -- dictionary of loaded file content.
    """
    with open(path_input, 'r') as stream:
        try:
            dfile = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print('[error] there any problem loading the yml file.')
            print(exc)
    return dfile


if __name__ == "__main__":
    import os
    
    # arguments
    folder_input = '/Users/admin/Workspace/projects/keywords/scripts/dev/v3-improving_computational_time'
    file_input = 'config.yml'
    
    # load
    dfile = load(os.path.join(folder_input, file_input))