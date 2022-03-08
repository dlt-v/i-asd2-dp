# import math


# def entropy2(string):
#     dictionary = {}
#     a = len(string)
#     for i in string:
#         if dictionary.get(i):
#             dictionary[i] = dictionary[i]+1
#         else:
#             dictionary[i] = 1
#     return abs(sum([i/a * math.log2(i/a) for i in dictionary.values()]))


# print('shannon:', entropy2('Shannon'))
# print('morrowind:', entropy2('mam na swoim kanale stream z morrowinda niepubliczny'))
# print('lorem:', entropy2('lorem ipsum'))

tekst = 'lorem ipsum'


class Drzewobinarne(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def dzieci(self):
        return (self.left, self.right)

    def galezie(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def drzewo_huffmana(galaz, left=True, binarka=''):
    if type(galaz) is str:
        return {galaz: binarka}
    (lewa, prawa) = galaz.dzieci()
    slownik = dict()
    slownik.update(drzewo_huffmana(lewa, True, binarka + '0'))
    slownik.update(drzewo_huffmana(prawa, False, binarka + '1'))
    return slownik


czest = {}
for i in tekst:
    if i in czest:
        czest[i] += 1
    else:
        czest[i] = 1
czest = sorted(czest.items(), key=lambda x: x[1], reverse=True)
galezie = czest
while len(galezie) > 1:
    (klucz1, i1) = galezie[-1]
    (klucz2, i2) = galezie[-2]
    galezie = galezie[:-2]
    galez = Drzewobinarne(klucz1, klucz2)
    galezie.append((galez, i1 + i2))
    galezie = sorted(galezie, key=lambda x: x[1], reverse=True)
kodhuffmana = drzewo_huffmana(galezie[0][0])
print(' Znak | Wersja bin ')
print('----------------------')
for (znak, czestotliwosc) in czest:
    print(' %-4r |%12s' % (znak, kodhuffmana[znak]))
