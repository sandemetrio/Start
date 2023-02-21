def put_in_the_box(width=20, symbol='$'):
    def inner(function):
        def wrapper(sring):
            list_of_words = function(sring).split()

            longest = len(sorted(list_of_words, key=lambda x: len(x),reverse=True)[0])
            if width-2 < longest:
                print(f'Min width for your string {longest+2} ')
                return

            print(symbol*width)
            for word in list_of_words:
                print(f'{symbol}{word.center(width-2)}{symbol}')
            print(symbol*width)
        return wrapper
    return inner


@put_in_the_box(width=9)
def string_printer(text: str):
    if isinstance(text, str):
        return text
    else:
        print('It is not a string')


def mian():
    list_1 = ['qwe', 'qweqwe', 'aweqerq', 'dfghjkjhvcvbh']
    string_printer('Hello this is my string')

if __name__ == '__main__':
    mian()