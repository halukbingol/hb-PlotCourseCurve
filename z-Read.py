import csv


def readData():
    """
    Read data.

    :return: (courseName, arrayOfFloats)
    """
    array = []
    with open('dataTest.txt', 'r') as file:
        reader = csv.reader(file)
        is_first_line = True
        course = 'no'
        for row in reader:
            if is_first_line:
                course = row[0]
                is_first_line = False
            else:
                array.append(float(row[0]))
    return (course, array)


(course, data) = readData()
print(course)
print(data)
