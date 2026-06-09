# This project is a note-taking CLI version that saves notes to a file named note.txt

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
    self.menu_length=len(self.menu_item)
    self.file_not_found= "file is not even created yet please first add some notes to the file"
    
  def __open_file(self):
    with open(self.path,"r") as e:
      self.line=e.readlines()
    return self.line


  def add_note(self):
    try:
      self.__open_file()
      count=len(self.line)+1
    except:
      print("file not found ")
      print("creating a new file name note.txt in same folder")
      count=1
    topic=input(f"enter topic name {count} :".title()).strip()
    note=input("enter note :".title()).strip()
    print(f"{count}|{topic}|{note}\n")
    with open(self.path,"a") as f:
      f.write(f"{count}|{topic}|{note}\n")
    return 
  

  def remove_note(self):
    try:
      self.__open_file()
      length=len(self.line)
      remove=input("enter the topic number :".title())
      if not remove.isdigit():
        print("input must be a number ")
        return
      remove=int(remove)
      if remove<=length:
        remove_line=self.line[remove-1]
        del self.line[remove-1]
        print(f"this topic got removed : {remove_line} ")
        storage=[]
        for i in range(0,len(self.line)):
          part=self.line[i].split("|")
          sec=part[1]
          third=part[2]
          new_line=f"{i+1}|{sec}|{third}"
          storage.append(new_line)
        with open(self.path,"w") as f:
          f.writelines(storage)
      else:
        print("line not found ")

    except:
      print(self.file_not_found)

        
      
  def see_all_note(self):
    try:
      self.__open_file()
      length=len(self.line)
      if length == 0:
        print("empty note".upper())
      else:
        note_view="".join(self.line)
        print(note_view)
    except:
      print(self.file_not_found)


  def search_topic(self):
    search= input("enter topic number :")
    if not search.isdigit():
      print("only positive number allowed ")
      return
    search=int(search)
    try:
      self.__open_file()
      length=(len(self.line))
      if length>=search>=1 :
        print(self.line[search-1])
        print("here you go")
      else:
        print("data not available ")
    except:
      print(self.file_not_found)


  def delete_note_file(self):
    try:
      self.__open_file()
      length=len(self.line)
      if length==0:
        print("note file is already empty")
      else:
        confirm=input("are you sure you want to delete the note file ? (y/n) :").title()
        if confirm in ["Y","Yes"]:
          os.remove(self.path)
          print("note file got deleted ")
        else:
          print("note file is not deleted")  
    except:
      print(self.file_not_found)

  
  def random_note(self):
    try:
      self.__open_file()
      if len(self.line)==0:
        print(self.file_not_found)
      else:
        output=random.choice(self.line)
        print(output)
    except:
      print(self.file_not_found)


  def path_name(self):
    if os.path.exists(self.path):
      full_path=os.path.abspath(self.path)
      print(full_path, "go to this location in your file to get the file ".title())   
    else:
      print(self.file_not_found)
      


  def menu(self):
    for i,menu in enumerate(self.menu_item):
      print(f"|{i} -> {menu}")

  

    


app=Notefile()

dist_choise={
      1: app.add_note,
      2: app.remove_note,
      3: app.see_all_note,
      4: app.search_topic,
      5: app.path_name,
      6: app.delete_note_file,
      7: app.random_note,
    }
  
while True:
  app.menu()
  choise= input("enter you choice number :").strip()
  if choise.isdigit():
    choise=int(choise)
    if choise ==0:
      print("thank you for using this app")
      break
    else:
      if choise in dist_choise.keys():
        action=dist_choise.get(choise)
        action()
        continue
      else:
        print(f"{choise} is not avilible on the menu ")
        continue
  else:
    print(f"please input only number b/w 0--{app.menu_length-1}")
    continue
  