# coding=utf-8

class tree:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

def PreOrder_Init(cmd,ct):
    if (cmd[ct[0]] != '_'):
        new = tree(cmd[ct[0]],None,None)
        root = new
        ct[0] += 1
        # print (ct)
        root.left = PreOrder_Init(cmd,ct)
        root.right = PreOrder_Init(cmd,ct)
        return root
    else:
        ct[0]+=1
        return None

def PreOrder_Vist(root):
    if (root!=None):
        print ("%c"%root.val,end='')
        PreOrder_Vist(root.left)
        PreOrder_Vist(root.right)
    else:
        print ("_",end='')


if __name__ == "__main__":
    # print ("你好，世界!")
    root = tree(0,None,None)
    cmd = "abc__d__ef___"
    ct = [0]
    root = PreOrder_Init(cmd,ct) # 传地址 list dict set
    PreOrder_Vist(root)          # 传参数 int float double str tuple
