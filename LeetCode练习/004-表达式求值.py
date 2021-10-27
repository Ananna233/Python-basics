#前缀表达式又称波兰表达式  后缀表达式又称逆波兰表达式
#p27-P28
#中缀转后缀  后缀计算
#假设输入是合法的，且输入为整数

#=================================
# 表达式转后缀表达式
# 步骤:
# 1.遇到操作数：直接加入后缀表达式
# 2.遇到界限符：遇到 '(' 直接入栈；遇到 ')'则依次弹出栈内运算符（按规则3）并加入后缀表达式，直到弹出'('为止，'('不加入后缀表达式
# 3.遇到运算符：依次弹出栈中优先级高于或等于当前运算符的所有运算符，并加入后缀表达式，若碰到'('或者栈空停止，之后把当前运算符入栈
def toPostfix_expression(express):
    operational_character = []  #运算符栈
    expression_stack = []  #后缀表达式
    lev = {  #运算符等级
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '(':3,
        ')':3
    }
    for i in express:
        # print(i,operational_character,expression_stack)
        if i not in ['+','-','*','/','(',')']:  #操作数入后缀表达式
            expression_stack.append(i)
        else:
            if i == '(':  #规则2，左括号直接入栈
                operational_character.append(i)
            elif i == ')':  #规则2,右括号直接弹出所有运算符直到遇到左括号  另外：括号不入表达式
                tmp = operational_character.pop()
                while tmp!='(':
                    expression_stack.append(tmp)
                    tmp = operational_character.pop()
            elif operational_character == []:  #如果栈是空的  入栈
                operational_character.append(i)
            elif lev[i]>lev[operational_character[-1]] or operational_character[-1]=='(':  #栈中最后运算符等级低于当前运算符或者最后运算符为左括号 入栈
                operational_character.append(i)

            elif lev[i]<=lev[operational_character[-1]]:  #最后运算符同等级或低等级 则弹出 ，直到栈空或者当前运算符等级高于栈中最后运算符等级
                while operational_character[-1]!='(' and lev[i]<=lev[operational_character[-1]]:  #直到栈空或者当前运算符等级高于栈中最后运算符等级
                    tmp = operational_character.pop()
                    expression_stack.append(tmp)
                    if operational_character == []:  #栈空跳出
                        break
                operational_character.append(i)  #栈中较高级运算符全部弹出后，入栈

    while operational_character!=[]:  #循环结束后弹出栈中剩余所有运算符
        tmp = operational_character.pop()
        expression_stack.append(tmp)

    return expression_stack  #返回后缀表达式


def evalRPN(tokens: list) -> int:
    tmp = []  #使用栈
    for i in tokens:
        if i not in ['+','-','*','/']:
            tmp.append(int(i))  #如果是操作数 字符串转数字  入栈
        else:
            b = tmp.pop()  #如果是操作符  将栈中前面两个操作数出栈，左操作数为a，后出栈，右操作数为b先出栈
            a = tmp.pop()
            if i == '+':
                tmp.append(a+b)
            elif i == '-':
                tmp.append(a-b)
            elif i == '*':
                tmp.append(a*b)
            else:
                tmp.append(int(a/b))
    return tmp.pop()  #输入的表达式合法则最后只剩结果

# toke = '((5/(7-(1+1)))*3)-(2+(1+1))'
# toke = ['(', '(', '15', '/', '(', '7', '-', '(', '1', '+', '1', ')', ')', ')', '*', '3', ')', '-', '(', '2', '+', '(', '1', '+', '1', ')', ')']
toke = ['(', '(', '10', '*', '(', '6', '/', '(', '(', '9', '+', '3', ')', '*', '-11',')', ')', ')', '+', '17', ')', '+', '5']
aa = toPostfix_expression(toke)
print(evalRPN(aa))