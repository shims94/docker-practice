import random

# 조원이름을 입력받기
names = input("조원 이름을 입력하세요(공백으로 구분합니다) ex)김씨 이씨 최씨 :").split()

selected_name = random.choice(names)
print(f"발표자는 {selected_name} 입니다")
