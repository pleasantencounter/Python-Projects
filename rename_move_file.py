import subprocess
import shutil
from MovieSerieTorrent import *
path = "<current path of file>"
dest= "<desired path of file>"
command = subprocess.run(['ls',f'{path}'],stdout=subprocess.PIPE)
movie_list=[]

def movie_title():
    for line in command.stdout.splitlines():
        movie = line.decode("utf-8")
        parse_movie = movie.split(" ")
        movie_list.append(parse_movie)
    return movie_list

def parse_title(title):
    year = Parser().parse(title)[0]['year']
    title = Parser().parse(title)[0]['title']
    return title + "(" + year + ")" 

def joinString(string):
    return " ".join(string)
   
movie_title = movie_title()

for title in movie_title:
    src = path + joinString(title)
    newTitle = path + parse_title(str(title))
    os.rename(src,newTitle)
    shutil.move(newTitle,dest)
