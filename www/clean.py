import argparse

def clean_code(code):
    code = ' '.join(code.split())
    
    code = '\t'.join(code.split('\t'))
    
    code = '\n'.join(code.split('\n'))
    
    return code

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="path to file")
    args = parser.parse_args()

    with open(args.filepath, 'r') as file:
        code = file.read()

    cleaned_code = clean_code(code)
    
    print(cleaned_code)

if __name__ == "__main__":
    main()
