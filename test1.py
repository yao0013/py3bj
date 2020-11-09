file1 = open('H:/py3/scores.txt','r',encoding='utf-8')
file_lines = file1.readlines()      
file1.close()

final_scores = []
for i in file_lines:    #用for...in...把每一行的数据遍历
    data = i.split()
    sum = 0
    for score in data[1:]:
        sum += int(score)      
    result = data[0] + str(sum)
    print(result)

    final_scores.append(result+'\n')

print(final_scores)

winner = open('H:/py3/winner.txt','w',encoding='utf-8') 
winner.writelines(final_scores)
winner.close()