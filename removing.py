import os
def remove_image():
    for i in os.listdir("./results"):
        # print(i)
        os.remove(f"./results/{i}")

    for j in os.listdir("./test"):
        os.remove(f"./test/{j}")

remove_image()