import random

# 生成五个随机数
numbers = [random.randint(1, 100) for _ in range(5)]

# 计算总和
total = sum(numbers)

# 输出结果
print("生成的随机数为：", numbers)
print("總合為：", total)
