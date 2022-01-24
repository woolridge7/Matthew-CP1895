animals = { 'a': ['aardvark'], 'b' : ['baboon'], 'c' : ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

a_dict = {'u': [10, 15, 5, 2, 6], 'B': [15]}

def how_many(animals):
    total_length = 0
    for item in a_dict.values():
        total_length += len(item)
    print(total_length)

    i = len(list(animals['a']))
    y = len(list(animals['b']))
    d = len(list(animals['c']))
    e = len(list(animals['d']))
    x = i + y + d + e
    print(x)

def main():
    how_many(animals)

if __name__ == "__main__":
    main()
