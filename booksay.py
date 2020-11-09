class BOOK:
    #属性初始化`
    def __init__(self,name,author,imformation,state=0):
    #书籍的名字，作者，信息，借阅状态
        self.name = name 
        self.author = author 
        self.imformation = imformation 
        self.state = state 

    def __str__(self): #用__str__可以直接print返回值，也可用show_info这种，这时print(book.show_info())
        if self.state == 0:
        #借阅状态分为0和1
            status = '未借出'
        else:
            status = '已借出'
        return '名称：《%s》 作者：%s  详情：%s  状态：%s' % (self.name,self.author,self.imformation,status)


class bookmanager:
    books = []
    #空列表，方便其他方法调用

    def __init__(self):
        book1 = BOOK('2018','刘慈欣','科幻小说',1)
        book2 = BOOK('假如给我三天光明','海伦凯勒','美国短篇')
        book3 = BOOK('从入门到死亡','小甲鱼','编程科普')

        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)


    def menu(self):
        print('欢迎使用图书管理系统！')
        while True:      #budong
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()   # 调用对象方法时self不能忘
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            else:
                print('感谢您的使用，再见！')
                break            
                
    def show_all_book(self):
        for book in self.books:
            print(book)
            print('')

    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author = input('请输入书籍作者：')
        new_info = input('请输入书籍详情：')

        new_book = BOOK(new_name,new_author,new_info) #传入参数，创建BOOK类实例
        self.books.append(new_book) #添加到列表books里
        print('书籍录入成功！')

    def check_book(self,name):
        for book in self.books:
            if book.name == name:
                return book  # 返回该实例对象，遇到return语句方法停止执行

        else: #若for循环中，没有返回满足条件的对象，则执行else子句
            return None 

    def lend_book(self):
        name = input('请输入书籍名称：')
        res = self.check_book(name)

        if res != None:
            if res.state == 1:
                print('书籍并没有被借出，是不是搞错了~')
            else:
                print('借阅成功!爱惜书籍哦~')
        else:
            print('系统内还没有这本书籍，找找别的吧！')

    def return_book(self):
        name = input('请输入归还的书籍名称：')
        res = self.check_book(name)

        if res != None:
            if res.state == 1:
                print('归还成功，谢谢！~')
            else:
                print('书籍并没有被借出，是不是搞错了？')
        else:
            print('系统内并没有这本书籍，是不是搞错了！')

            


manager = bookmanager()
manager.menu()