import json


class country_from_json:
    def __init__(self, json_file):
        self.json_file = json_file
        self.country_index = 0
        self.current_country = None

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.json_file, encoding="utf-8") as f:
            data = json.load(f)
            if self.country_index == len(data):
                raise StopIteration
            self.current_country = data[self.country_index]
            country_link = self.current_country['name']['official'] + ' - ' + 'https://en.wikipedia.org/wiki/' + \
                           self.current_country['name']['common'].replace(' ', '_') + '\n'
            self.country_index += 1
        return country_link


def get_links(input_file, output_file):
    for country_link in country_from_json(input_file):
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(country_link)


if __name__ == '__main__':
    # json_file = 'files\countries.json'
    # output_file = 'files\links.txt'
    get_links('files\countries.json', 'files\links.txt')
