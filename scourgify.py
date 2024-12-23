import csv
import sys
from typing import Dict

def read_names_csv(before_csv: str)-> Dict:
    """_Read a csv file containing names and houses in the format 'first_name, last_name', house_

    Returns:
        Dict: _A dict with keys name and house_
    """
    name_house_dict = {}
    try:
        name_house = open(file=before_csv, mode="r")
    except FileNotFoundError:
        print(f"File doesn't exist")
        sys.exit(1)
    else:
        reader = csv.DictReader(name_house)
        
        for row in reader:
            name_house_dict.update({row['name'] : row['house']})
        name_house.close()
        return name_house_dict
def scourgify(names: Dict)-> Dict:
    pass
def write_names_csv(names: Dict)-> None:
    pass


def main()-> None:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        before_csv, after_csv = sys.argv[1:3]
    unformatted_names: Dict = read_names_csv(before_csv)
   

    #formatted_names: Dict = scourgify(unformatted_names)

    #write_names_csv(formatted_names)


if __name__ =="__main__":
    main()