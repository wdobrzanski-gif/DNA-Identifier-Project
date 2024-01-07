"""
Module: dna_profiler
 
A program to use short tandem repeats (STRs) to identify a person using their
DNA.

Authors:
    1) Toan Thai - tthai@sandiego.edu
    2) Will Dobrzanski - wdobrzanski@sandiego.edu
"""

from typing import Tuple, List, Dict, Union


def read_dna_sequence(sequence_filename: str) -> str:
    """ 
    Reads in the DNA sequence from a specified file.

    Parameters:
    sequence_filename (str): The filename of the file containing the DNA sequence.

    Returns:
    str: The DNA sequence read from the file>

        Argv:
            sequence_filename(str)l: 
        Return:
            (str) the DNA sequence

        >>> read_dna_sequence("alice.txt")
        'AGACGGGTTACCATGACTATCTATCTATCTATCTATCTATCTATCTATCACGTACGTACGTATCGAGATAGATAGATAGATAGATCCTCGACTTCGATCGCAATGAATGCCAATAGACAAAA'
    """
    with open(sequence_filename) as f:
        content = f.readline().strip()
    return content


def create_dna_profiles(profiles_filesname: str) -> tuple[list[str], dict[str, list[int]]]:
    """ 
    Reads a DNA profiles file and creates a dictionary of profiles.

    Parameters:
    profiles_filesname (str): The filename of the DNA profiles file.

    Returns:
    tuple[list[str], dict[str, list[int]]]: A tuple containing a list of STR names and a dictionary of profiles.
        Argv:
           profiles
        Return:

        >>> create_dna_profiles("dna_database.csv")
        (['AGAT', 'AATG', 'TATC'], {'Alice': [5, 2, 8], 'Bob': [3, 7, 4], 'Charlie': [6, 1, 5]})
    """

    str_names = []  # List to store the names of the STRs
    profiles = {}  # Dictionary to store the profiles

    with open(profiles_filesname) as f:
        header_line = f.readline().strip()
        fields = header_line.split(",")
        str_name = fields[1:]  # Extract STR names from the header line

        # Iterate through each line in the file
        for line in f:
            fields = line.split(",")
            name = fields[0]  # Extract the person's name
            # Extract the counts of STRs for the person
            counts = [int(x) for x in fields[1:]]
            # Add the counts to the profiles dictionary
            profiles[name] = counts

        # Return the STR names and profiles as a tuple
        return str_name, profiles


def find_max_consecutive(dna: str, target: str) -> int:
    '''
    Finds the maximum cosecutive occurences of a target string in the given DNA sequence.

    Parameters:
    dna (str): The DNA sequence to search within.
    target (str): The target string to find and count.

    Returns:
    int: The maximum consecutive count of the target string in the DNA sequence.

    '''

    max_count = 0  # Variable to store the maximum consecutive count of the target string
    count = 0  # Variable to store the current consecutive count of the target string
    i = 0  # Variable to iterate through the DNA sequence

    # Iterate through the DNA sequence
    while i < len(dna):

        # Check if the current substring matches the target string
        if dna[i:i+len(target)] == target:
            count += 1  # Increment the count if there's a match
            i += len(target)  # Move the index to the end of the target string
            if count > max_count:
                max_count = count  # Update the maximum count if needed

        else:
            count = 0  # Reset the count if no match is found
            i += 1  # Move to the next character in the DNA sequence
    return max_count  # return the maximum consecutive count of the target string


def identify_dna(mystery_dna: str, profiles: dict, str_names: list[str]) -> str:
    '''
    Identifies the DNA by comparing the given mystery DNA sequence with known profiles.

    Parameters:
    mystery_dna (str): The DNA sequence to be identified.
    profiles (dict): A dictionary contian known DNA profiles.
    str_names (list[str]): A list of DNA short Tandem Repeat (STR) names to consider

    Returns:
    str: The identified DNA profile name or "No Match" if no match is found.
    '''

    result = []  # A list to store the consective counts of STRs in the mystery DNA

    # Iterate through each STR name in the provided list
    for STR in str_names:
        # Find the max consecutive count of the current STR
        con_max = find_max_consecutive(mystery_dna, STR)
        # Append the max consecutive count to the result list
        result.append(con_max)

    # Iterate through each profile in the provided profiles dictionary
    for k, v in profiles.items():
        # If the profile matches the result (consecutive counts of STRs)
        if v == result:
            return k  # Return the identified DNA profile name
        else:
            return "No Match"  # Return "No Match" is no matching profile is founded


def main(sequence_filename: str, profiles_filename: str) -> None:
    '''
    Calls the fuctions to print out the name of the person whose DNA matches that given in the
    sequence_filename file. 

    Parameters: 
    sequency_filename(str): The name of the file containing a DNA sequence.
    profiles_filename(str): The name of the file the information about the STRs for each person 

    Returns:
    None
    '''
    # Function to read DNA aequence from the specified file
    a = read_dna_sequence(sequence_filename)

    # Function to create DNA profiles from the specified file
    # Returns a tuple with profiles (b) and a value (k)
    b, k = create_dna_profiles(profiles_filename)

    # Function to identify DNA using the sequence (a), profiles (b), and value (k)
    c = identify_dna(a, k, b)

    # Print the result of the DNA identification
    print(c)


# Write your new functions below this point.
# Recall that all functions need type hints for all parameters and the return,
# AND must have docstrings in the correct format.
# keep the following code at the END of your file, as per convention
if __name__ == "__main__":
    main('alice.txt', 'dna_database.csv')
