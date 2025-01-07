thislist=["Allen","Albert","Thevara"]
thatlist=["1","2"]
thislist[1:2]="N"
thislist.append("MITS")
thislist.extend(thatlist)
print(thislist)
print("Length is :",len(thislist))
