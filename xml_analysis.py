#!/usr/bin/env python
# coding: utf-8

# url https://blog.csdn.net/shiboyuan0410/article/details/87929497?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
# 介绍一些标签信息

123123
from bs4 import BeautifulSoup
from RawTable import RawTable
from util import *
import os
from tqdm import tqdm

prepath = 'xml/'
savepath = 'json/'
rawpath = ''

filename = 'document.xml'
with open(rawpath+filename,'r',encoding='utf-8') as f:
    con = f.read()
f.close()

soup = BeautifulSoup(con,'lxml')
tbl = soup.find_all('w:tbl')
tbl = tbl[0]

rawTbl = RawTable(tbl)

print('------------ 何伟东 begin--------------')
'''
rawTbl.handleCell()    ###拿到每一个cell的描述信息
for c in rawTbl.tcell:
    print(c)#### 注意有空行
'''



tr_list = tbl.find_all('w:tr')
style = []
for tr in tr_list:
    tc_in_one_tr_style = []
    
    tc_list = tr.find_all('w:tc')
    for tc in tc_list:
        every_tc_style = {}
        tccontent = tc.find_all('w:t')
                
        if tccontent:  
            
            everytc = []
            for i in tccontent:
                everytc.append(i.string)#取出单元格中内容
               
            if (''.join(everytc).split()) != None:
                    
                tc_width = tc.find_all('w:tcw',attrs={"w:w":True})
                if  tc_width:
                    every_tc_style['width'] = tc_width[0].get('w:w')
                else:
                    every_tc_style[width] = 'nowidth'
                
                
                # l.append(tccontent[0].string)
                    #print(tccontent[0].string)
            else : 
                pass
            tc_in_one_tr_style.append(every_tc_style)      
      
    style.append(tc_in_one_tr_style)        
for i in style:
    print (i)
                   








'''
何伟东完善上次写的代码，根据上述拿到的单元格信息，得到每一个单元格的style
公司所给文档的的属性尽量都得到 (就是style部分)
写一个函数 函数的返回值就是那 9 个属性的值
如果某个属性无法得到 就返回None(即什么也不返回)
最后一个占行数量 可能比较难 实在没法实现就与我联系 
'''
print('------------ 何伟东 end--------------')

print('------------ 聂兴潮 begin--------------')
rawTbl.handleCon()
tccontent_list = rawTbl.tccontent_list
for tccon in tccontent_list:
    print(tccon)
'''
写一个类吧 用于处理FormItem  
目前仅仅处理三个属性 label type(暂时都定义为text) required (暂时都定义为True)
也就是主要是处理label   将得到的信息处理为类的数据成员信息
'''
print('------------ 聂兴潮 end--------------')

print('------------ 张世奇 begin--------------')
rawTbl.handleCon()
tccontent_list = rawTbl.tccontent_list
tcloc_list = rawTbl.tcloc_list
length = len(tccontent_list)
for i in range(length):
    print(tcloc_list[i])  ### 表示宽度
    print(tccontent_list[i]) ### 表示内容

'''
写一个类 用于处理layout 
主要是 多元素行(grid) 的处理
如果需要处理syle信息，就暂时跳过 将该信息置为空([])
''' 

print('------------ 张世奇 end--------------')



#for res in rawTbl.tccontent_list:
# for res in results:
#     print(res)

# filenames = os.listdir(prepath)

# for fname in tqdm(filenames):
#     path = prepath+fname

#     tablecon = TableCon(prepath+fname)




#     results = tablecon.mergeLines()

#     savename = fname.split('.')[0]+'.json'

#     saveToFile(savepath+savename,results)


















