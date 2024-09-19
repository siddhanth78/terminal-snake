import time
import os
import random
import msvcrt
import sys

os.system('cls')

class Node:
    
    def __init__(self, prev, x, y):
        
        self.prev = prev
        self.x = x
        self.y = y

grid = [['.' for i in range(24)] for j in range(12)]
 
head = Node(None, 0, 5)
neck = Node(head, head.x, head.y+1)

nodes = []
nodes.append(neck)

foodflag = 1

acc = [0,1]

foodx = 5
foody = 10

grid[foody][foodx] = '*'

available = []

score = 0

sys.stdout.write('\0337')
sys.stdout.write('\033[?25l')
sys.stdout.flush()

while True:

    if msvcrt.kbhit():
        key = msvcrt.getch()
        
        if key == b'w' and acc != [0, 1]:
            acc = [0, -1]
        elif key == b'a' and acc != [1, 0]:
            acc = [-1, 0]
        elif key == b's' and acc != [0, -1]:
            acc = [0, 1]
        elif key == b'd' and acc != [-1, 0]:
            acc = [1, 0]
        else:
            pass
        
    grid[head.y][head.x] = '.'
        
    grid[nodes[-1].y][nodes[-1].x] = '.'
    
    head.x += acc[0]
    head.y += acc[1]
    
    #head.x, head.y = head.x%24, head.y%12 <- Screen wrap
    
    if head.x >= len(grid[0]) or head.x < 0:
        print(f'Score: {score}')
        break
    if head.y >= len(grid) or head.y < 0:
        print(f'Score: {score}')
        break
    
    if grid[head.y][head.x] == '#':
        print(f'Score: {score}')
        break
        
    if head.x == foodx and head.y == foody:
        foodflag = 0
        score += 1
        newnode = Node(nodes[-1], nodes[-1].x, nodes[-1].y)
        grid[newnode.y][newnode.x] = '#'
        nodes.append(newnode)
        
    for node in nodes[::-1]:
        node.x = node.prev.x
        node.y = node.prev.y
        grid[node.y][node.x] = '#'
        
    if foodflag==0:
        available = []
        for row in range(len(grid)):
            available.extend([(j,row) for j in range(row) if grid[row][j] != '#'])
        food = random.choice(available)
        foodx, foody = food
        grid[foody][foodx] = '*'
        
        foodflag = 1
        
    print('\n'.join(''.join(r for r in rows) for rows in grid))
    
    print(f'\nScore: {score}')
    
    time.sleep(0.3)
    
    sys.stdout.write('\0338\033[0J')
    sys.stdout.flush()
