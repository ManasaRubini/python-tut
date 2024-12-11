import time
m = '''Don't you want me like i want you baby
don't you need me like i need you now
sleep tomorrow but tonight go crazy
all you gonna do is just 
meet me at the
apatue apatue apatue apatue apatue apatue'''

words = m.split()
for word in words:
    time.sleep(0.3)
    print(word,end=" ",flush=True)