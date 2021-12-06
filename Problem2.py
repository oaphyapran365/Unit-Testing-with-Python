
def calculate(s):
        
        num=0
        res=0
        sign=1
        stack=[]
        
        for char in s:
            if char.isdigit():
                num=num+int(char)
            elif char in ["-","+"]:
                res=res+num*sign
                num=0
                if char=="-":
                    sign=-1
                else:
                    sign=1
            elif char=="(":
                stack.append(res)
                stack.append(sign)
                sign=1
                res=0
            elif char==")":
                res+=sign*num
                res*=stack.pop()
                res+=stack.pop() 
                num=0
        
        return res+num*sign

s = input("Enter your equation:")
eq = calculate(s)
print(eq)
