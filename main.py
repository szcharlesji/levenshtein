from levenshtein import calc_levenshtein_distance


def main():
    string_a = 'Execution'
    string_b = 'Intention'
    print("The Levenshtein Distance between " + string_a + " and " + string_b + " is ", end='')
    print(calc_levenshtein_distance(string_a, string_b))


if __name__ == '__main__':
    main()
