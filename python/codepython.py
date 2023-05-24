# hien thi hello world
print('hello world')

# ngat dong
print('đoạn văn trong văn bản gồm nhiều câu và do đó\
      ta cần ngắt thành nhiều dòng để dễ đọc hơn \
      Câu thứ 1: ceveiefjfi2 ')

# ký tự đặc biệt
print('xuống dòng\n và bắt đầu dòng mới')
print('cách 1 tab\t rồi viết tiếp')

# biến
language = 'python'
print('bạn đang học ngôn ngữ ' + language)

#Kiểu dữ liệu 
year = '2023' 
print('Năm nay là '+ str(year))

# toán tử
# số học
a = 3
b = 12
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # lấy số dư
print(a**b)  # lũy thừa 
# so sánh
print(a<b)
print(a>b)
print(a<2)
print(a!=b) #<> a khác b
print(a!=2) # a khác 2
print(a==2) # a bằng 2
print(a<=2) # a nhỏ hơn hoặc bằng
print(a>=2) # a lớn hơn hoặc bằng
# gán giá trị
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a**=b
print(a)
# logic (and, or, not)
a= True
b= False
print(a and b)
print(a or b)
print(not a)
print(not b)
# membership (in, not in)
a = 'Hello World'
print('W' in a)
print('H' in a)
print('e' not in a)

# truy cập từng giá trị
_type1=('one','two','three','four')
_type2=(10,20,30,40,50,60)
_type3=('Nguyen Huyen')

print(_type1[2])
print(_type2[3])
print(_type3[-5:])
print(len(_type3)) # đếm số lượng phần tử

for num in _type2: # lặp qua từng phần tử và hiển thị giá trị
    print(num/10)

for index, num in enumerate(_type1): #lặp từng phần tử và hiển thị vị trí, giá trị
    print('stt:', index,'value:',num)

print(_type1.count('three')) # đếm số lần xh của 1 value
print(_type3.count('n'))

print(_type1.index('three')) # kiểm tra vị trí của 1 value

# kiểu dữ liệu string
name ='Nguyen Huyen'
print(type(name)) # kiểm tra kiểu biến
print(len(name))
print(name[2:6])

print(name.find('n')) # tìm thứ tự của 1 ký tự
print(name.lower()) # trả về kí tự thường
print(name.upper()) # trả về kí tự hoa
for char in name:
    print(char)

mytuple = (20,'huyen',['one','two'], False)
print(mytuple[1])
print(mytuple[0:2])
print(type(mytuple[0:1]))
print(len(mytuple))

# kiểu dữ liệu list
drinks =['sting','pepsi','sprite','coca cola']
numbers =[3,27,12,4,1,99]
print(drinks[0:3])

astring ='ndbeax'
print(list(astring))

print(sorted(drinks)) # sắp xếp list
print(sorted(numbers))
print(sorted(astring))

drinks[2]= '7up' # mutable
print(drinks)
drinks.append('sprite') # thêm phần tử
print(drinks)
del(drinks[3]) #xoa phan tu
print(drinks)
drinks.remove('pepsi')
print(drinks)

# dictionary
languageCreators = {'python':'ran va hoa hong','php':'davinci'}
print(languageCreators['python'])
languageCreators['python']='rose' #thay doi
print(languageCreators)
del languageCreators['php']
print(len(languageCreators))
persident={2009:'obama',2019:'trump'}
print(max(persident)) #gia tri key lon nhat
print(min(persident)) #key nho nhat

print(persident.keys()) # lay all key
print(persident.values()) #lay all values
print(persident.get('php'))
print(persident.get(2009))

