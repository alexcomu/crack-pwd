import sys
from hashlib import sha256

'''
How To use:

python SCRIPT_NAME USERNAME PWD

Return 
  True    if pwd is right
  False   if pwd is wrong

If PWD is correct go to:
http://194.116.76.60/PWD

Attention, use clear PWD not hashed.
'''

def process(username, password):
  myTable = dict(steve="e5a7cb935075fb9de473fadf28ad04b18f6145c13259bc87e31bd2b93383b463",
                 penny="5b898ab6fb958c8b61c253041c730f7a3f068d7e247ce74046404dffed5a2a98",
                 john="7c5c9c9999e6b99533604d9525288bf6ffedf515068100eff7ea0c48fb0b3ff3")
  #check if username exists
  if not username in myTable.keys():
    print "\n##ERROR.\n#####Username not found.\n"
    sys.exit(1)

  #search user
  for name in myTable.keys():
    if name==username:
      #check hashed password
      hashed_pwd = sha256()
      hashed_pwd.update(password)
      return hashed_pwd.hexdigest() == myTable[name]

def main():
  if len(sys.argv) != 3:
    print '\nWrong usage!\nExample: python script.py username password\n'
    sys.exit(1)

  print process(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
  main()
