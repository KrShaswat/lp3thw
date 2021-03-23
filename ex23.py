import sys
# imported whole sys library and used only argv?
script, encoding, error = sys.argv
# function name main take the file, encoding type and errors
# main function uses another function inside it i.e print_line
def main(language_file, encoding, errors):
    line = language_file.readline()#reads a line
    
    if line:#if there is a line then the code below runs
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

#print_line function takes line, encoding, errors
def print_line(line, encoding, errors):
    next_lang =line.strip()# apprently just returns a string
    raw_bytes = next_lang.encode(encoding, errors=errors)#encode function returns the input in the mentioned encoding
    cooked_string = raw_bytes.decode(encoding, errors=errors)#decode from the encoded string

    print(raw_bytes,"<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

#https://learnpythonthehardway.org/python3/languages.txt