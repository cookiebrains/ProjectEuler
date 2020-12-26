from utilz.alphabet_values_dictionary import alphabet_values_dict as dict


def get_names(file_path):
    with open(file_path) as file:
        names = file.read().replace('"', '')
    return names


def alphabetize(names):
    long_string = names.replace(',', ' ')
    alphabetized_list = [name.lower() for name in (long_string.split())]
    return sorted(alphabetized_list)


class Name:
    alphabetic_value = 0
    total_value = 0

    def __init__(self, name, place_value):
        self.place_value = place_value
        self.name = name
        self.__init_alphabetic_value()
        self.__init_total_value()

    def __init_total_value(self):
        self.total_value = self.place_value * self.alphabetic_value

    def __init_alphabetic_value(self):
        value = 0
        for letter in self.name:
            value += dict[letter]
        self.alphabetic_value = value


def solution(alphabetized_list):
    counter = 1
    running_total = 0
    for name in alphabetized_list:
        tot_value = Name(name, counter).total_value
        counter += 1
        running_total += tot_value
    return running_total


def run():
    a = (get_names('input_files/p022_names.txt'))
    b = (alphabetize(a))
    print(solution(b))

    #
    # colin = Name('colin', 234)
    # print(colin.alphabetic_value)
    # print(colin.total_value)

    # name23 = Name('Colin', 234)
    # print(name23.total_value())
