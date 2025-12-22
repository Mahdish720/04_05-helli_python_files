kalame = input()
list_nahayi = ['']
for harf in kalame:
    list_jadid = []
    for i in list_nahayi:
        list_jadid.append( i + harf )
    list_nahayi.extend(list_jadid)
print(list_nahayi)