import math
import string
import re

def is_multiple_of_9(n):
    """Return True if n is a multiple of 9; False otherwise."""
    return n % 9 == 0


def next_prime(m):
    """Return the first prime number p that is greater than m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    if m <= 1:
        return 2

    prime = m
    found = False

    while not found:
        prime = prime + 1
        if is_prime(prime):
            found = True
    return prime


def is_prime(n):

    if n == 1 or n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    a = float(a)
    b = float(b)
    c = float(c)

    r = b**2 - 4*a*c

    if r > 0:
        r0 = (((-b) + math.sqrt(r))/(2*a))
        r1 = (((-b) - math.sqrt(r))/(2*a))
        tup = (r0, r1)
        return tup
    elif r == 0:
        r0 = -b / 2*a
        return r0
    else:
        return "complex"


def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    For example, [0, 1, 2, 3, 4, 5, 6, 7] => [0, 4, 1, 5, 2, 6, 3, 7]"""
    left  = []
    right = []
    new_list = even_list

    if len(even_list) == 0 or len(even_list) == 1:
        return even_list

    half = int(len(new_list)/2)
    for i in range(0, half):
        left.append(new_list[i])
        right.append(new_list[half + i])
 
    i = 0
    k = 0
    while i < len(even_list):
        new_list[i] = left[k]
        new_list[i+1] = right[k]
        i += 2
        k += 1

    return even_list


def triples_list(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 3."""
    output_list = [ num*3 for num in input_list]
    return output_list


def double_consonants(text):
    """Return a new version of text, with all the consonants doubled.
    For example:  "The *BIG BAD* wolf!" => "TThhe *BBIGG BBADD* wwollff!"
    For this exercise assume the consonants are all letters OTHER
    THAN A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""

    newtext = ""
    for char in text:
        if char not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U") and char.isalpha():
            newtext += char + char
        else:
            newtext += char
    return newtext


def count_words(text):
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', '*', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ]  ).
    Convert all the letters to lower-case before the counting."""
    lowertext = text.lower()
    newtext = re.findall(r"[a-z0-9\-\+\*\/\@\#\%\']+|[a-z]", lowertext)
    #newtext =  re.split('; |, |\*|\n',lowertext)
    wordfreq = [newtext.count(p) for p in newtext]
    return dict(list(zip(newtext, wordfreq)))


def make_cubic_evaluator(a, b, c, d):
    """When called with 4 numbers, returns a function of one variable (x)
    that evaluates the cubic polynomial
    a x^3 + b x^2 + c x + d.
    For this exercise Your function definition for make_cubic_evaluator
    should contain a lambda expression."""
    return lambda x: a * x * x * x + b * x * x + c * x + d


class Polygon:
    """Polygon class."""
    def __init__(self, n_sides, lengths=None, angles=None):
        # Additional code will go here.
        self.n_sides = n_sides
        self.lengths = lengths
        self.angles = angles

    @staticmethod
    def _all_the_same(items):
        return all(x == items[0] for x in items)

    def is_rectangle(self):
        if self.n_sides is 4 and self.angles is None:
            return None
        elif self.n_sides is 4 and self._all_the_same(self.angles):
            return True
        else:
            return False

    def is_rhombus(self):
        if self.n_sides == 4 and self.lengths is None:
            return None
        elif self.n_sides == 4 and self._all_the_same(self.lengths):
            return True

        else:
            return False

    def is_square(self):
        if self.is_rectangle() is False or self.is_rhombus() is False:
            return False
        elif self.n_sides == 4 and (self.angles is None or self.lengths is None):
            return None
        else:
            return True

    def is_regular_hexagon(self):
        if self.n_sides == 6 and self.angles is not None and self._all_the_same(self.angles) and self.lengths is not None and self._all_the_same(self.lengths):
            return True
        # elif self.n_sides == 6 and self.lengths is not None and self._all_the_same(self.lengths):
        #     return True
        elif self.n_sides == 6 and self.lengths is not None and self._all_the_same(self.lengths):
            return None
        elif self.n_sides == 6 and self.angles is not None and self._all_the_same(self.angles):
            return None
        else:
            return False

    def is_isosceles_triangle(self):
        if self.n_sides == 3 and self.angles is None and self.lengths is None:
            return None
        elif self.n_sides == 3 and self.lengths is not None and (self.lengths[1] == self.lengths[0] or self.lengths[2] == self.lengths[0] or self.lengths[1] == self.lengths[2]):
            return True
        elif self.n_sides == 3 and self.angles is not None and (self.angles[1] == self.angles[0] or self.angles[2] == self.angles[0] or self.angles[1] == self.angles[2]):
            return True
        else:
            return False

    def is_equilateral_triangle(self):
        if self.n_sides == 3 and self.angles is None and self.lengths is None:
            return None
        elif self.n_sides == 3 and self.lengths is not None and self._all_the_same(self.lengths):
            return True
        elif self.n_sides == 3 and self.angles is not None and self._all_the_same(self.angles):
            return True
        else:
            return False

    def is_scalene_triangle(self):

        if self.n_sides == 3 and self.lengths is not None and self.lengths[1] != self.lengths[0] != self.lengths[2]:
            return True
        elif self.n_sides == 3 and self.angles is not None and self.angles[1] != self.angles[0] != self.angles[2]:
            return True
        elif self.is_isosceles_triangle() or self.is_equilateral_triangle():
            return False
        elif self.n_sides == 3: #self.is_isosceles_triangle() is False and self.is_equilateral_triangle() is False:
            return None
        else:
            return False



