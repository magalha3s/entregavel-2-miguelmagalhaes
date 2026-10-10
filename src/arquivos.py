import csv
import cv2 as cv
from pathlib import Path


def get_images_path() -> list:
    # Return a List containing the images Paths sorted by Name
    return order_names(list(Path("imagens/").glob("*.jpg")))

def convert_int(l : list[int]):
    return [int(x) for x in l]


def csv_read() -> dict:
    storage={}

    # Read CSV raw data
    try:
        with Path("dados/anotacoes.csv").open() as csv_file:
            raw_data = list(csv.reader(csv_file))[1:]
    except FileNotFoundError as error:
        raise FileNotFoundError('"anotacoes.csv" not found')
    
    # Organize the CSV data per image in a Dict
    for line in raw_data:
        line=[line[0]]+convert_int(line[1:])
        storage[line[0]]=storage.get(line[0],[])+[line[1:]]
    return  storage

def cwd() -> Path:
    # Print Current Working Directory
    return Path().cwd()

def pop_numbers(l:str) -> str:
    l=list(l)
    new_l=[]
    for character in l:
        if character in ["0","1","2","3","4","5","6","7","8","9","0","_","-"]:
            pass
        else: new_l.append(character)

    return "".join(new_l)


## Auxiliary Functions

def order_names(name_list:list[Path]) -> list:
    sorted_list=[]

    while len(name_list) > 0:
        min = pop_numbers(name_list[0].name)
        pos = 0

        for index,path in enumerate(name_list[1:]):
            if min[0] == pop_numbers(path.name[0]):
                try:
                    i=1
                    while min[i] == pop_numbers(path.name)[i]:
                        i+=1
                    if ord(min[i]) >= ord(pop_numbers(path.name)[i]):
                        min = pop_numbers(path.name)
                        pos = index + 1
                except IndexError:
                    if len(min) > len(pop_numbers(path.name)):
                        min = pop_numbers(path.name)
                        pos = index + 1
                    
            elif ord(min[0]) >= ord(pop_numbers(path.name)[0]):
                min = pop_numbers(path.name)
                pos = index + 1
            else:
                pass

        sorted_list.append(name_list.pop(pos))
    return sorted_list

        


