"""
TODO
"""

from fractions import Fraction

class Beta():
    def __init__(self, alpha, beta):
        self.alpha = Fraction(alpha)
        self.beta = Fraction(beta)

    # TODO: setattribute?

    def __repr__(self):
        return "Beta({}, {})".format(self.alpha, self.beta)

    
    def mean(self):
        return self.alpha / (self.alpha + self.beta)

    def var(self):
        return (self.alpha * self.beta
                / ((self.alpha + self.beta)**2 
                    * (self.alpha + self.beta + 1)))




