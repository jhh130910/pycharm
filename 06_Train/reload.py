

class  ChongZai():
    def __getitem__(self, item):
        return item**2 - 5

tmp = ChongZai()

for i in range(1,11):

    print (abs(tmp[i]))