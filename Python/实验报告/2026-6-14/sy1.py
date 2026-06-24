#20255120201100廖懋雄
def hobby(*args):
    print("我的爱好有：")
    for item in args:
        print(item)
hobby('学习SQL')
print("-" * 20)
hobby('学习JAVA', '学习CCS', '学习web')
