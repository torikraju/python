
"""
    r: Read access only
    w: Write access only
    r+: Read and Write access only
    x: Write Access only: Exclusive creation, fails if file exists
    b: Open in binary mode 
"""

file_name = 'demo.txt'

# writing to file
def write_to_file(content, file_name):
    f = open(file_name, mode='w')
    f.write(content+'\n')
    f.close()


# append to file
def append_to_file(content, file_name):
    f = open(file_name, mode='a')
    f.write(content+'\n')
    f.close()


# read from file
def read_single_from_file(file_name):
    f = open(file_name, mode='r')
    file_content = f.readline()
    f.close()
    return file_content

# read from file
def read_multiple_line_from_file(file_name):
    f = open(file_name, mode='r')
    file_content = f.readlines()
    f.close()
    return file_content

# read from file with keyword
def read_file_with(file_name):
    with open(file_name, mode='r') as f:
        file_content = f.readlines()
        return file_content


write_to_file('Hello from python', file_name)
append_to_file('append this line', file_name)
print(read_single_from_file(file_name))
print(read_multiple_line_from_file(file_name))
print([el[:-1] for el in read_multiple_line_from_file(file_name)])
print(read_file_with(file_name))
