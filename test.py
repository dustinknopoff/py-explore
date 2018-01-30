def main():
    string = 'my name is %j and %h'
    print(err(string))

def err(template):
    newStr = ''
    myiter = iter(range(0, len(template)))
    for i in myiter:
        print(i)
        if template[i] is '%' and template[i + 1] is 't':
            return True;
        elif template[i] is '%' and (template[i+1] != 't' or template[i+1] != 'h'):
            return False;

if __name__ == '__main__':
    main()