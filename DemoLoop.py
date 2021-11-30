#구구단 출력
for x in [2,3,4,5,6]:
    print("---{0}단 출력".format(x))
    #inner에 해당되는 for in루프
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} x {1} = {2}".format(x, y, x*y))


