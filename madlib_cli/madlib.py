

def read_template(path: str) -> str:

    if path != "assets/text1.txt":

        return FileNotFoundError('no path found')

    with open(path, 'r') as file:

        file_content = file.read()

    return file_content


def merge(string,word):
    statment=string.format(*word)
    
    with open('assets/dark_and_stormy_night_template.txt','w') as f:
     f.write(statment)
     
    return statment