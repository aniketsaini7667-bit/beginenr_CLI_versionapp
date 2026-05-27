# this project is a note taking CLI version and save them in file on note.txt
path="note.txt"
def add_note():
  try:
    with open(path,"r") as a:
      line=a.readlines()
      count=len(line)+1
  except:
    print("file not found ")
    print("crating a new file name note.txt in same folder")
    count=1
  topic=input(f"enter topic name {count} :".title()).strip()
  note=input("enter note :".title()).strip()
  print(f"{count}|{topic}|{note}\n")
  with open(path,"a") as f:
    f.write(f"{count}|{topic}|{note}\n")
  return 
def remove_note():
  try:
    with open(path,"r")as f:
      line=f.readlines()
      lenth=len(line)
      remove=input("enter the topic number :".title())
    if not remove.isdigit():
      print("input must be a number ")
      return
    remove=int(remove)
    if remove<=lenth:
      remove_line=line[remove-1]
      del line[remove-1]
      print(f"this topic got removet : {remove_line} ")
      storage=[]
      for i in range(0,len(line)):
        part=line[i].split("|")
        sec=part[1]
        thirt=part[2]
        new_line=f"{i+1}|{sec}|{thirt}"
        storage.append(new_line)
        with open(path,"w") as f:
          f.writelines(storage)
    else:
      print("line not fount ")

  except:
    print("file hasn't even created please add some note first")

      
    
def see_all_note():
  try:
    with open(path,"r") as f:
      line= f.readlines()
      lenth=len(line)
      if lenth == 0:
        print("empty note".upper())
      else:
        f.seek(0)
        print("=".center(50,"="))
        line= f.readlines()
        for i in line:
          print(f"{"|"}{i.ljust(10-len(i)," ")}{"-".center(50,"-")}")
        print("=".center(50,"="))
  except:
    print("empty - empty - empty note hasn't crated")
      
def search_topic():
  search= input("enter topic number :")
  if not search.isdigit():
    print("only positive number allowed ")
    return
  search=int(search)
  try:
    with open(path,"r") as f:
      line=f.readlines()
      lenth=(len(line))
      if lenth>=search>=1 :
        print(line[search-1])
        print("here you go")
      else:
        print("data not avalible ")
  except:
    print("empty :- please add note first")

def delete_note_file():
  try:
    with open(path,"r") as f:
      line=f.readlines()
      lenth=len(line)
    if lenth==0:
      print("note file is already empty")
    else:
      conform=input("are you sure you want to delete the note file ? (y/n) :").title()
      if conform=="Y":
        import os
        os.remove(path)
        print("note file deleted")
      else:
        print("note file is not deleted")  

  except:
    print("note file hasn't even created")



def menu():
  print("1. add note".title())
  print("2. remove note".title())
  print("3. see all note".title())
  print("4. search topic".title())
  print("5. note file path".title())
  print("6. exit".title())
  print("7. to delete the note file".title())
  
while True:
  menu()
  choice= input("enter you choice number :".strip())
  if choice.isdigit():
    choice=int(choice)
    if choice==1:
      add_note()
      continue
    elif choice==2:
      remove_note()
      continue
    elif choice==3:
      see_all_note()
      continue
    elif choice==4:
      search_topic()
      continue
    elif choice==5:
      try:
        with open(path,"r") as f:
          f.seek(0)
          print(path, "go to this location in your file to get the file ".title())
          continue
      except:
        print("file is not even created ")
        continue
    elif choice==6:
      print("thankyou for using this app")
      break
    elif choice==7:
      delete_note_file()
      continue
    else:
      print("only the number 1--7 allowed")
  else:
    print("only positive number allowed")