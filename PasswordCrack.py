import time as t
# Target's Phone Password It's Internal Process
x = int(input("Enter The User's Password:"))
print("Firewall Cracking Initialize.......")
i = 0
'''Started Trying All Possible Combinations Of Numbers'''
while True:
    i += 1
    if i == x:
        for j in range(10, 110, 10):
            t.sleep(2)
            print("Started Cracking Firewall", j, "%.........")
        t.sleep(0.2)
        print("Firewall Cracked!..\nThe Match Found is", i)
        break
