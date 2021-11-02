
import re


# def read_template(path: str) -> str:

#     if path != "assets/text1.txt":

#         return FileNotFoundError('no path found')

#     with open(path, 'r') as file:

#         file_content = file.read()
#         words = re.findall('\{.*?\}', file_content)

#         print(words)
#         for i in range(len(words)):
#             name = input("Enter an "[i]+"!")
#             print(name)
#     return file_content

def read_template(fpath: str) -> str:

    if fpath != "assets/text1.txt":

        raise FileNotFoundError('no path found')

    with open(fpath, 'r') as file:

        file_content = file.read()

    return file_content.strip()

# read_template('assets/text1.txt')


def parse_template(file_content: str):

    parse = re.findall(r'\{(.*?)\}', file_content)

    for item in parse:

        file_content = file_content.replace((item), '', 2)

    return file_content, tuple(parse)



def merge(file_content, parse):

    updatedText = file_content.format(*parse)

    with open('assets/text3.txt', 'w') as result:

        result.write(updatedText)

    return updatedText
