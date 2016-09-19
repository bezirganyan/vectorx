#!/usr/bin/python
#
# Created by : Grigor Bezirganyan
# Email : grigor.bezirganyan98@gmail.com
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, see <http://www.gnu.org/licenses/>.

import math;

class vector:
    __m_array = [];

    def __init__(self, array):
        self.__m_array = array;

    def __add__(self, other):
        if (self.getDimension() == other.getDimension()):
            result = [];
            for ind in xrange(0, self.getDimension()):
                result.append(self.getArray(ind) \
                        + other.getArray(ind));
        else:
            raise Exception("Cannot add two vectors \
                    \nin different dimensions");
        return result;

    def __sub__(self, other):
        if (self.getDimension() == other.getDimension()):
            result = [];
            for ind in xrange(0, self.getDimension()):
                result.append(self.getArray(ind) \
                        - other.getArray(ind));
        else:
            raise Exception("Cannot substract two vectors \
                    \nin different dimensions");
        return result;

    def __mul__(self, other):
        if (self.getDimension() == other.getDimension()):
            result = [0];
            for ind in xrange(0, self.getDimension()):
                result[0] = result[0] + (self.getArray(ind) \
                        * other.getArray(ind));

        else:
            raise Exception("Cannot get the dot product of \
                    \ntwo vectors in different dimensions");
        return result;

    def __and__(self, other):
        if (self.getDimension() == other.getDimension() == 3):
            result = [];
            result.append((self.getArray(1) * other.getArray(2)) \
                    - (self.getArray(2) * other.getArray(1)))

            result.append((self.getArray(2) * other.getArray(0)) \
                    - (self.getArray(0) * other.getArray(2)))

            result.append((self.getArray(0) * other.getArray(1)) \
                    - (self.getArray(1) * other.getArray(0)))

        else:
            raise Exception("Cross Product is only possible \
                    \nin 3 dimensional vectors");
        return result;

    def __xor__(self, other):
        result = [0];
        result[0] = math.acos((self.getArray()[0] * other.getArray()[0]) \
                /(self.length() * other.length()));
        return result;

    def length(self):
        result = 0;
        for ind in xrange (0, self.getDimension()):
            result = result + self.getArray(ind) \
                    * self.getArray(ind);
        return math.sqrt(result);

    def getArray(self, ind = -1) :
        if (-1 == ind) :
            return self.__m_array;
        elif (ind >= 0):
            return self.__m_array[ind];

    def getDimension(self) :
        return self.__m_array.__len__();

def doOperation(a, op):
    if ('+' == op):
        return a[0] + a[1];
    elif ('-' == op):
        return a[0] - a[1];
    elif ('*' == op):
        return a[0] * a[1];
    elif ('&' == op):
        return a[0] & a[1];
    elif ("^" == op):
        return a[0] ^ a[1];
    else :
        return ("No such operation %s" % op)
print ("Welcome to VectorX \
        \nA simple vector calculator \
        \n\nFor calculating insert 1st vector, then operation\
        \n(or \"len\" to get the length), and then next vector\
        \n\nVector coordinates must be inputed seperated by spaces\
        \n\nOperations (op):\n+    :  addition\n-    :  substraction\
        \n*    :  dot product\n&    :  cross product\
        \n^    :  to find the angle beetween the vectors\
        \nlen  :  length\nto quit press ctrl + c\
        \n\nCreated By: Grigor Bezirganyan\nVersion 0.1")

while (True):
    print("\n\n---------------------------------------------")
    vectors = [0,0];
    a = raw_input("1:  ");
    try :
        vectors[0] = (vector(map(float, a.split())));
    except ValueError :
        print("Oops, that was not valid input")
        continue;
    op = raw_input("op: ");
    if ("len" == op):
        print ("    ________\n")
        print ("    %s" % vectors[0].length())
        vectors = [0, 0];
        continue;
    a = raw_input("2:  ")
    try :
        vectors[1] = (vector(map(float, a.split())));
    except ValueError :
        print("Oops, that was not valid input")
        continue;
    print ("    ________\n")
    try :
        result = doOperation(vectors, op);
        formattedResult = ['%g' % elem for elem in result];
    except Exception as err :
        print err
        continue;
    print ("    %s" % formattedResult);
