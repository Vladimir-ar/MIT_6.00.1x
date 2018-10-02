import sys
final_data = [[[3, 21], 3], [[1, 14], 1], [[2, 23], 1], [[0, 22], 2], [[6, 22], 1], [[4, 22], 1], [[3, 20], 3], [[3, 19], 1]]


final_data.sort()

tmp_data = [[[0, 22], 2], [[1, 14], 1], [[2, 23], 1], [[3, 19], 1], [[3, 20], 3], [[3, 21], 3], [[4, 22], 1], [[6, 22], 1]]
#tmp_data = [[[2, 4], 1], [[2, 23], 4], [[3, 6], 1], [[3, 16], 1], [[3, 20], 1], [[4, 15], 1], [[4, 19], 1], [[4, 20], 4], [[4, 21], 2], [[5, 3], 3], [[5, 4], 2], [[5, 8], 1], [[5, 10], 2], [[5, 21], 2], [[5, 23], 3], [[6, 23], 1]]
#tmp_data = [[[2, 4], 1], [[2, 23], 4], [[3, 6], 1], [[3, 16], 1], [[3, 20], 1], [[4, 15], 1], [[4, 19], 1], [[4, 20], 4], [[4, 21], 2], [[5, 3], 3], [[5, 4], 2], [[5, 8], 1], [[5, 10], 2], [[5, 21], 2], [[5, 23], 3], [[6, 23], 1]]
#tmp_data = [[[0, 15], 1], [[0, 17], 1], [[1, 15], 3], [[2, 18], 3], [[3, 16], 6], [[3, 17], 3], [[3, 18], 2], [[3, 19], 1], [[4, 14], 1], [[4, 15], 2], [[5, 16], 3], [[6, 19], 4]]
tmp_data = [[[3, 20], 1], [[5, 12], 1]]
tmp_data = [[[1, 11], 2], [[2, 4], 1], [[2, 5], 1], [[2, 8], 2], [[2, 11], 1], [[3, 9], 1], [[3, 10], 1], [[3, 22], 1], [[3, 23], 1], [[4, 0], 2], [[4, 2], 1], [[4, 4], 1], [[4, 23], 2], [[5, 0], 1], [[5, 1], 4], [[5, 2], 1], [[5, 7], 2], [[6, 2], 1], [[6, 3], 1], [[6, 4], 3]]
#tmp_data = [[[1, 11], 2], [[2, 4], 1], [[2, 5], 1], [[2, 8], 2], [[2, 11], 1], [[3, 9], 1], [[3, 10], 1], [[3, 22], 1], [[3, 23], 1], [[4, 2], 1], [[4, 4], 1], [[4, 23], 2], [[5, 1], 4], [[5, 2], 1], [[5, 7], 2], [[6, 2], 1], [[6, 3], 1], [[6, 4], 3]]

new_lst = []
for i, s in enumerate(tmp_data):
    new_lst.insert(i, [s[0][0], [s[0][1], s[1]]])
#print (new_lst)

new_lst2 = [[0],[1],[2],[3],[4],[5],[6]]



for i, s in enumerate(new_lst):
     #print (i,s)
     new_lst2[new_lst[i][0]].append(s[1])

print(new_lst2)
print ("       00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23")
print ("       =======================================================================")

#print (new_lst2[0][1])

# for i, s in enumerate(new_lst2):
#     if len(s) > 1:
#         print('label'+'{:>20d}'.format(s[1][1]))
#         print("       -----------------------------------------------------------------------")

adict_days = {0: 'Mon', 1:'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
adict_posn = {0: 9, 1: 12, 2: 15, 3: 18, 4: 21, 5: 24,6: 27, 7: 30, 8: 33, 9: 36, 10: 39, 11: 42, 12: 45 ,13: 48, 14: 51, 15: 54,
              16: 57, 17: 60 ,18: 63, 19: 66, 20: 69, 21: 72, 22: 75, 23: 78}

for i, s in enumerate(new_lst2):
    current_day = adict_days.get(new_lst2[i][0])
    new_lst2[i][0] = current_day

for i, s in enumerate(new_lst2):
    if len(s) == 1:
        print (new_lst2[i][0])
        print ("       ******************************No Commits*******************************")
        print('       -----------------------------------------------------------------------')
    if len(s) > 1:
        print(new_lst2[i][0])
        posns = []
        commits = []
        c_0 = 1
        posn_0 = adict_posn.get(s[1][0])
        posn = adict_posn.get(s[c_0][0])
        for val in range(len(s)-1):
            #posn = adict_posn.get(s[c_0][0])
           # posns.append(val[])
            #commit = s[c_0][1]
            print(('{:>%s}' %posn).format(s[c_0][1]),end=" ")
            c_0 += 1
            try:
                posn = (adict_posn.get(s[c_0][0])-adict_posn.get(s[c_0-1][0]))-1
            except IndexError:
                break

        print ('',end='\n')
        print('       -----------------------------------------------------------------------')



# for i in final_data:
#     if final_data[0][0][0] == 0:
#         print
adict = {'Mon': '', 'Tue': None, 'Wed': None, 'Thu': None, 'Fri': None, 'Sat': None, 'Sun': None}
adict2 = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
adict3 ={}



for i, s in enumerate(tmp_data):
    adict3[tmp_data[i][0][0]] = [s[0][1], s[1]]

# for i in adict3:
#     if i in adict_days:
#         adict3[adict_days[i]] = adict3.pop(i)

# for i, s in enumerate(new_lst2):
#     current_day = adict_days.get(new_lst2[i][0])
#     new_lst2[i][0] = current_day
#
# print(new_lst2)

tmpdict= {x: y for x, y in zip(range(1,25), range(9,81,3))}
print (tmpdict)
input("Press enter to exit ;)")

