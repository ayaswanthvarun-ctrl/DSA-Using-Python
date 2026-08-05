def launch(n):
    print(n)
    if n>0:
        n-=1
        return launch(n)
result=launch(20)
