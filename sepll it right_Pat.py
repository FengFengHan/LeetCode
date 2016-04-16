s = input()
if(s.find(" ") != -1):
    s = s.split()
sum_ = 0
for i in range(len(s)):
    sum_ += ord(s[i]) - ord('0')
digits = list()
if sum_ == 0:
    digits.append(0)
while sum_ != 0:
    digits.append(sum_ % 10)
    sum_ = sum_ // 10
englishs = ["zero","one","two", "three","four","five",
            "six","seven","eight","nine","ten"]
print(englishs[digits.pop()],end="")
while(len(digits) > 0):
    print(" ",end="")
    print(englishs[digits.pop()],end="")
print()
