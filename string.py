# String
input = 'Here is the input text '
print('String', input[2])
print(input[2:6])
print(input[12:])
print(input[:7])
print(input[:-5])

def simple_print(txt, input):
    print(txt, ': ', input)

simple_print('Uppercase', input.upper())
simple_print('Lowercase', input.lower())
simple_print('strip', input.strip())

txt = 'Hello {}'

name = 'gokul'.upper()
welcome = 'welcome!'
simple_print('String' , txt.format(name))

txt = 'Hello {1} {0}'
simple_print('String' , txt.format(name, welcome))

txt = 'hello Gokul welcome'
simple_print('capitalize' , txt.capitalize())
simple_print('casefold' , txt.casefold())
simple_print('center' , txt.center(1))
simple_print('count' , txt.count('l'))
simple_print('encode' , txt.encode())
simple_print('endswith' , txt.endswith('e'))
simple_print('endswith' , txt.endswith('el'))
