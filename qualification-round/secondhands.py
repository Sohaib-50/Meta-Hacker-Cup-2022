from math import ceil
from re import I

# for test case validation
import sys
sys.stdin = open('./second_hands_input.txt', 'r')

T = int(input())
answers = []
for test_case in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)
    
    clocks = input().split()
    if ceil(len(clocks) // 2) > K:
        answers.append(False)
        continue

    display_case_0 = set()
    display_case_1 = set()

    can_store = True
    for clock in clocks:
        if clock not in display_case_0 and len(display_case_0) < K:
            display_case_0.add(clock)
        elif clock not in display_case_1 and len(display_case_1) < K:
            display_case_1.add(clock)
        else:
            can_store = False
            break
    
    answers.append(can_store)

with open("second_hand_answers.txt", "w") as f:
    for test_case in range(T):
        print(f"Case #{test_case + 1}: {'YES' if answers[test_case] else 'NO'}")
        f.write(f"Case #{test_case + 1}: {'YES' if answers[test_case] else 'NO'}\n")

# for test case validation:
sys.stdin.close()



        
