import matplotlib.pyplot as plt

def fibonacci1(n):
    if n in [0, 1]:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
    
def draw_fibonacci_tree(n):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_axis_off()

    def plot_subtree(n, x0, x1, y):
        if n <= 1:
            ax.annotate(str(fibonacci1(n)), xy=((x0 + x1) / 2, y), ha='center', va='center')
            return
        x_left = (2 * x0 + x1) / 3
        x_right = (x0 + 2 * x1) / 3
        y_next = y - 1
        ax.annotate(str(fibonacci1(n)), xy=((x0 + x1) / 2, y), ha='center', va='center')
        ax.plot([x0, x1], [y, y], '-k')
        ax.plot([x_left, x_left], [y, y_next], '-k')
        ax.plot([x_right, x_right], [y, y_next], '-k')
        plot_subtree(n-1, x0, x_left, y_next)
        plot_subtree(n-2, x_right, x1, y_next)

    plot_subtree(n, 0, 10, 0)
    plt.show()

def fibonacci2(n, memo={0: 1, 1: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci2(n-1, memo) + fibonacci2(n-2, memo)
        return memo[n]

def fibonacci3(n, a=1, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci3(n-1, b, a+b)

if __name__ == "__main__":
    n=10
    print(fibonacci1(n))
    print(fibonacci2(n))
    print(fibonacci3(n))
    draw_fibonacci_tree(6)