import cmath
class NumericalMethods:
    @staticmethod
    def DerivativeOneSideDifference(func, x, delta = 0.001):
        """Calculating the derivative using the one-way difference method"""
        return (func(x + delta) - func(x)) / delta

    @staticmethod
    def DerivativeTwoSideDifference(func, x, delta = 0.001):
        """Calculating the derivative using the two-way difference method"""
        return (func(x + delta) - func(x - delta)) / (2 * delta)

    @staticmethod
    def FindSignChangeInterval(func, start = 0, step = 1, max_iter = 1000):
        """Searching for the sign change interval"""
        x0 = start
        f0 = func(x0)
        for i in range(1, max_iter):
            x1 = x0 + step
            f1 = func(x1)
            if f1 * f0 < 0:
                return (x0, x1) #Interval change sign
            x0, f0 = x1, f1
        raise ValueError("The sign-changing interval within max_iter was not found.")

    @staticmethod
    def NewtonMethod(func, x = None, delta = 0.01, max_iter = 1000, safe_start = True):
        """algorithm for approximating the roots of real-valued functions"""
        if x is None:
            try:
                x0 = NumericalMethods.FindSignChangeInterval(func)[1]
            except ValueError:
                if safe_start:
                    x0 = 0
                else:
                    raise

        elif isinstance(x, (tuple, list)):
            x0 = x[1]
        else:
            x0 = x

        for _ in range(max_iter):
            fx = func(x0)
            dfx = NumericalMethods.DerivativeTwoSideDifference(func, x0)
            if abs(dfx) < 1e-12:
                raise ZeroDivisionError("The derivative is too small")
            x1 = x0 - fx / dfx
            if abs(x1 - x0) <= delta:
                return x1
            x0 = x1
        raise ValueError("I can't find a solution")

    @staticmethod
    def MethodHalfDivision(func, x = None, delta = 0.01, max_iter = 1000):
        """the method of half division (bisection)"""
        if x is None:
            interval = NumericalMethods.FindSignChangeInterval(func)
        else:
            interval = x
        for _ in range(max_iter):
            x0 = (interval[0] + interval[1]) / 2

            fa = func(interval[0])
            fx = func(x0)
            if fa * fx < 0:
                interval = [interval[0], x0]
            else:
                fb = func(interval[1])
                if fx * fb < 0:
                    interval = [x0, interval[1]]
                else:
                    raise ValueError(f"The function does not change the sign on the interval from {interval[0]} to {interval[1]}")

            if abs(interval[1] - interval[0]) < delta:
                return (interval[0] + interval[1]) / 2

        raise ValueError("I can't find a solution")
