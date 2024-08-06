import os

def test_fib(fib):
    # Test that fib(0) == 1
    green = "\033[92m"
    red = "\033[91m"
    if fib(0) != 1:
        print(f"{red}fib(0) should be 1")
        return
    else:
        print(f"{green}Test 1 [fib(0)] : passed") 
    
    # Test that fib(1) == 1
    if fib(1) != 1:
        print(f"{red}fib(1) should be 1")
        return
    else:
        print(f"{green}Test 2 [fib(1)] : passed")
    
    # Test that fib(5) == 8
    if fib(5) != 8:
        print(f"{red}fib(5) should be 8")
        return
    else:
        print(f"{green}Test 3 [fib(5)] : passed")
    
    # Test that fib(10) == 89
    if fib(10) != 89:
        print(f"{red}fib(10) should be 89")
        return
    else:
        print(f"{green}Test 4 [fib(10)] : passed")


def test_File(mean,std):
    # test mean = 5.0
    green = "\033[92m"
    red = "\033[91m"
    if mean != 5.0:
        print(f"{red}mean should be 5.0")
        return
    else:
        print(f"{green}Test 1 [mean] : passed")
    
    # test std = 2
    if std != 2:
        print(f"{red}std should be 2")
        return
    else:
        print(f"{green}Test 2 [std] : passed")
    
    # test that the file exists
    if not os.path.exists("results.txt"):
        print(f"{red}results.txt should exist")
        return
    else:
        with open("results.txt","r") as f:
            lines = f.readline()
            lines = float(lines.split(':')[1])
            lines2 = f.readline()
            lines2 = float(lines2.split(':')[1])
        if lines != 5:
            print(f"{red}The mean in results.txt should be 5")
            return
        else:
            print(f"{green}Test 3 [mean in results.txt] : passed")
        if lines2 != 2:
            print(f"{red}The std in results.txt should be 2")
            return
        else:
            print(f"{green}Test 4 [std in results.txt] : passed")