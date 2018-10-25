import random
import re


def demo_random():
    # 1-100
    random.seed(1)
    print 1,int(random.random()*100);
    print 2,random.randint(0,200)

    # choice one in the container
    print 3,random.choice(range(0,100,10))

    # choice multi in the container
    print 4,random.sample(range(0,100),4)

    # shuffle
    a=[1,2,3,4,5]
    random.shuffle(a)
    print 5,a

def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    print p1.findall(str)
    p2 = re.compile('[\d]')
    print p2.findall(str)
    str = 'a@163.com;b@gmai.com;c@qq.com;e@163.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 3, p3.findall(str)

    str = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print p4.findall(str)

if __name__ == '__main__':
    demo_re()