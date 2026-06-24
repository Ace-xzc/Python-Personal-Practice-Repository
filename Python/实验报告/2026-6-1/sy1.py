#20255120201140 李泓毅
grade = float(input("请输入学生的成绩："))
if grade >= 90:
    print("评语：优秀")
elif 80 <= grade <= 89:
    print("评语：良好")
elif 60 <= grade <= 79:
    print("评语：合格")
else:
    print("评语：不及格")