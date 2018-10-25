import requests
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser');

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello world'
    print stra.replace('world', 'nowcoder')
    print stra.capitalize()
    strb = '   \n\rhello world \r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    print 3, strb.strip()
    strc = 'hello w'
    print 4, strc.startswith('hel')
    print 5, strc.endswith('x')
    print 6, stra + strb + strc
    print 7, len(strc)
    print 8, '-'.join(['a', 'b', 'c'])
    print 9, strc.split(' ')
    print 10, strc.find('ello')


def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 2, True, not True, False
    print 3, 1 < 2, 5 > 2
    print 4, 2 << 3
    print 5, 5 | 3, 5 & 3, 5 ^ 3
    x = 3;
    y = 2.3
    print x / y, type(x), type(y)


def demo_buildinfunction():
    print 1, max(2, 1), min(5, 3)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-3)
    print 4, range(1, 10, 3)
    print 5, dir(list)
    x = 2
    print 6, eval('x+3')
    print 7, chr(65), ord('a')
    print 8, divmod(11, 3)
    print 9, 10 % 4


def demo_controflow():
    score = 68
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10
    score = 75
    for i in range(0, 10):
        pass
        # print 3, i

    for i in range(0, 10, 2):
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break


def demo_list():
    lista = [1, 2, 3]
    print 1, lista
    listb = [1, 'sdf', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb
    print lista
    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)
    print 8, listb
    listb.reverse()
    print 9, listb

    print 10, listb[0], listb[1]
    listb.sort(reverse=True)
    print listb
    print 14, listb * 2
    print 15, [0] * 14

    tuplaa = (1, 2, 3)
    # listaa

def add(a,b):
    return a+b
def sub(a,b):
    return a-b


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1)
    for key, value in dicta.items():
        print key, value
    dictb={'+':add,'-':sub}
    print 5,dictb['+'](1,2)
    print 6,dictb['-'](15,3)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(4)

def demo_set():
    seta = set([1,2,3,1,2])
    setb = set((2,3,4))
    print 1,seta
    print 2,setb
    print 3,seta.intersection(setb),seta&setb
    print 4,seta|setb ,seta.union(setb)
    print 5,seta-setb
    seta.add('x')
    print seta
    print len(seta)

if __name__ == '__main__':
    # sfdha
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controflow()
    # demo_list()
    # demo_dict()
    # demo_set()
    lista =[1,23,3]
    lista.append(5)
    print lista