class chinese:
    def __init__(self,region,home):
        self.region = region
        self.home = home
        print('这是第一次分类')
    
    def born(self):
        print('我出生在%s'%(self.region))

    def live(self):
        print('我生活在%s'%(self.home))

    def citys(self):
        self.born()
        self.live()

wo = chinese('湖南','东莞')
wo.citys()

    