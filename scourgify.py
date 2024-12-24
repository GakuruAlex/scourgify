import csv
import sys
from typing import Dict, List

def read_names_csv(before_csv: str)-> Dict:
    """_Read a csv file containing names and houses in the format 'first_name, last_name', house_

    Returns:
        Dict: _A dict with keys name and house_
    """
    name_house_dict = {}
    try:
        name_house = open(file=before_csv, mode="r")
    except FileNotFoundError:
        sys.exit(f"Could not read {before_csv}")
    except csv.Error:
        sys.exit(f"Error in file {before_csv}")
    else:
        reader = csv.DictReader(name_house)
        for row in reader:
            name_house_dict.update({row['name'] : row['house']})
        name_house.close()
        return name_house_dict
    
def scourgify(name_house: Dict)-> List:
    """_Given a dictioanry with name been 'first, last' and house been house , format dict as first, last, house_

    Args:
        name_house (Dict): _Names of student as keys with their coresponding house as value_

    Returns:
        List: _List in the whose values are a dict in the form {'first_name': value, 'last_name': value, 'house': value}_
    """
    names_houses = []

    for name, house in name_house.items():
        last_name, first_name = name.strip("").split(",")
        names_houses.append({'first':first_name, 'last':last_name,'house': house})
    return names_houses

def write_names_csv(names_houses: List, after_csv: str)-> None:
    """_Write a a list of dictionaries to a csv_

    Args:
        names_houses (List): _List with the dictionary containing first name, last name and house of a person_
        after_csv (str): _Name of csv to write to_
    """
    
    csv_file = open(file=after_csv, mode="w", newline='')

    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(f=csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for item in names_houses:
        writer.writerow({'first': item['first'], 'last': item['last'], 'house': item['house']})
    csv_file.close()




def main()-> None:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        before_csv, after_csv = sys.argv[1:3]
        unformatted_names: Dict = read_names_csv(before_csv=before_csv)
    

        formatted_names: Dict = scourgify(name_house=unformatted_names)
        

        write_names_csv(names_houses=formatted_names, after_csv=after_csv)


if __name__ =="__main__":
    main()