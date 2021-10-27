# 变量.rstrip()  删除字符串结尾的空白
# 变量.lstrip()  删除字符串开头的空白
# 变量.strip()   删除字符串开头、结尾的空白
# 这种改变是暂时的
language = '  Python  '
print(language)           #   Python  <<空格
print(language.rstrip())  #   Python<<
print(language.lstrip())  # Python  <<
print(language.strip())   # Python<<
print(language)           #   Python  <<改变不会记录进变量
lan = language.strip()
print(lan)                # Python<<可以使用另一个变量记录

a = '  hello   world  '
print(a.strip())          #hello   world<<中间不会被去掉