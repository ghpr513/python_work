#3.4嘉宾名单
name_list = ['tom','paul','allen','herry']
print(f'I invent you to come this party,{name_list[0].title()}')
print(f'I invent you to come this party,{name_list[1].title()}')
print(f'I invent you to come this party,{name_list[2].title()}')
print(f'I invent you to come this party,{name_list[3].title()}')

#3.5修改嘉宾名单
#以完成练习 3.4 时编写的程序为基础， 在程序末尾添加函数调⽤ print()， 指出哪位嘉宾⽆法赴约。
cannot_name = name_list[1]
name_list.remove(cannot_name)
print(cannot_name.title())
#修改嘉宾名单， 将⽆法赴约的嘉宾的姓名替换为新邀请的嘉宾的 姓名。
name_list.insert(1,'alice')
#再次打印⼀系列消息， 向名单中的每位嘉宾发出邀请
print(f'I invent you to come this party,{name_list[0].title()}')
print(f'I invent you to come this party,{name_list[1].title()}')
print(f'I invent you to come this party,{name_list[2].title()}')
print(f'I invent you to come this party,{name_list[3].title()}')

#3.6添加嘉宾
#调⽤ print()， 指出你找到了⼀张更⼤的餐桌
print("I find a bigger desk.")
#使⽤ insert() 将⼀位新嘉宾添加到名单开头
name_list.insert(0,'tina')
#使⽤ insert() 将另⼀位新嘉宾添加到名单中间
name_list.insert(2,'anna')
#使⽤ append() 将最后⼀位新嘉宾添加到名单末尾
name_list.append('jassica')
#打印⼀系列消息， 向名单中的每位嘉宾发出邀请
print(f'I invent you to come this party,{name_list[0].title()}')
print(f'I invent you to come this party,{name_list[1].title()}')
print(f'I invent you to come this party,{name_list[2].title()}')
print(f'I invent you to come this party,{name_list[3].title()}')
print(f'I invent you to come this party,{name_list[4].title()}')
print(f'I invent you to come this party,{name_list[5].title()}')
print(f'I invent you to come this party,{name_list[6].title()}')

#3.7缩短名单
#在程序末尾添加⼀⾏代码， 打印⼀条你只能邀请两位嘉宾共进晚餐的消息
print("I'm so sorry that I only can invent tow people because the desk can't be sent on time.")
#使⽤ pop() 不断地删除名单中的嘉宾， 直到只有两位嘉宾为⽌。 每次从名单中弹出⼀位， 都打印⼀条消息， 让该嘉宾知道你很抱歉， ⽆法邀请他来共进晚餐。
name_1 = name_list.pop()
print(f"I'm sorry that you can't come,{name_1.title()}.")
name_2 = name_list.pop()
print(f"I'm sorry that you can't come,{name_2.title()}.")
name_3 = name_list.pop()
print(f"I'm sorry that you can't come,{name_3.title()}.")
name_4 = name_list.pop()
print(f"I'm sorry that you can't come,{name_4.title()}.")
name_5 = name_list.pop()
print(f"I'm sorry that you can't come,{name_5.title()}.")
#对于余下两位嘉宾中的每⼀位， 都打印⼀条消息， 指出他依然在 受邀之列
print(f"I'm glad to tell you that you can come,{name_list[0].title()}.")
print(f"I'm glad to tell you that you can come,{name_list[1].title()}.")
#使⽤ del 将最后两位嘉宾从名单中删除， 让名单变成空的。 打印 该名单， 核实名单在程序结束时确实是空的
del name_list[0]
del name_list[0]
print(name_list)