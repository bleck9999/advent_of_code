[print(sum([int(l[i+1])>int(l[i])for i in range(len(l)-1)]))for l in[open("input",'r').read().splitlines()]]
[print(sum([l1[i+1][0]>l1[i][0]for i in range(len(l1)-1)]))for l1 in[[[sum(l[i:i+3])]for i in range(len(l)-2)]for l in[[int(x)for x in open("input",'r').read().splitlines()]]]]
