# MIT License
#
# Copyright (c) 2025 programmer-pro-123
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
This file contains the function words_frec. This function counts the number
of occurrences of the words in the input file, and returns a csv file with
the words of the input file and its number of occurrences.

In this case, we understand a word as a substring made by letters a-z, case
insensitive.
"""

def words_frec(str1, str2):
  """
  The parameter str1 is the input file, which is a txt file. The parameter str2
  is the output file, which is a csv file.
  """
  
    alphabet_space = (' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z') # A variable with the letters of the
                                                             # alphabet and the character space.
                                                             # We will use this variable to identify the words.

    str3 = ''    # A variable with an empty string. We will use this variable to add each word of the input file.

    with open(str1, 'r') as fr, open(str2, 'w') as fw: # We open the input file to read, and the output file to write.
        for line in fr:
            for element in line:
              """
              We loop through each character of each line of the input file
              """
                if element.lower() in abecedario_espacio: 
                  # We check if the character is a letter or a space character.
                    str3 += element.lower()    # In case of a letter of a space character, we add it to the variable str3.
                else:
                    str3 += ' '                # In other case, we add a space character to the variable str3

        dicc = dict()                          # An empty dictionary. We will use it to add each word as key, and
                                               # its occurrences as values.
        for word in str3.split():
            dicc[word] = 0
        for word in str3.split():
            dicc[word] += 1

        for word in sorted(dicc):
            print(f"{word},{dicc[word]}", end='\n', file=fw)
