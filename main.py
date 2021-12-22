nums1=[0,1,1,2,3]
nums2=[5,8,13,21,34]
def mediana(nums1, nums2):
    sort=sorted(nums1+nums2) #общий список
    if len(sort)==0:
        m=sort
    elif len(sort)%2==1:
        m=sort[len(sort)//2]
    else:
        m=(sort[len(sort)//2-1]+sort[len(sort)//2])/2
    return m
print(mediana(nums1, nums2)) #медиана для обьединения двух списко
