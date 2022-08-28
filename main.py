import sys


def is_spe(c):
    if c == '~' or c == '#' or c == '{' or c == '[' or c == '|' or c == '@' or c == ']' or c == '}' or c == '^':
        return True
    else:
        return False


def convert_spe(c):
    if c == '~':
        return "DigiKeyboard.sendKeyStroke(KEY_2, MOD_ALT_RIGHT);"
    elif c == '#':
        return "DigiKeyboard.sendKeyStroke(KEY_3, MOD_ALT_RIGHT);"
    elif c == '{':
        return "DigiKeyboard.sendKeyStroke(KEY_4, MOD_ALT_RIGHT);"
    elif c == '[':
        return "DigiKeyboard.sendKeyStroke(KEY_5, MOD_ALT_RIGHT);"
    elif c == '|':
        return "DigiKeyboard.sendKeyStroke(KEY_6, MOD_ALT_RIGHT);"
    elif c == '@':
        return "DigiKeyboard.sendKeyStroke(KEY_0, MOD_ALT_RIGHT);"
    elif c == ']':
        return "DigiKeyboard.sendKeyStroke(45, MOD_ALT_RIGHT);"
    elif c == '}':
        return "DigiKeyboard.sendKeyStroke(46, MOD_ALT_RIGHT);"
    else:
        return "La touche " + c + " n'est pas supportée"


def convert(string):
    string_list = list(string)
    for char in range(len(string_list)):
        if string_list[char] == 'a':
            string_list[char] = 'q'
        elif string_list[char] == 'z':
            string_list[char] = 'w'
        elif string_list[char] == 'q':
            string_list[char] = 'a'
        elif string_list[char] == 'm':
            string_list[char] = ';'
        elif string_list[char] == 'w':
            string_list[char] = 'z'
        elif string_list[char] == 'A':
            string_list[char] = 'Q'
        elif string_list[char] == 'Z':
            string_list[char] = 'W'
        elif string_list[char] == 'Q':
            string_list[char] = 'A'
        elif string_list[char] == 'M':
            string_list[char] = ':'
        elif string_list[char] == 'W':
            string_list[char] = 'Z'
        elif string_list[char] == '1':
            string_list[char] = '!'
        elif string_list[char] == '2':
            string_list[char] = '@'
        elif string_list[char] == '3':
            string_list[char] = '#'
        elif string_list[char] == '4':
            string_list[char] = '$'
        elif string_list[char] == '5':
            string_list[char] = '%'
        elif string_list[char] == '6':
            string_list[char] = '^'
        elif string_list[char] == '7':
            string_list[char] = '&'
        elif string_list[char] == '8':
            string_list[char] = '*'
        elif string_list[char] == '9':
            string_list[char] = '('
        elif string_list[char] == '0':
            string_list[char] = ')'
        elif string_list[char] == '°':
            string_list[char] = '_'
        elif string_list[char] == '&':
            string_list[char] = '1'
        elif string_list[char] == 'é':
            string_list[char] = '2'
        elif string_list[char] == '"':
            string_list[char] = '3'
        elif string_list[char] == '\'':
            string_list[char] = '4'
        elif string_list[char] == '(':
            string_list[char] = '5'
        elif string_list[char] == '-':
            string_list[char] = '6'
        elif string_list[char] == 'è':
            string_list[char] = '7'
        elif string_list[char] == '_':
            string_list[char] = '8'
        elif string_list[char] == 'ç':
            string_list[char] = '9'
        elif string_list[char] == 'à':
            string_list[char] = '0'
        elif string_list[char] == ')':
            string_list[char] = '-'
        elif string_list[char] == ',':
            string_list[char] = 'm'
        elif string_list[char] == '?':
            string_list[char] = 'M'
        elif string_list[char] == '²':
            string_list[char] = '`'
        elif string_list[char] == '$':
            string_list[char] = ']'
        elif string_list[char] == '£':
            string_list[char] = '}'
        elif string_list[char] == 'ù':
            string_list[char] = '\\\"'
        elif string_list[char] == '%':
            string_list[char] = '\''
        elif string_list[char] == '*':
            string_list[char] = '\\\\'
        elif string_list[char] == 'µ':
            string_list[char] = '|'
        elif string_list[char] == ';':
            string_list[char] = ','
        elif string_list[char] == '.':
            string_list[char] = '<'
        elif string_list[char] == ':':
            string_list[char] = '.'
        elif string_list[char] == '/':
            string_list[char] = '>'
        elif string_list[char] == '!':
            string_list[char] = '/'
        elif string_list[char] == '§':
            string_list[char] = '?'
    return ''.join(string_list)


Tab = [None] * 256
i_pos = 0
for i in range(1, len(sys.argv)):
    Tab[i_pos] = sys.argv[i]
    i_pos += 1
UserInput = ' '.join(Tab[:i_pos])
ListUserInput = list(UserInput)
IndexList = 0


if len(UserInput) == 0:
    print('You must enter a string')
else:
    if is_spe(ListUserInput[0]):
        print(convert_spe(ListUserInput[0]))
        IndexList += 1
    else:
        while IndexList < len(ListUserInput):
            BufferList = [None] * 256
            BufferList[0] = "DigiKeyboard.print(\""
            IndexBuffer = 1
            while IndexList < len(ListUserInput):
                if not is_spe(ListUserInput[IndexList]):
                    BufferList[IndexBuffer] = convert(ListUserInput[IndexList])
                    IndexList += 1
                    IndexBuffer += 1
                else:
                    break
            BufferList[IndexBuffer] = "\");"
            print(''.join(BufferList[:IndexBuffer + 1]))
            if IndexList < len(ListUserInput):
                print(convert_spe(ListUserInput[IndexList]))
                IndexList += 1
        print("DigiKeyboard.println();")
