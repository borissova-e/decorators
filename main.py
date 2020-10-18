import datetime

import hw_countries


def get_performance(path):
    def decorator(old_function):
        def new_function(input_file, output_file):
            start = datetime.datetime.now()
            result = old_function(input_file, output_file)
            with open(path, 'a') as file:
                file.write(
                    f"Дата и время вызова функции -  {start},\nИмя функции - {old_function.__name__},\nАргументы  - {input_file}, {output_file}\nВозвращаемое значение - {result}\n\n")
            return result

        return new_function

    return decorator

@get_performance('performance.log')
def make_hw(file1, file2):
    input_file = file1
    output_file = file2
    hw_countries.get_links(input_file, output_file)


if __name__ == '__main__':
    make_hw('files\countries.json', 'files\links.txt')
