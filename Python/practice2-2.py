scores = []
scores.append(int(input('国語の点数 >>')))
scores.append(int(input('算数の点数 >>')))
scores.append(int(input('理科の点数 >>')))
scores.append(int(input('社会の点数 >>')))
scores.append(int(input('英語の点数 >>')))
print(f'合計{sum(scores)}点 平均{sum(scores) / len(scores)}点')
