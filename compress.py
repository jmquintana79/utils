#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:18:36 2019

@author: admin
"""

import zipfile
import os

## unzipping
def unzip(path_input:str, folder_output:str = '', verbose:bool = False)->bool:
    """
    Unzzip a .zip file.
    path_input -- path of input zipped file.
    folder_outpout -- output folder (default = '').
    verbose -- display or not extra information (defatul False).
    return -- True/False if the process was successful or not.
    """
    
    # validation
    assert '.zip' in path_input, 'input file have to be a zip file.'
    if folder_output == '':
        folder_output = path_input.replace('.zip','')
    # unzip
    try:
        with zipfile.ZipFile(path_input,"r") as zip_ref:
            zip_ref.extractall(folder_output)
        print('[info] it was unzipped "%s" successfully.'%os.path.split(path_input)[-1])
        return True
    except Exception as e:
        print('[error] there are a problem unzipping "%s"...'%os.path.split(path_input)[-1])
        print(str(e))
        return False
    
## zipping
def zip(folder_input:str, path_output:str = '', verbose:bool = False)->bool:
    """
    Zip a folder.
    folder_input -- folder to be zipped.
    path_outpout -- output path (default = '').
    verbose -- display or not extra information (defatul False).
    return -- True/False if the process was successful or not.
    """
    # function
    def zipdir(path, ziph):
        # Iterate all the directories and files
        for root, dirs, files in os.walk(path):
            # Create a prefix variable with the folder structure inside the path folder. 
            # So if a file is at the path directory will be at the root directory of the zip file
            # so the prefix will be empty. If the file belongs to a containing folder of path folder 
            # then the prefix will be that folder.
            if root.replace(path,'') == '':
                    prefix = ''
            else:
                    # Keep the folder structure after the path folder, append a '/' at the end 
                    # and remome the first character, if it is a '/' in order to have a path like 
                    # folder1/folder2/file.txt
                    prefix = root.replace(path, '') + '/'
                    if (prefix[0] == '/'):
                            prefix = prefix[1:]
            for filename in files:
                    actual_file_path = root + '/' + filename
                    zipped_file_path = prefix + filename
                    zipf.write( actual_file_path, zipped_file_path)
                    
    # validation
    if path_output == '' or not '.zip' in path_output:
        path_output = '%s.zip'%folder_input
    # zip
    try:
        zipf = zipfile.ZipFile(path_output, 'w', zipfile.ZIP_DEFLATED)
        zipdir(folder_input, zipf)
        zipf.close()
        print('[info] it was zipped "%s" successfully.'%os.path.split(folder_input)[-1])
        return True
    except Exception as e:
        print('[error] there are a problem zipping "%s"...'%os.path.split(folder_input)[-1])
        print(str(e))
        return False
    
    
if __name__ == "__main__":
    path_input = '/Users/admin/Workspace/github/mytools/GoogleKeep_to_Text/data/bkp-google_keep-copy'
    folder_output = ''
    zip(path_input, '', True)