#insertion sort
'''
This did not work. Learn recurssion properly.

def insertion_sort(A,i,n):
    value=A[i]
    j=i
    while j>0 and A[j-1]>value:
        A[j]=A[j-1]
        j=j-1
    A[j]=value
    if i+1<=n:
        insertion_sort(A,i+1,n)

print(insertion_sort([4,1,5,2,7],0,5))'''

'''def insert(A,n):
    for i in range(1,len(A)):
        temp=A[i]
        j=i
        while j>0 and A[j-1]>temp:
            A[j]=A[j-1]
            j=j-1
        A[j]=temp
    return A
print(insert([3,8,2,4,1],5))'''


# Binary search

'''def bin(A,x,n):
    left=0
    right=n
    while left<right:
        mid=int(left+((right-left)/2))
        if A[mid]==x:
            return mid
            break
        elif A[mid]<x:
            left=mid
        else:
            right=mid

print(bin([1,3,4,5,6,7,8],7,7))
print(bin([1,3,4,8,12],8,5))'''

#bubble sort
'''def bubble(A,n):
    for i in range(1,n):
        j=i
        while j>0:
            if A[j]<A[j-1]:
                temp=A[j]
                A[j]=A[j-1]
                A[j-1]=temp
                j=j-1
            else:
                break
    return A
print(bubble([9,3,4,6,1,2],6))'''

#selection sort
'''def sel(A,n):
    for i in range(1,n):
        minimum=A[i-1]
        min_index=i-1
        j=i
        while j<n:
            if minimum>A[j]:
                minimum=A[j]
                min_index=j
                j+=1
            else:
                j+=1
        temp=A[i-1]
        A[i-1]=minimum
        A[min_index]=temp
        print(A)
    return A
print(sel([90,43,56,87,23,69],6))'''

#merge sort
'''def merge(arr1,arr2):
    result=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    result+=arr1[i:]
    result+=arr2[j:]

    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    m=len(arr)//2
    arr1=merge_sort(arr[:m])
    arr2=merge_sort(arr[m:])

    return merge(arr1,arr2)

arr=[4,14,2,11,7,9,5,3,1,9,15,17,12]
print(merge_sort(arr))'''


#quick sort
'''def partition(arr,l,r):
    ptr=l
    pivot=arr[r]
    for i in range(l,r):
        if arr[i]<=pivot:
            (arr[i],arr[ptr])=(arr[ptr],arr[i])
            ptr+=1
    (arr[ptr],arr[r])=(arr[r],arr[ptr])
    return ptr

def quick_sort(arr,l,h):
    if len(arr)==1:
        return arr
    if l<h:
        pi_loc=partition(arr,l,h)
        quick_sort(arr,0,pi_loc-1)
        quick_sort(arr,pi_loc+1,h)
    return arr

arr=[2,4,3,1,6,5]
#print(partition([2,4,3,1,6,5],0,5))
print(quick_sort(arr,0,5))'''

#union of two arrays
'''def uni(arr1,arr2,n,m):
    arr=[-1]*(n+m)
    i=0
    j=0
    k=0
    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            if arr[k-1]!=arr1[i]:
                arr[k]=arr1[i]
                k+=1
            i+=1
        else:
            if arr[k-1]!=arr2[j]:
                arr[k]=arr2[j]
                k+=1
            j+=1
        
    while i<n:
        if arr[k-1]!=arr1[i]:
            arr[k]=arr1[i]
            k+=1
        i+=1
    while j<m:
        if arr[k-1]!=arr2[j]:
            arr[k]=arr2[j]
            k+=1
        j+=1
    return arr[:k]

arr1=[1,1,2,3,3,5,6,6,6,6,8,9]
arr2=[1,1,1,3,5,15,15,19]
print(uni(arr1,arr2,len(arr1),len(arr2)))'''

#intersection

'''def int(arr1,arr2,n,m):
    arr=[-1]*(n+m)
    i=0
    j=0
    k=0
    while i<n and j<m:
        if arr1[i]==arr2[j]:
            if arr[k-1]!=arr1[i]:
                arr[k]=arr1[i]
                k+=1
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    if k==0:
        return [-1]
    else:
        return arr[:k]

arr1=[1]
arr2=[3,5,15,15]
print(int(arr1,arr2,len(arr1),len(arr2)))'''


#minimum no. of swaps

'''def minswap(arr):
    arr2=sorted(arr)
    #arr3=arr.copy()
    temp=0
    for i in range(len(arr)):
        if arr2[i]!=arr[i]:
            j=arr.index(arr2[i])
            print(j)
            (arr[i],arr[j])=(arr[j],arr[i])
            print(arr)
            temp+=1
    return (temp)

arr=[10,19,6,3,5]
print(minswap(arr))'''

#segss_0,1,2

'''def seg(arr,N):
    d={0:0,1:0,2:0}
    for i in arr:
        if i==0:
            d[0]+=1
        elif i==1:
            d[1]+=1
        else:
            d[2]+=1
    for j in range(d[0]):
        arr[j]=0
    for k in range(d[0],d[1]+d[0]):
        arr[k]=1
    for l in range(d[0]+d[1],d[0]+d[1]+d[2]):
        arr[l]=2
    return arr
arr=[1,1,1,0]
print(seg(arr,len(arr)))'''

#median
'''def med(arr1,arr2,n,n2):
        arr=[-1]*(n+n2)
        i=0
        j=0
        k=0
        while i<n and j<n2:
            if arr1[i]<arr2[j]:
                arr[k]=arr1[i]
                i+=1
            else:
                arr[k]=arr2[j]
                j+=1
            k+=1
        while i<n:
            arr[k]=arr1[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=arr2[j]
            j+=1
            k+=1     
        print(arr)  
        if (n+n2)%2==0:
            result=(arr[(n+n2-2)//2]+arr[(n+n2)//2])/2
            if result%1==0:
                return int(result)
            else:
                return result
        else:
            return arr[(n+n2)//2]

arr1=[27,70,130,152,261,271,282,315,321,397,567,572,705,720,755,757,788,834,835,926,968,1005,1014,1086,1142,1205,1225,1388,1397,1429,1543,1555,1620,1621,1676,1879,1916,1965,2020,2045,2135,2181,2187,2200,2227,2321,2349,2350,2379,2381,2460,2516,2534,2538,2652,2666,2762,2803,2811,3017,3033,3035,3059,3076,3078,3122,3132,3136,3159,3188,3381,3391,3454,3496,3600,3621,3690,3758,3810,3844,3855,3887,3998,4051,4060,4062,4106,4133,4156,4206,4209,4319,4323,4363,4370,4374,4446,4492,4607,4719,4802,4880,4882,4891,4901,4942,4960,4986,5001,5050,5091,5092,5097,5120,5174,5185,5209,5245,5290,5340,5353,5400,5463,5503,5528,5650,5689,5784,5814,5848,5960,6103,6158,6318,6328,6336,6358,6446,6477,6479,6494,6498,6507,6699,6769,6803,6843,6998,7002,7003,7097,7122,7204,7250,7329,7377,7429,7429,7622,7657,7759,7782,7789,7800,7858,7866,7891,7934,7939,8134,8134,8146,8159,8197,8245,8354,8357,8360,8375,8435,8442,8580,8582,8702,8746,8754,8759,8762,8953,8989,8997,9107,9126,9131,9161,9204,9272,9275,9281,9328,9349,9445,9471,9472,9487,9595,9663,9739,9767,9775,9808,9819,9841,9890,9956,10002,10008,10085,10101,10120,10142,10184,10197,10206,10227,10228,10383,10393,10402,10418,10442,10474,10491,10499,10509,10541,10558,10619,10634,10642,10649,10687,10708,10756,10771,10772,10780,10781,10809,10815,10817,10835,10856,11080,11305,11362,11560,11657,11679,11693,11716,11759,11763,11854,11957,11972,11973,11998,12002,12003,12003,12029,12106,12156,12218,12362,12377,12407,12495,12539,12546,12548,12556,12592,12636,12934,12955,12956,13169,13171,13186,13186,13194,13243,13405,13415,13419,13422,13443,13572,13579,13582,13665,13679,13702,13708,13765,13769,13813,13889,13894,13999,14052,14068,14071,14074,14143,14181,14288,14389,14399,14410,14497,14517,14537,14609,14622,14634,14639,14669,14883,14956,15052,15087,15105,15111,15205,15250,15256,15285,15302,15338,15374,15394,15421,15556,15579,15641,15757,15761,15779,15779,15820,15927,15928,15952,15997,16000,16030,16108,16110,16141,16145,16151,16208,16210,16214,16260,16315,16343,16528,16654,16731,16748,16812,16831,16862,16879,16983,16988,17128,17184,17239,17278,17300,17330,17354,17407,17418,17446,17498,17512,17526,17529,17530,17532,17631,17663,17703,17720,17737,17753,17769,17791,17813,17862,17941,17999,18052,18163,18180,18228,18272,18334,18385,18418,18452,18455,18457,18460,18470,18474,18485,18498,18511,18571,18590,18643,18769,18772,18874,18997,19130,19138,19187,19212,19297,19300,19328,19362,19424,19437,19463,19478,19505,19507,19561,19616,19617,19668,19823,19898,19922,19930,19932,19938,20144,20310,20363,20423,20595,20630,20657,20683,20697,20776,20799,21021,21064,21104,21407,21446,21457,21477,21478,21482,21535,21557,21571,21584,21603,21622,21630,21651,21692,21737,21758,21781,21885,21887,21892,21921,21995,22047,22094,22109,22133,22140,22157,22228,22263,22267,22292,22301,22316,22338,22346,22475,22505,22508,22523,22536,22565,22572,22610,22626,22727,22736,22758,22818,22852,22860,22870,22894,22942,22971,23011,23028,23128,23150,23194,23248,23277,23291,23293,23352,23365,23402,23436,23436,23502,23520,23536,23600,23711,23789,23799,23812,23891,24017,24021,24096,24113,24140,24280,24330,24350,24409,24445,24453,24571,24575,24713,24731,24747,24769,24828,24839,24860,24899,24917,25004,25019,25021,25048,25091,25117,25151,25160,25171,25207,25269,25277,25367,25385,25443,25482,25492,25525,25572,25578,25583,25627,25660,25720,25733,25746,25803,25807,25813,25841,25926,25938,26038,26116,26172,26174,26211,26212,26239,26324,26347,26368,26385,26512,26626,26655,26743,26749,26802,26885,26900,26921,26991,26999,27004,27041,27059,27066,27092,27121,27121,27214,27229,27255,27288,27304,27395,27423,27431,27465,27527,27558,27608,27621,27643,27654,27784,27851,27917,28024,28096,28105,28127,28128,28242,28270,28280,28303,28306,28349,28353,28401,28480,28490,28575,28577,28581,28663,28686,28725,28741,28764,28838,28869,28900,28922,28924,28950,28963,28995,28995,29088,29118,29154,29177,29190,29219,29243,29269,29310,29335,29420,29505,29560,29620,29642,29698,29709,29752,29773,29831,29919,29929,30018,30020,30022,30139,30154,30193,30194,30267,30361,30376,30476,30477,30519,30529,30563,30607,30618,30668,30701,30708,30710,30744,30753,30757,30871,30879,30885,30918,31006,31007,31020,31048,31099,31103,31129,31150,31158,31181,31189,31209,31215,31235,31242,31272,31297,31321,31344,31345,31385,31391,31432,31502,31597,31616,31699,31777,31794,31820,31823,31840,31863,31880,31929,31945,31972,31984,32062,32063,32113,32122,32145,32233,32263,32263,32268,32402,32424,32436,32463,32547,32550,32632,32636,32642,32728,32742]
arr2=[4,11,59,64,83,113,125,250,281,284,319,329,333,340,456,479,524,567,577,578,739,1047,1054,1102,1133,1292,1294,1310,1318,1340,1351,1419,1444,1493,1509,1527,1678,1757,1850,1868,2028,2080,2088,2096,2096,2165,2185,2201,2288,2311,2376,2539,2571,2572,2675,2824,3037,3046,3057,3088,3130,3143,3145,3173,3265,3282,3316,3339,3399,3466,3568,3701,3746,3762,3855,3860,4008,4032,4034,4048,4113,4115,4324,4324,4408,4433,4435,4529,4535,4572,4593,4608,4724,4911,4948,4949,4953,4960,5041,5095,5113,5130,5152,5209,5238,5255,5274,5276,5371,5510,5587,5680,5726,5733,5777,5784,5821,5828,5831,5861,5957,5973,5980,5990,5998,6051,6065,6080,6089,6168,6187,6209,6279,6289,6367,6368,6418,6420,6507,6534,6571,6598,6646,6738,6755,6794,6823,6869,6872,6916,6973,7058,7119,7128,7158,7177,7200,7221,7236,7256,7349,7361,7409,7444,7466,7501,7569,7606,7658,7691,7786,7835,7960,7981,8080,8094,8100,8114,8236,8255,8347,8422,8427,8441,8451,8478,8500,8563,8576,8600,8609,8611,8696,8699,8705,8746,8773,8810,8835,8851,8938,8980,9066,9074,9086,9149,9157,9312,9313,9317,9330,9355,9362,9539,9591,9662,9734,9852,9898,9980,10026,10053,10094,10116,10126,10139,10182,10194,10264,10297,10313,10336,10425,10432,10437,10491,10533,10559,10591,10656,10737,10776,10893,10956,10960,11074,11092,11167,11174,11204,11208,11221,11290,11390,11414,11465,11467,11480,11506,11522,11580,11584,11608,11734,11784,11784,11804,11808,11814,11885,11931,11934,11949,11969,12006,12016,12040,12057,12110,12274,12274,12403,12416,12425,12496,12499,12512,12536,12557,12582,12602,12697,12698,12711,12721,12738,12778,12797,12814,12859,12890,12966,13000,13010,13024,13128,13280,13292,13310,13332,13344,13355,13435,13466,13475,13511,13531,13548,13565,13579,13626,13739,13898,13938,13942,13960,14004,14009,14026,14064,14103,14113,14144,14264,14276,14329,14445,14487,14531,14539,14575,14596,14623,14649,14652,14666,14692,14754,14775,14829,14848,14882,14917,14925,15063,15205,15278,15285,15310,15343,15361,15390,15417,15632,15662,15860,15894,15935,15968,15979,16001,16005,16013,16053,16067,16123,16152,16159,16181,16205,16235,16274,16275,16330,16387,16441,16448,16456,16473,16477,16520,16665,16729,16851,16854,16950,16981,17157,17201,17239,17245,17265,17275,17278,17321,17328,17330,17345,17372,17533,17562,17577,17614,17615,17639,17641,17662,17719,17732,17760,17818,17828,17965,17992,18037,18043,18060,18122,18160,18248,18281,18349,18448,18484,18538,18548,18604,18652,18653,18717,18745,18817,18818,18952,18977,19022,19037,19037,19073,19144,19226,19238,19396,19413,19438,19515,19530,19541,19597,19629,19632,19634,19666,19706,19838,19895,19996,20017,20022,20057,20118,20150,20159,20224,20236,20322,20348,20349,20376,20394,20399,20467,20516,20545,20546,20558,20563,20586,20627,20729,20792,20814,20831,20856,20860,20927,21011,21036,21037,21067,21070,21155,21163,21163,21185,21197,21280,21293,21312,21376,21402,21505,21522,21577,21584,21629,21650,21683,21747,21813,21893,21944,21976,22017,22020,22046,22055,22092,22094,22103,22150,22243,22286,22308,22308,22309,22312,22354,22374,22425,22433,22490,22495,22529,22608,22664,22704,22751,22758,22935,22964,22969,23098,23099,23112,23155,23193,23261,23306,23313,23343,23468,23488,23494,23497,23532,23533,23578,23686,23723,23744,23782,23792,23804,23811,23851,23980,24016,24045,24102,24104,24169,24197,24248,24310,24364,24486,24524,24647,24703,24717,24721,24763,24775,24776,24930,24936,24944,25002,25036,25082,25135,25149,25264,25332,25371,25390,25400,25402,25411,25446,25472,25498,25514,25518,25545,25579,25640,25672,25746,25807,25834,25908,25943,26003,26082,26108,26146,26186,26232,26240,26257,26321,26327,26338,26425,26465,26491,26563,26702,26706,26715,26871,26881,26886,26904,26945,26970,26994,27007,27118,27146,27193,27216,27218,27308,27319,27430,27444,27500,27507,27534,27635,27771,27800,27833,27869,28020,28031,28064,28083,28101,28109,28201,28244,28309,28321,28375,28420,28440,28493,28547,28553,28554,28568,28599,28600,28667,28673,28751,28774,28793,28848,28866,28930,28948,28974,28999,29027,29040,29153,29242,29258,29260,29277,29318,29401,29421,29561,29569,29579,29586,29614,29666,29766,29798,29803,29898,29903,30001,30006,30047,30049,30057,30288,30348,30434,30609,30701,30701,30776,30779,30805,30860,30919,30955,30986,30992,31014,31095,31174,31192,31215,31254,31284,31375,31378,31384,31427,31487,31536,31551,31572,31578,31606,31640,31667,31712,31727,31746,31754,31768,31785,31864,31884,31944,31966,32049,32050,32067,32097,32107,32111,32149,32192,32213,32214,32260,32319,32322,32369,32500,32531,32565,32593,32620,32742,32744]
print(med(arr1,arr2,790,788))'''
#platformsssss
'''def find(n,arr,dep):
    p=[0]*2361
    pf=1
    s=0
    xtra=0
    time=[]
    for i in range(n):
        p[arr[i]]+=1
        p[dep[i]]-=1
        print (f'p[{arr[i]}]={p[arr[i]]}')
        print (f'p[{dep[i]}]={p[dep[i]]}')
    for ele in p:
        s+=ele
        pf=max(s,pf)
    return pf

arr=[10,300,450,720,1130,1440,1710,1900,2240]
dep=[600,800,730,750,1200,1900,2100,2300,2310]
print(find(9,arr,dep))
arr=[12,310,825,1000,1230,1550,1900,2100]
dep=[600,350,1500,1900,1500,1910,2230,2230]
print(find(8,arr,dep))
arr=[5,100,500,900,1300]
dep=[1900,1950,1800,1300,2100]
print(find(5,arr,dep))'''

#sum matrix

'''def sum_matrix(A,B):
    res=[]
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        return res
    for i in range(len(A)):
        p=[]
        for j in range(len(A[0])):
            p.append(A[i][j]+B[i][j])
        res.append(p)
    return res


A=[[2,3],[3,4],[1,2]]
B=[[1,2],[2,3],[1,4]]
print(sum_matrix(A,B))'''

        

#reverse array
'''def rev(A):
    result=[]
    for element in A:
        result=[element]+result
    A=result
    return A

print(rev([1,2,3,4,6,9]))'''

'''def rev(A):
    start=0
    end=len(A)-1
    while start<end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
    return A

print(rev([1,1,2,3,3,5,6,6,6,6,8,9]))'''

#minimum and maximum in an array

'''def min_max(A):
    if len(A)==1:
        min=A[0]
        max=A[0]
        return (f'min = {min} and max = {max}')
    elif len(A)==2:
        if A[0]>=A[1]:
            min=A[1]
            max=A[0]
            return (f'min = {min} and max = {max}')
        else:
            min=A[0]
            max=A[1]
            return (f'min = {min} and max = {max}')
    else:
        if A[0]>A[1]:
            min=A[1]
            max=A[0]
        else:
            min=A[0]
            max=A[1]
        for i in range(2,len(A)):
            if A[i]>max:
                max=A[i]
            elif A[i]<min:
                min=A[i]
        return (f'min = {min} and max = {max}')
    
A=[4,1,8,3,5,7,11,12,9,4]
B=[1,1]
C=[5,0]
print(min_max(B))'''

#Find the number repeated most number of times.
'''def most_rep(A):
    dict={}
    for i in A:
        if i not in dict.keys():
            dict[i]=1
        else:
            dict[i]+=1
    print(dict)
    max=0
    result=0
    for keys,values in dict.items():
        if values>max:
            max=values
            result=keys
    return result
A=[1,1,2,2,2]
print(most_rep(A))'''

#matrix multiplication

'''def product_of_matrix():
    n1 = int(input())
    m1 = int(input())
    A = []
    for i in range(n1):
        row_A=[]
        for j in range(m1):
            ele_A = int(input())
            row_A.append(ele_A)
        A.append(row_A)
    n2 = int(input())
    m2 = int(input())
    B = []
    for i in range(n1):
        row_B=[]
        for j in range(m1):
            ele_B = int(input())
            row_B.append(ele_B)
        B.append(row_B)
    
#Function to multiply two matrices.
    def multiplyMatrix(self,A,B):
        # code here 
        Result = []
        if m1!=n2:
            return Result
        else:
            for i in range(n1):
                row_result = []
                for j in range(m2):
                    sum=0
                    for k in range(m1):
                        product = A[i][k]*B[k][j]
                        sum+=product
                    row_result.append(sum)
                Result.append(row_result)
            return Result

print(product_of_matrix())'''

#determinant_of_matrix
'''def determinantOfMatrix(matrix,n):
    import copy
    det=0
    if n==1:
        return (matrix[0][0])
    if n == 2:
        det = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return det
    else:
        for i in range(n):
            dup = copy.deepcopy(matrix)
            dup.pop(0)
            print(dup)
            print(matrix)
            for j in dup:
                j.pop(i) 
                print(dup)
                print(matrix)       
            p = ((-1)**i)*matrix[0][i]*determinantOfMatrix(dup,len(dup))
            det+=p
    return det
                
matrix = [[1,0,2,-1],[3,0,0,5],[2,1,4,-3],[1,0,5,0]]
n=len(matrix)
print(determinantOfMatrix(matrix,n))'''

#rotate a matrix by 90 degree in anticlockwise direction

'''def rotateby90(matrix, n): 
    # code here
    if n == 1:
        return matrix
    elif n == 2:
        matrix[0][0],matrix[1][0],matrix[1][1],matrix[0][1] = matrix[0][1],matrix[0][0],matrix[1][0],matrix[1][1]
        #print(matrix)
        return matrix
    else:
        for i in range(n//2):
            for j in range(i,n-(i+1)):
                matrix[i][j], matrix[n-j-1][i],matrix[n-i-1][n-j-1],matrix[j][n-i-1] = matrix[j][n-i-1],matrix[i][j],matrix[n-j-1][i],matrix[n-i-1][n-j-1]
    return matrix

matrix = [[1,2,3,0],[4,5,6,7],[7,8,9,8],[4,6,9,2]]
n = len(matrix)
print(rotateby90(matrix, n))'''

#traversing a matrix spirally
'''def sprl(matrix,r,c):
    result = []
    hor = 0
    ver = 0
    if len(matrix) == 1:
        return matrix[0]
    else:
        #while len(result) < r*c:
        for i in range((r+1)//2):
            while hor < (c-i):
                if len(result) < r*c:
                    result.append(matrix[ver][hor])
                else:
                    break
                #print(f'hor = {hor},ver = {ver}')
                #print(result)
                hor+=1
            hor-=1
            ver+=1
            while ver < (r-i):
                if len(result) < r*c:
                    result.append(matrix[ver][hor])
                else:
                    break
                #print(f'hor = {hor},ver = {ver}')
                #print(result)
                ver+=1
            ver-=1
            hor-=1
            while hor >= i:
                if len(result) < r*c:
                    result.append(matrix[ver][hor])
                else:
                    break
                #print(f'hor = {hor},ver = {ver}')
                #print(result)
                hor-=1
            hor+=1
            ver-=1
            while ver >= i+1:
                if len(result) < r*c:
                    result.append(matrix[ver][hor])
                else:
                    break
                #print(f'hor = {hor},ver = {ver}')
                #print(result)
                ver-=1
            hor+=1
            ver+=1
    return result
matrix = [[1],[2],[3],[4]]
r = len(matrix)
c = len(matrix[0])
print(sprl(matrix,r,c))'''

#Max area under histogram
'''def maxArea(M, n, m):
    height=[]
    max_area=0
    for i in range(n):
        s = 0
        for j in range(m):
            s+=M[i][j]
        height.append(s)
    ps = [-1]
    ns = []
    for i in range(1,n):
        j=i
        while j>0:
            if height[i]>height[j-1]:
                ps.append(j-1)
                break
            else:
                j-=1
        else:
            ps.append(-1)
    for i in range(n-1):
        j=0
        while j<(n-1):
            if height[i]>height[j+1]:
                ns.append(j+1)
                break
            else:
                j+=1
        else:
            ns.append(n)
    ns.append(n)
    print(ns)
    print(ps)
    print(height)
    for ele in range(n):
        area = (ns[ele] - ps[ele] - 1) * height[ele]
        print(area)
        max_area = max(max_area,area)
    return max_area

M = [[1,0,2,0]]
n=len(M)
m=len(M[0])
print(maxArea(M,n,m))'''


#max area of rectangle in binary matrix
# (:\ not accepted, optimise it )

'''def max_rect(M,m,n):
    height = [M[0]]
    for i in range(1,m):
        temp =[]
        for j in range(n):
            if M[i][j] == 0:
                temp.append(0)
            else:
                temp.append(M[i][j]+height[i-1][j])
        height.append(temp)
    max_area = 0
    h = len(height)
    w = len(height[0])
    for i in range(h):
        ps=[-1]
        ns=[]
        for ele in range(1,n):
            j=ele
            while j>0:
                if height[i][ele]>height[i][j-1]:
                    ps.append(j-1)
                    break
                else:
                    j-=1
            else:
                ps.append(-1)
        for ele in range(1,n):
            j=ele
            while j<n:
                if height[i][ele-1]>height[i][j]:
                    ns.append(j)
                    break
                else:
                    j+=1
            else:
                ns.append(n)
        ns.append(n)
        #print(ps)
        #print(ns)
        for _ in range(w):
            area = (ns[_]-ps[_]-1)*height[i][_]
            max_area = max(area,max_area)
    return max_area

M = [[1,1,1,1,1],[0,1,0,0,0]]
m=len(M)
n=len(M[0])
print(max_rect(M,m,n))'''

# k consecutive elements' sum in array
'''def solver(arr,n,k):
    result=[]
    for i in range(k-1,n):
        s=0
        for j in range(k):
            s += arr[i-j]
        print(s)
        if s<=arr[n-1]:
            if s in arr:
                result.append(s)
                print(result)
            else:
                break
    if len(result) == 0:
        return -1
    else:
        for j in result:
            return j
arr =[2,4,6,7,10,11,13,14,17]
n=9
k=2
print(solver(arr,n,k))'''

#max_area of rectngle in binary matrix

'''def max_hist(arr,m):
    # m is number of columns
    ps=[-1]
    ns=[]
    max_area = 0
    for i in range(1,m):
        print(f'i = {i}')
        temp = i
        while temp>=0:
            if arr[i]>arr[temp-1]:
                ps.append(temp-1)
                print(ps)
                break
            else:
                temp-=1
        else:
            ps.append(temp)
    for j in range(m-1):
        print(f'j={j}')
        temp=j
        while temp<m-1:
            if arr[j]>arr[temp+1]:
                ns.append(temp+1)
                print(ns)
                break
            else:
                temp+=1
                print(f'temp={temp}')
        else:
            ns.append(m)
    ns.append(m)
    print(ns)
    for i in range(m):
        area = (ns[i]-ps[i]-1)*arr[i]
        print(area)
        max_area = max(max_area,area)
    return max_area'''

'''arr = [1,1,1,0,1]
m=len(arr)
print(max_hist(arr,m))'''

'''def max_rect(M,n,m):
    test=[M[0]]
    maximum_area=0
    for i in range(1,n):
        temp=[]
        for j in range(m):
            if M[i][j]!=0:
                temp.append(test[i-1][j] + M[i][j])
            else:
                temp.append(0)
        test.append(temp)
    print(test)
    for _ in test:
        area = max_hist(_,m)
        maximum_area = max(maximum_area,area)
        print(f'maximum_area={maximum_area}')
    return maximum_area


M=[[1,1,1,0,1],[0,1,1,0,0],[1,0,1,0,0]]
n=len(M)
m=len(M[0])
print(max_rect(M,n,m))'''

#binary String

'''str = '10102'
for i in str:
    if i=='0' or i=='1':
        continue
    else:
        print(0)
else:
    print(1)'''

#substring start index
def strstr(s,x):
    n = len(x)
    p = len(s)
    for i in range(p-n+1):
        #print(f'start={i}')
        #print(f'end = {i+n-1}')
        if s[i:i+n] != x:
            continue
        else:
            return i
    else:
        return -1

s = 'GeeksForGeeks'
x = 'ek'
print(strstr(s,x))
        



