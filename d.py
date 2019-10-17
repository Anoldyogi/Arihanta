class Test:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("desctructor")


t1=Test()
t2=t1
t3=t1
del t1,t2,t3
print("not destroyed")
