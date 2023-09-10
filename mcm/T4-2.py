from model import T1_model
import math

θ = math.radians(120)
α = math.radians(1.5)
H = 110
distance = [-2, 0, 2]
Conversion = 1852
for i in range(len(distance)):
    distance[i] = distance[i] * Conversion
ans = T1_model(θ, α, H, distance)
deep = ans.deep_calculate()
print("海水深度：")
print(deep)


def get_width(deep):
    return 2 * math.sqrt(3) * deep


def get_width_(deep):
    return math.sqrt(3) * deep


width = []
for item in deep:
    width.append(get_width_(item))
print("扫描宽度：")
print(width)
start = []
end = []
start.append(width[2])
end.append(width[0])
flag = 0
while (start[flag] < 2 * 1852):
    start.append(start[0] * 2 + start[flag])
    flag = flag + 1
for i in range(len(start) - 1):
    end.append(end[0] * 2 + end[i])
print("三角形起点坐标：")
print(start)
print("三角形的终点坐标")
print(end)
line = []
bias = width[0] - width[2]
# rate = bias / (4 * 1852)
tmp = math.sqrt((bias) ** 2 + (4 * 1852) ** 2)
print(tmp)
t2_ans = 0

for i in range(len(start) - 1):
    if end[i] <= (2 * 1852):
        tmp = math.sqrt((end[i] - start[i]) ** 2 + (4 * 1852) ** 2)
        line.append(tmp)
        t2_ans += tmp
    else:
        rate = 1 - (end[i] - 2 * 1852) / (end[i] - start[i])
        tmp = math.sqrt((end[i] - start[i]) ** 2 + (4 * 1852) ** 2) * rate
        line.append(tmp)
        t2_ans += tmp
print(line)
print(t2_ans)
print(t2_ans / 1852)
obj = zip(start, end)
for st, ed in obj:
    print(f"开始：{st},结束：{ed}")
print(len(start))