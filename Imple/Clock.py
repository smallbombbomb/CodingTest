# H를 입력받기
h = int(input())

count = 0
for inx in range(h + 1):
    for jnx in range(60):
        for knx in range(60):
            # 매시각안에 3포함 시 카운트 증가
            if '3' in str(inx) + str(jnx) + str(knx):
                count += 1

print(count)