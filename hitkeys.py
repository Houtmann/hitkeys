####################################################
#
# Version 1.0 for Python 3
# by hadmagic
# https://github.com/hadmagic
#
####################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


import os
import argparse
import sys
import datetime
import keys

parser = argparse.ArgumentParser()
parser.add_argument("PATH", help="precise path of disk or folder")
args = parser.parse_args()

fileList = []
fileSize = 0
folderCount = 0
rootdir = args.PATH
output = open('output.txt', 'w')

for root, subFolders, files in os.walk(rootdir): #List All files of the path
    folderCount += len(subFolders)
    for file in files:
        f = os.path.join(root,file)
        try:
            fileSize = fileSize + os.path.getsize(f)
        except:
            continue
        fileList.append(f)

print(("Total Size    : {0} Mo".format(fileSize // 1024 //1024)))
print("Total Files   :", len(fileList))
print("Total Folders :", folderCount)
#print(keys.list_keys)


hit_count = 0
for i in range(0, len(fileList)):
        sys.stdout.write('\r' + str(i) + ' / ' + str(len(fileList)) +'\r' )

        for hit in keys.list_keys:
            try:
                fopen = open(fileList[i], 'rb+') # open all files of the dirs
                if hit in fopen.read().decode('latin1'):
                    hit_count += 1
                    
                    output.write(hit +' ---> ' + fileList[i] + '\n')
                    
                else:
                    pass
            
            except MemoryError:
                with open(fileList[i], 'rb+') as fopen:
                    for chunk in iter(lambda: fopen.read(8192), b''):
                        
                          if hit in chunk.decode('latin1'):
                              hit_count += 1
                              output.write(hit +' ---> ' + fileList[i]+ '\n')
            except:
                pass

            fopen.close()
print('\n'+ 'Resultat trouvés : ' + str(hit_count))
        
        
