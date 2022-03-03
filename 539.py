while True:
    init = int(input("init = "))
    num = input("nday = ")
    m = input("bou = ")
    rate ={
        "10":[20000,3.55],
        "9":[20000,2.89],
        "8":[25000,2.71],
        "7":[25000,2.21],
        "6":[30000,1.71],
        "5":[30000,1]
    }
    score = 1
    sum=0
    for i in range(1,int(num)+1):
        if i==1:
            score = init
            if score < rate[m][0]:
                sum+=(int(rate[m][1]*score)+score)
                print(f"day={i}, score={init}, d={int(rate[m][1]*score)}, m={int(rate[m][1]*score)*26}, sum={sum}")
                score*=2
        else:
            if score < rate[m][0]:
                sum+=(int(rate[m][1]*score)+score)
                print(f"day={i}, score={score}, d={int(rate[m][1]*score)}, m={int(rate[m][1]*score)*26}, sum={sum}")
                score*=2
            elif score >= rate[m][0]:
                sum+=(int(rate[m][1]*score)+score)
                print(f"day={i}, score={rate[m][0]}, d={int(rate[m][0]*rate[m][1])}, m={int(rate[m][1]*score)*26}, sum={sum}")
    print("\n")