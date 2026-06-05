# this project is a note taking CLI version and save them in file on note.txt

import random 
import os

class Notefile:

  def __init__(self):
    self.path="note.txt"
    self.menu_item=["Exit", 
               "Add notes",
               "Remove notes",
               "See all notes",
               "Search topic",
               "See file path",
               "Delete note file",
               "show random notes"]
    self.menu_lenth=len(self.menu_item)
    



  def add_note(self):
    try:
      with open(self.path,"r") as a:
        line=a.readlines()
        count=len(line)+1
    except:
      print("file not found ")
      print("crating a new file name note.txt in same folder")
      count=1
    topic=input(f"enter topic name {count} :".title()).strip()
    note=input("enter note :".title()).strip()
    print(f"{count}|{topic}|{note}\n")
    with open(self.path,"a") as f:
      f.write(f"{count}|{topic}|{note}\n")
    return 
  def remove_note(self):
    try:
      with open(self.path,"r")as f:
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
          with open(self.path,"w") as f:
            f.writelines(storage)
      else:
        print("line not fount ")

    except:
      print("file hasn't even created please add some note first")

        
      
  def see_all_note(self):
    try:
      with open(self.path,"r") as f:
        line= f.readlines()
        lenth=len(line)
        if lenth == 0:
          print("empty note".upper())
        else:
          f.seek(0)
          print(f.read())
    except:
      print("empty - empty - empty note hasn't crated")
        
  def search_topic(self):
    search= input("enter topic number :")
    if not search.isdigit():
      print("only positive number allowed ")
      return
    search=int(search)
    try:
      with open(self.path,"r") as f:
        line=f.readlines()
        lenth=(len(line))
        if lenth>=search>=1 :
          print(line[search-1])
          print("here you go")
        else:
          print("data not avalible ")
    except:
      print("empty :- please add note first")

  def delete_note_file(self):
    try:
      with open(self.path,"r") as f:
        line=f.readlines()
        lenth=len(line)
      if lenth==0:
        print("note file is already empty")
      else:
        conform=input("are you sure you want to delete the note file ? (y/n) :").title()
        if conform in ["Y","Yes"]:
          os.remove(self.path)
          print("note file got deleted ")
        else:
          print("note file is not deleted")  

    except:
      print("note file hasn't even created")

  
  def random_note(self):
    try:
      with open(self.path,"r") as e:
        line= e.readlines()
        if len(line)==0:
          print("you don't have a note created yet")
        else:
          output=random.choice(line)
          print(output)
    except:
      print("note file havent created yet")


  def menu(self):
    for i,menu in enumerate(self.menu_item):
      print(f"|{i} -> {menu}")


go=Notefile()
while True:
  go.menu()
  choice= input("enter you choice number :".strip())
  if choice.isdigit():
    choice=int(choice)
    if choice==0:
      print("thankyou for using this app")
      break
    elif choice==1:
      go.add_note()
      continue
    elif choice==2:
      go.remove_note()
      continue
    elif choice==3:
      go.see_all_note()
      continue
    elif choice==4:
      go.search_topic()
      continue
    elif choice==5:
      try:
        with open(go.path,"r") as f:
          f.seek(0)
          print(go.path, "go to this location in your file to get the file ".title())
          continue
      except:
        print("file is not even created ")
        continue
    elif choice==6:
      go.delete_note_file()
      continue
    elif choice==7:
      go.random_note()
    else:
      print(f"only the number 0--{go.menu_lenth} allowed")
  else:
    print("only positive number allowed")