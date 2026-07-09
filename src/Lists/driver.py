from utils import list_command
if __name__ == '__main__':
    N = int(input())
    list2=[]
    for _ in range(N):
        command=input().split()
        list_command(list2, command)
