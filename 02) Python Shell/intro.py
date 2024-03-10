# To open python shell directly write python in terminal then enter

# 1) module os : To known the directory

import os
a=os.getcwd()
print("Directory :",a)
# cwd: command directory

# 2) sys: system

import sys
c=sys.platform
print("System:",c)

# example: by use 1st folder
#  import hello
#  hello.ck("HI")

# 3) When the new data add and want to reload it
from importlib import reload
# reload(write the name of file)