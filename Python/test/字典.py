slang_dict = {'你好': '跟别人问好。', '是' :' 表示肯定','棒棒的' : '表示赞扬'}
slang_dict['厉害'] = '指对别人的肯定'
slang_dict['鄙视'] = '指看不起别人'
query = input('请输入想要查询的字词')
if query in slang_dict:
    print (' 您查询的 '+ query + '的含义如下')
    print (slang_dict[query])
else:
    print('对不起该词典中搜索不到该词')
    print ('我们收录的词共有' + str(len(slang_dict))+'个')