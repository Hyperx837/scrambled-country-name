from collections import Counter


def get_country(user_country):
    countries_list = (x.strip().lower() for x in open('countries.txt').readlines())
    countries = (country for country in countries_list
                 if len(country.replace(' ', '')) == len(user_country))

    for country in countries:
        if all(country.replace(' ', '').count(char) == occur
               for char, occur in Counter(user_country).items()):
            return country.title()


while True:
    inp = input('Gibberish: ').lower().replace(' ', '')
    if inp == 'end':
        break

    print('\n', get_country(inp), '\n\n')
