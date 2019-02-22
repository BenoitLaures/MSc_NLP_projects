import glob
import re


def display_data(data, number_of_lines=5):
    """
    Display the dataset line by line to check the read_dataset function
    :param data:
    :param number_of_lines:
    :return:
    """
    i = 0
    while i < number_of_lines:
        print(data[i])
        i += 1


def read_dataset(
        path_to_dataset_folder='data/1-billion-word-language-modeling-benchmark-r13output/training-monolingual.tokenized.shuffled',
        number_lines=10 ** 6):
    """
    Read the dataset
    :param path_to_dataset_folder: str, path
    :param number_lines: lines to be extracted (10**6 by default)
    :return: array of words
    """

    # Getting files in the dataset folder
    files = glob.glob(path_to_dataset_folder + '/*')

    # Sorting to be sure to have alphabetical order
    files.sort()

    # Printing number of found files
    print("Found", str(len(files)), "files to read.")

    # Init regex to remove non alphanumerical characters, still we keep spaces and '
    regex = re.compile("[^a-z ']+")

    data = []
    id_file = 0
    while len(data) < number_lines:
        with open(files[id_file], encoding='utf-8') as current_file:
            print("Opening file n°" + str(id_file) + ". Wrote " + str(len(data)) + "/" + str(number_lines))

            # Init line
            line = current_file.readline()

            while line and len(data) < number_lines:
                # While we are not in the end of the file and we haven't filled the data list

                # Removing unwanted characters
                processed_line = regex.sub('', line.lower())
                final_line = processed_line.replace("  ", " ").split(" ")
                final_line.pop()
                data.append(final_line)

                # refresh line value
                line = current_file.readline()
        # Moving to new file
        id_file += 1
    print("Finished reading")
    return data

