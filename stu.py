f=open('students.csv')
z1,z2,z3,z4,z5=f.readline().split(',')
idioti=[]
suma=0
spisok=[]
for i in range(500):
    sr=f.readline().split(',')
    if sr[4]!='None\n':
        idioti.append([int(sr[0]), sr[1].split()[0], sr[1].split()[1], sr[1].split()[2], int(sr[2]), sr[3], int(sr[4])])
    else:
        idioti.append([int(sr[0]), sr[1].split()[0], sr[1].split()[1], sr[1].split()[2], int(sr[2]), sr[3], 0])
    if sr[1].split()[0]=='Хадаров' and sr[1].split()[1]=='Владимир':
        print('Ты получил: ', int(sr[4]),', за проект - ', int(sr[2]), sep="")
    suma+=idioti[-1][-1]
suma=float(suma)
sr=format(suma/500, '.3f')
print(sr)
for i in range(len(idioti)):
    if idioti[i][-1]==0:
        idioti[i][-1]=sr
spisok=idioti
spisok(sort(key=lambda x: x=[
f.close()
f=open('students_new.csv', 'w')
f.write(z1+";")
f.write(z2+";")
f.write(z3+";")
f.write(z4+";")
f.write(z5)
for i in range(len(idioti)):
    f.write(str(idioti[i][0])+';')
    f.write(str(idioti[i][1])+' '+str(idioti[i][2])+' '+str(idioti[i][3])+';')
    f.write(str(idioti[i][4])+';')
    f.write(str(idioti[i][5])+';')
    f.write(str(idioti[i][6])+';')
    f.write('\n')
f.close()

