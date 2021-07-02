import numpy as np

xdatcar = open('XDATCAR', 'r')
xyz = open('XDATCAR.xyz', 'w')
xyz_fract = open('XDATCAR_fract.xyz', 'w')
lat_rec = open('lattice.vectors', 'w')

while True:
    
    system = xdatcar.readline()   # 1行目読み出し

    if len(system) == 0:
        break                                            # 中断条件：要素無し
    
    scale = float(xdatcar.readline().rstrip('\n'))   # 2行目読み出し
    
    #get lattice:vectors
    a1 = np.array([ float(s)*scale for s in xdatcar.readline().rstrip('\n').split() ])  # 3行目読み出し
    a2 = np.array([ float(s)*scale for s in xdatcar.readline().rstrip('\n').split() ])  # 4行目読み出し
    a3 = np.array([ float(s)*scale for s in xdatcar.readline().rstrip('\n').split() ])  # 5行目読み出し
    
    #Save scaled lattice vectors
    lat_rec.write(str(a1[0])+' '+str(a1[1])+' '+str(a1[2])+'\n') #空白行を挟み文字列を記入
    lat_rec.write(str(a2[0])+' '+str(a2[1])+' '+str(a2[2])+'\n')
    lat_rec.write(str(a3[0])+' '+str(a3[1])+' '+str(a3[2])+'\n'+'\n')
        
    #Read xdatcar　辞書型として
    element_names = xdatcar.readline().rstrip('\n').split()  # 6行目読み出し リスト
    element_dict = {}
    element_numbers = xdatcar.readline().rstrip('\n').split()   # 7行目読み出し　リスト

    #元素リストの辞書化
    i = 0
    N = 0
    for t in range(len(element_names)):                          #繰り返しの数=元素種類の要素数t
        element_dict[element_names[t]] = int(element_numbers[i]) #t番目の元素種 = i番目の原子数を辞書に追記
        N += int(element_numbers[i])                             # N = Σi 原子数 = 原子の総和
        i += 1                                                   # i= i +1 = t
         
    line = xdatcar.readline()                            # 8行目から繰り返し読み出し
    
    

    xyz.write(str(N) + "\n"+str(line))                    # 原子数　＋　コメント
    xyz_fract.write(str(N)+ "\n"+str(line))                # 原子巣　＋　コメント
    for el in element_names:                             # el = 元素種の数だけ繰り返し
        for i in range(element_dict[el]):                # i  = 各元素elの原子数だけ繰り返し
            p = xdatcar.readline().rstrip('\n').split()  # p  = 9行目からの読み出し（リスト）
            coords = np.array([ float(s) for s in p ])   # coord << リストp の配列化
            cartesian_coords = coords[0]*a1+coords[1]*a2+coords[2]*a3
            xyz.write(el+ " " + str(cartesian_coords[0])+ " " + str(cartesian_coords[1]) + " " + str(cartesian_coords[2]) +"\n")
            xyz_fract.write(el+ " " + str(coords[0])+ " " + str(coords[1]) + " " + str(coords[2]) +"\n")
    
    
xdatcar.close()
xyz.close()
xyz_fract.close()
lat_rec.close()
