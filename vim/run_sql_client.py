#!/usr/bin/python
import os, sys
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "editor.sql"
os.system('vim -c ":source sql_client.vim" -o ' + filename + ' viewer')
