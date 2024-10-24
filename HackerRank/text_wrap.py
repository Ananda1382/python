import textwrap

def wrap(string, max_width):
    wrapped = textwrap.fill(string, max_width )
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    if 0 < len(string) < 1000 and 0 < max_width < len(string):
        result = wrap(string, max_width)
        print(result)