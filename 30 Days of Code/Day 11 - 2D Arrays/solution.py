"""
    author : Ali Emre SAVAS
    Link : https://www.hackerrank.com/challenges/30-2d-arrays/problem
"""
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = -63  # -63 because sum can be between -63 and +63. Thus, -63 can be minimum value of sum
    """
    There are 3 section in hourglass
    1 1 1 -> Upper
      1   -> Belt
    1 1 1 -> Bottom
    So, We can use 3 counter in for loop. 
    """
    for x, y, z in zip(range(0, 4), range(1, 5), range(2, 6)):
        for i in range(4):
            upperSection = arr[x][i:i+3]  # There are 3 item in Upper section
            belt = arr[y][i+1]  # There is 1 item in Belt Section
            bottomSection = arr[z][i:i+3]  # There are 3 item Bottom section
            temp = sum(upperSection) + belt + sum(bottomSection)
            if temp > result:
                result = temp
    print(result)
