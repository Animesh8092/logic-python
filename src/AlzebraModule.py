import math, cmath

class AlzebraicEquation:
    def QuadraticEquation(a, b, c, **args):
        if (a==0):
            return "Invalid equation, as a ≠ 0"
        else:
            eqn = "{}x\u00b2+{}x+{}".format(a,b,c)
            D = (b**2)-(4*a*c)
            alpha = -b/a
            beta = c/a
            roots = "\u03B1 = {0} and \u03B2 = {1}".format(alpha,beta)

            if (D<0):
                c_sol1 = -b+(cmath.sqrt(D))/2*a
                c_sol2 = -b-(cmath.sqrt(D))/2*a
                soln = "x = {0} and x = {1}".format(c_sol1,c_sol2)
            elif (D>=0):
                q_sol1 = -b+(math.sqrt(D))/2*a
                q_sol2 = -b-(math.sqrt(D))/2*a
                soln = "x = {0} and x = {1}".format(q_sol1,q_sol2)

            return "f(x) = {0}\nSoln: {1}\nRoots: {2}".format(eqn,soln,roots)