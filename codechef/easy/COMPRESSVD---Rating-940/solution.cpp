for _ in range(int(input())):
    n = int(input())
    frames = list(map(int, input().split()))
    
    min_frames = n
    for i in range(n - 1):
        if frames[i] == frames[i + 1]:
            min_frames -= 1
            
    print(min_frames)
