#猜颜色
import numpy as np

char = '红黄蓝绿白紫'
ans = input('输入“随机”或输入谜底：')
if ans == '随机':
    s = ''
    for i in range(4):
        s += char[np.random.randint(low=0, high=6)]
    ans = s
    print('生成了随机谜底')
else:
    print('谜底为：', ans)
for i in range(8):
    guess = input('猜')
    fc = 0
    hc = 0
    hashA = []
    hashB = []
    for j in range(4):
        if guess[j] == ans[j]:
            fc += 1
            hashA.append(j)
            hashB.append(j)
    for j in range(4):
        if j not in hashA:
            for k in range(4):
                if k not in hashB and guess[j] == ans[k]:
                    hc += 1
                    hashA.append(j)
                    hashB.append(k)
                    break
    print(f"第{i + 1}/{8}轮：{guess}，全对{fc}个，半对{hc}个")
    if fc == 4:
        print("完全正确！")
        break

print('谜底为：', ans)
