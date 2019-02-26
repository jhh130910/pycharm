# python 科学计算器 ，运算符
def add_subtract_multiply_divide(p1,p2,p3,p4,p5):
    return (p1*p2 + p3 - p4/p5)

add_subtract_multiply_divide_TEMP = add_subtract_multiply_divide(12,34,78,132,6)
#print (add_subtract_multiply_divide_TEMP)


# 判断年份是否为闰年

def judge_year( year):
    if year % 400 == 0 :
        print ('This year is run ...')
    else :
        if year % 4 == 0:
            if year % 100 != 0:
                print ('This year is run ...')
            else:
                print ('This year is ping ...')
        else :
            print ('Thist year is ping ...')

#judge_year(100)
#judge_year(200)
#judge_year(400)
#judge_year(500)
