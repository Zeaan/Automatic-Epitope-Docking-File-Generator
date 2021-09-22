print("Enter the name you want to give that file")
name_of_file = input()

def makeLinearFile(name_of_file,start,end,chainName):
  f = open(name_of_file,'w')
  for i in range(start,end):
    text = str(i)+" "+chainName+"\n"
    f.write(text)
  text = str(end)+" "+chainName
  f.write(text)

def makeConformationalFile(name_of_file,start,end,chainName):
  count = 0
  f = open(name_of_file,'w')
  while True:
    for i in range(start,end):
      text = str(i)+" "+chainName+"\n"
      f.write(text)
    text = str(end)+" "+chainName
    f.write(text)
    ans = input("If you want to stop, type 'end' ")
    if ans=='end':
      break
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

print("If you want Linear Epitope generator, type 1\nIf you want Conformational Epitope generator, type 2")
n = int(input())
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
chainName = input("Enter the Chain Name: ")

if n==1:
  makeLinearFile(name_of_file,start,end,chainName)
if n==2:
  makeConformationalFile(name_of_file,start,end,chainName)