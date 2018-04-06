# Problem: The gradient descent algorithm is applied to find a local minimum of the function f(x)=x4−3x3+2,
# with derivative (dao ham) f(x)=4x3−9x2.

# From calculation, it is expected that the local minimum occurs at x=9/4

# The value does not matter as long as abs(x_new - x_old) > precision
x_old = 0
x_new = 6  # The algorithm starts at x=6
gamma = 0.01  # step size
precision = 0.00001


def df(x):
    y = 4 * x**3 - 9 * x**2
    return y


while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new += -gamma * df(x_old)

print("The local minimum occurs at %f" % x_new)
