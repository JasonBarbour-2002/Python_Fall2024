import os
def test_fact(fact):
    # Test that fact(0) == 1
    green = "\033[92m"
    red = "\033[91m"
    if fact(0) != 1:
        print(f"{red}fact(0) should be 1")
        return
    else:
        print(f"{green}Test 1 [fact(0)] : passed") 
    
    # Test that fact(1) == 1
    if fact(1) != 1:
        print(f"{red}fact(1) should be 1")
        return
    else:
        print(f"{green}Test 2 [fact(1)] : passed")
    
    # Test that fact(5) == 120
    if fact(5) != 120:
        print(f"{red}fact(5) should be 120")
        return
    else:
        print(f"{green}Test 3 [fact(5)] : passed")
    
    # Test that fact(10) == 3628800
    if fact(10) != 3628800:
        print(f"{red}fact(10) should be 3628800")
        return
    else:
        print(f"{green}Test 4 [fact(10)] : passed")

def test_mylists(l1,l2,l3,l4,l5):
    # test l1 = [1,2,3,4,5,6,7,8,9,10]
    expected = [1,2,3,4,5,6,7,8,9,10]
    green = "\033[92m"
    red = "\033[91m"
    if l1 != expected:
        print(f"{red}my_list should be {expected}")
        return
    else:
        print(f"{green}Test 1 [my_list] : passed")
    
    # test l2 = [1,3,5,7,9,11,13,15,17,19]
    expected = [1,3,5,7,9,11,13,15,17,19]
    
    if l2 != expected:
        print(f"{red}my_list2 should be {expected}")
        return
    else:
        print(f"{green}Test 2 [my_list2] : passed")
    
    # test l3 = [2,4,6,8,10]
    expected = [2,4,6,8,10]
    
    if l3 != expected:
        print(f"{red}my_list3 should be {expected}")
        return
    else:
        print(f"{green}Test 3 [my_list3] : passed")
    
    # test l4 = l2[::-1]
    expected = l2[::-1]
    
    if l4 != expected:
        print(f"{red}my_list4 should be {expected}")
        return
    else:
        print(f"{green}Test 4 [my_list4] : passed")
    
    # test l5 = l2[:3]
    expected = l2[:3]
    
    if l5 != expected:
        print(f"{red}my_list5 should be {expected}")
        return
    else:
        print(f"{green}Test 5 [my_list5] : passed")
