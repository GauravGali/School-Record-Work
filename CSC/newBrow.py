import webbrowser as webb

def concated(word):
    seped = word.split()
    joined = ''

    for i in seped:
        joined += i
        if i == seped[-1]:
            break
        joined += '+'
    return joined


search = input('Search : ')
searched = concated(search)

webb.open_new_tab(f'https://search.brave.com/search?q={searched}&source=desktop')
