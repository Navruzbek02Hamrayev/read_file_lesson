#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    l=[]
    a=open(filename).read().split(",")
    for i in a:
        l.append(int(i))
    # Open the file
    # Read the file
    return l

#Print list from file
print(read_file("data.txt"))
