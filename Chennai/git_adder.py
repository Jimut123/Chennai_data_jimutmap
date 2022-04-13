import os

for i in range(10):
    command = "git add Chennai_00"+str(i)
    os.system(command)
    command = "Chennai_00"+str(i)
    os.system("git commit -m {}".format(command))
    os.system("git push")


for i in range(10,40):
    command = "git add Chennai_0"+str(i)
    os.system(command)
    command = "Chennai_0"+str(i)
    os.system("git commit -m {}".format(command))
    os.system("git push")

