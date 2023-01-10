import textwrap

def wrap(string, max_width):
    lists =[*string]
    nstring ="" + lists[0]
    for i in range(1, len(lists)):
        if i % max_width == 0:
            nstring += '\n'
            nstring += lists[i]
        else:
            nstring += lists[i]
      
    return nstring

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
