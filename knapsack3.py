import time

class Item:
    weight=0
    profit=0

    def __init__(self, txt):
        fields = txt.split(",")

        self.weight=int(fields[0])
        self.profit=int(fields[1])

class Pack:
    items=[]    

    def __init__(self, _items):        
        self.items=_items.copy()

    def append(self, _item):
        self.items.append( _item )

    def getProfit(self):        
        p=0
        for _item in self.items:
            p+= allitems[_item].profit       
        return p
    
    def printPack(self):                        
        _str=""
        for _item in self.items:
            _str=_str + str(_item) + " "
        print(_str)

def clearOverweight( cap, items):
    i=0
    while i<len(items):
        _item= allitems[items[i]]
        if _item.weight>cap:            
#            print("Remove overweight item(w,p) %d(%d, %d)" % (items[i], _item.weight, _item.profit))
            items.remove(items[i])
            if len(items)==0: break
        else:
            i+=1
    return


def solve(cap, items, pack, opt_pack):
    printmsg=False
       
    items1=items.copy()
    clearOverweight(cap, items1) 

    if len(items1)==0:
        if printmsg:
            pack.printPack()
        if pack.getProfit()> opt_pack.getProfit():
            opt_pack.items.clear
            opt_pack.items= pack.items.copy()
            print("max profit:", pack.getProfit())
        return 

    #include 1st item
    itemindex1=items1[0]
    item1= allitems[itemindex1]
    cap1=cap- item1.weight

    pack1= Pack(pack.items) #copy and save pack1
    pack1.append(itemindex1)    
    items1.remove(itemindex1)
    
    items2= items1.copy()  
    if printmsg:
        print("Add item(w,p): %d(%d, %d), cap= %d" % (itemindex1, item1.weight, item1.profit,  cap1))
    solve(cap1, items2, pack1, opt_pack)

    #not include 1st item in items
    cap2=cap
    pack2= Pack(pack.items) 
    items2= items1.copy()

    if printmsg:
        print("Exclude item(w,p): %d(%d, %d), cap= %d" % (itemindex1, item1.weight, item1.profit,  cap2))
    solve(cap2, items2, pack2, opt_pack)

    return 



capacity=0
f=open("test4.txt","r")
capacity=int(f.readline())
allitems=[]
w= f.readline().split(",")
p= f.readline().split(",")
answer= int(f.readline())
f.close()

for i in range(0, len(w)):
    _item=Item(w[i]+","+p[i])
    allitems.append(_item)

print("Items")
print("Weight \t Profit")
for _item in allitems:
    print("%d \t %d" %(_item.weight, _item.profit))
print("capacity: %d answer: %d" % (capacity,answer))
print("*************")

pack=Pack([])
opt_pack=Pack([])
solve(capacity,[*range(0, len(allitems))], pack, opt_pack)

p=0
w=0
print("Weight \t Profit")
for i in opt_pack.items:
    _item= allitems[i]
    print("%d \t %d" %(_item.weight, _item.profit))
    p+= _item.profit
    w+= _item.weight
print("----------------")
print(" %d \t %d" % (w, p))
print("CPU time: %10.2f seconds" % (time.process_time()))






    




