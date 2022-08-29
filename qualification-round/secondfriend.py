from math import ceil
from re import I

# for test case validation
import sys
sys.stdin = open('second_friend_validation_input.txt', 'r')

def tree_happy(scene, row, col):
    neighbors = 0
    for i in range(row - 1, row + 2):
        if i < 0 or i >= len(scene):
            continue
        if scene[i][col] == '^':
            neighbors += 1
            if neighbors == 2:
                return True

    for j in range(col - 1, col + 2):
        if j < 0 or j >= len(scene[0]):
            continue
        if scene[row][j] == '^':
            neighbors += 1
            if neighbors == 2:
                return True
    
    return False


def make_tree_happy(scene, row, col):
    for i in range(row - 1, row + 2):
        if i < 0 or i >= len(scene):
            continue
        if scene[i][col] == '.':
            scene[i][col] = '^'
            make_tree_happy(scene, i, col)
    
    for j in range(col - 1, col + 2):
        if j < 0 or j >= len(scene[0]):
            continue
        if scene[row][j] == '.':
            scene[row][j] = '^'
            make_tree_happy(scene, row, j)


def solve(scene):
    for row in range(len(scene)):
        for col in range(len(scene[0])):
            if scene[row][col] == '^' and not tree_happy(scene, row, col):
                make_tree_happy(scene, row, col)

    for row in range(len(scene)):
        for col in range(len(scene[0])):
            if scene[row][col] == '^' and not tree_happy(scene, row, col):
                return False

    return True


T = int(input())
answers = []
for test_case in range(T):
    R, C = input().split()
    R = int(R)
    C = int(C)

    scene = []
    for row in range(R):
        scene.append(list(input()))

    answers.append(solve(scene))

    

with open("second_friend_answers.txt", "w") as f:
    for test_case in range(T):
        print(f"Case #{test_case + 1}: {'Possible' if answers[test_case] else 'Impossible'}")
        f.write(f"Case #{test_case + 1}: {'Possible' if answers[test_case] else 'Impossible'}\n")

# for test case validation:
sys.stdin.close()



        
