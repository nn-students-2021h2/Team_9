import time
from fibonacci import fibonacci_of

def main():
    t_start = time.time()
    ###
    n = fibonacci_of(30)
    ###
    t_end = time.time()

    t_diff = t_end - t_start
    
    print(n, " time= ", t_diff)

if __name__ == "__main__":
    main()
