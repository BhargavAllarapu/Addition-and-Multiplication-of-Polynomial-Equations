class Node:
    def __init__(self, coefficient = None, exponent = None):
        self.coefficient = coefficient
        self.exponent = exponent
        self.nextval = None

class Polynomial:
    def __init__(self):
        self.headval = None

    def DegreeOfPolynomial(self):
        if self.headval is None:
            return -1
        else:
            return self.headval.exponent

    def printPoly(self):
        expression = ''
        printval = self.headval
        while printval is not None:
            expression = expression+" + "+str(printval.coefficient)+" x^"+str(printval.exponent)
            printval = printval.nextval
        return expression[3:]

    def insertNode(self, coefficient, exponent):
        if self.headval is None:
            term = Node(coefficient, exponent)
            self.headval = term
            return term
        else:
            term = Node(coefficient, exponent)
            lastnode = self.headval
            while lastnode.nextval:
                lastnode = lastnode.nextval
            lastnode.nextval = term
            return term
        return None
    def __add__(self, rhs):
        polysum = Polynomial()
        nodeA = self.headval
        nodeB = rhs.headval
        while nodeA is not None and nodeB is not None:
            if nodeA.exponent > nodeB.exponent:
                degree = nodeA.exponent
                coefficient = nodeA.coefficient
                nodeA = nodeA.nextval
            elif nodeA.exponent < nodeB.exponent:
                degree = nodeB.exponent
                coefficient = nodeB.coefficient
                nodeB = nodeB.nextval
            else:
                degree = nodeB.exponent
                coefficient = int(nodeA.coefficient) + int(nodeB.coefficient)
                nodeA = nodeA.nextval
                nodeB = nodeB.nextval
            polysum.insertNode(coefficient, degree)
        return polysum
    def __mul__(self, rhs):
        polymul = Polynomial()
        nodeA = self.headval
        while nodeA is not None:
            nodeB = rhs.headval
            while nodeB is not None:
                coefficient = int(nodeA.coefficient) * int(nodeB.coefficient)
                degree = int(nodeA.exponent) + int(nodeB.exponent)
                polymul.insertNode(coefficient, degree)
                nodeB = nodeB.nextval
            nodeA = nodeA.nextval
        return polymul.termMultiply()
    def termMultiply(self):
        nodeA = self.headval
        while nodeA is not None and nodeA.nextval is not None:
            nodeB = nodeA.nextval
            while nodeB is not None:
                if nodeA.exponent == nodeB.exponent:
                    nodeA.coefficient = int(nodeA.coefficient) + int(nodeB.coefficient)
                    nodeA.nextval = nodeB.nextval
                    nodeB.nextval = None
                    del nodeB
                    nodeB = nodeA.nextval
                else:
                    nodeB = nodeB.nextval
            nodeA = nodeA.nextval
        return self
    def filter(self, expression):
        terms = expression.split('+')
        for i in range(len(terms)):
            term = terms[i]
            xloc = term.find('x')
            if 1 <= xloc:
                coefficient = term[:xloc]
                exponent = term[xloc + 2:]
            else:
                coefficient = term
                exponent = '0'
            self.insertNode(coefficient, exponent)
        return True

if __name__ == '__main__':
    li = Polynomial()
    print("Welcome to polynomial equations")
    expression1 = input("Enter polynomial as (ax^2+bx^1+c) : ")
    li.filter(expression1)
    li2 = Polynomial()
    expression2 = input("Enter another polynomial as (ax^2+bx^1+c) : ")
    li2.filter(expression2)
    li3 = Polynomial()
    expression3 = input("Enter another polynomial as (ax^2+bx^1+c) : ")
    li3.filter(expression3)
    print("\n")
    sum = li + li2 + li3
    print("Sum"+"\t:"+str(sum.printPoly()))
    mul = li * li2 * li3
    print("Product"+"\t:"+str(mul.printPoly()))

#Limts of Program
#1. when polynomials are given in inordered form the result is effected