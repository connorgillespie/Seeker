info = """
   ____            _             
  / ___|  ___  ___| | _____ _ __ 
  \___ \ / _ \/ _ \ |/ / _ \ '__|
   ___) |  __/  __/   <  __/ |   
  |____/ \___|\___|_|\_\___|_|   
                                
  Author: Connor Gillespie
  Description: An advanced but simple file seeker.
  Documentation: github.com/
  License: MIT
  
"""
import os, fnmatch, datetime

print(info)
seek = input("  File: ")
path = input("  Path: ")

"""

  Searches the specified path for the specified files.

"""
def find(seek, path):  
  results = []
  
  for root, dirs, files in os.walk(path):
    for file in fnmatch.filter(files, seek):
      file = path + "/" + file
      results.append(file)
  
  return results

"""

  Outputs files found to a text file.

"""
results = find(seek, path)
print("\n\n  {} results found for {}\n  Results added to results.txt\n\n".format(len(results), seek))
with open(os.path.dirname(os.path.realpath(__file__)) + "/results.txt", "w") as f:
  f.write("Executed {} with {} results found.\n\n".format(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"), len(results)))
  
  i = 0
  for file in results:
    i = i + 1
    f.write("{}. {}\n".format(i, file))
    
  f.close()

"""

  Prevents script from closing on Windows operating systems.

"""
if os.name == "nt":
  os.system("pause")

  

