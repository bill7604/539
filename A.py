import os

dir=['for bill']
for i in dir:
    path=f"{os.path.dirname(__file__)}/{i}"
    print(path)
    # print(os.listdir(path))
    for j in os.listdir(path):
        # print(j)
        with open(f"{path}/{j}",mode='r',encoding='utf-8') as f1:
            with open(fr"{path}/new/{j}",mode='w',encoding='utf-8') as f2:
                for line in f1:
                    f1.readline()
                    if float(line.strip())<11:
                        continue
                    f2.write(line)