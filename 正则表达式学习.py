#匹配1-100之间的数字
import re
s=1
res=re.match(r'100|([1-9]?[1-9]$)',str(s))
print(res.group())




#匹配座机号码
s='0101-67113292'
import re
res=re.match(r'(\d{3}-\d{8}$)|(\d{4}-\d{7}$)',s)
print(res.group())



#对输入的qq号进行匹配（qq匹配规则：长度为5-10位，纯数字组成，且不能以0开头。
s='39663212323'
import re
res=re.match(r'[1-9]\d{4,9}$',s)
print(res.group())


#查找字符串中有多少个af
s='sadqweafqweaflsajdfaaf'
import re
res=re.findall(r'af',s)




#规则是按照空格出现一次或者多次切割
s = "zhangsan   lisi     wangwu    "
res=re.split(r'\s+',s)





#用正则\\切割
s = "c:\\abc\\a.txt"
res=re.split(r'\\',s)



#将连续5个以上数字替换成#
s = "wer89346juo123wa89320571f"
res=re.sub(r'\d{5,}','#',s)


#取出字符串中的所有字母 
s = "abDEe23dJfd343dPOddfe4CdD5ccv!23rr"
res=re.findall(r'[a-zA-Z]+',s)



#找出以字母e结尾的单词，忽略大小写
s = 'THREE people at HERE do some THING'
res=re.findall(r'\w+e\b',s,re.I)



#将多个重复字母替换成&
import re
s = "cudddbhuuujdddcaa"
res=re.sub(r'(\w)\1+','&',s)

#将多个重复字母替换成一个字母（比如ddd替换成d）
s = "cudddbhuuujddd"
res=re.sub(r'([a-zA-Z])\1+',r'\1',s)

#获取长度为3个字母的单词
s = "min tian jiu yao fang jia le ,da jia"
res=re.findall(r'\b[a-zA-Z]{3,3}\b',s)


#将字符串变成 '我要学编程'
s = "我我...我我...我要..要要...要要...学学学...学学...编编编..编程..程.程...程...程"
res=re.sub(r'\W+','',s)
ret=re.sub(r'(\w)\1+',r'\1',res)

#去掉div和b标签
s = "<div class='a'>正则<span>表达式</span><b style='color:red'>练习</b></div>"
res=re.sub(r'(</?div.*?>)|(</?b.*?>)','',s)


s='123abc456'
import re
res=re.search(r'[a-zA-Z]{1,}',s)


s = 'abc abcde bc bcd'
res=re.findall(r'\sbc\s',s)  

s='abababa babbabb aabaab'
re.findall( r'(ab)' , s )


s = 'aaa bbb111 cc22cc 33dd '  #匹配以下字符串中的前一部分是字母，后一部分是数字或没有的变量名字
res=re.findall(r'\b[a-zA-Z]+[0-9]*\b',s)




s ='123 10e3 20e4e4 30ee5'
res=re.findall(r'\b\d+e?\d?\b',s)





s='123 456 789'
res=re.findall(r'\d.*?',s)





s='<table><tr>hello world 18111234589<tr><tr><span>name:张三,tel:18711001111</span></tr></table>'
res=re.findall(r'\d+',s)
res=re.search(r'<span>\w+</span>',s)
start = s.find('<span>')
end = s.rfind('</span')


s='12faslkdj34'
res=re.search(r'12\w+34',s)




import re
s= '''张伟 86-14870293148  \n
   王伟   +86-13285654569    \n
    王芳        15856529115    \n
 李伟         13022816340  \n
  王秀英   (86)14785720656     \n
   李秀英    17201444672    \n
    李娜         15682812452     \n
    张秀英         14326967740     \n
    刘伟  15146435743    \n
   张敏        (86)-17712576838   \n
    李静       86 14295083635  \n
    张丽     (+86) 13722348123   \n
   王静         17587918887   \n
  王丽    15493106739    \n
 李强      13786842977   \n
 张静         86-15542304386     \n
    李敏         15642387356 \n
   王敏          18627216756  \n
 王磊       17206185726   \n
    李军      17857426238     \n
   刘洋        17345352790     \n'''

res=re.findall(r'\d{11}',s,re.I)   #11位电话号码
dianhua=re.findall(r'1[38]\d{9}',s)  #提取所有 18 或 13 开头的电话号码
mingzi=re.findall(r'王\w+',s,re.I|re.M)
zhang=re.findall(r'(?P<张的号码是>(?<=(?:张\S)).*)',s,re.I|re.M)



str = """
  张伟         1996.8.24 
   王伟      1993年10月21日   
 王芳         1997-7-24   
   李伟       1996.3.21  
   王秀英        1991.12.0  
   李秀英     1994-7-5    
   李娜       1999.1.28   
   张秀英        1998-2-24   
   刘伟     1996.5.28      
   张敏      1996.10.26   
  李静      1993年1月6日    
   张丽        1992.5.21     
   王静  1998-5-1  
    王丽   1994-4-14  
   李强  1993.8.13   
   张静          1998年1月5日   
   李敏    1993-8-21  
   王敏      1997-3-7    
   王磊     1999-3-18    
  李军         1990-12-18  
    刘洋   1995年5月7日  
"""

riqi=re.findall(r'\d{4}[-.年]\d{1,2}[-.月]\d{1,2}日?',str)   #所有日期
shengri=re.findall(r'\D+\d{3}[0-5][-.年]\d{1,2}[-.月]\d{1,2}日?',str,re.I|re.M)


for i in shengri:
    print(i)

b = re.findall(r'\S+\s+1\d{2}[0-5][年.-]?\d{1,2}[月.-]?\d{1,2}\S?',str) 

c = re.sub(r'\s*(\S+)\s+(\d{4})[年.-]?(\d{1,2})[月.-]?(\d{1,2})\S?',r'\1  \2 年 \3 月 \4 日 \n',str) 




a='18880668813519'
res=re.findall(r'([0-9])\1{2,}',a)



phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My Number is 411-234-4566')
# 建议都打出来看看
print(mo1.group())
print(mo1.group(1))
print(mo1.groups())






s='1878787887787878787'
res=re.findall(r'(87){3}',s)
res.groups()




noNewlineRegex = re.compile('.*')
noNewline = noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
print(noNewline)
newlineRegex = re.compile('.*', re.DOTALL)
newline = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(newline)



s='1887878787'
res=re.search(r'(87){2,}',s)





s='qweioqwehalshdafilqwehlqeqfalifhqwqafafoiqweqhjlbxjkcafioqwuehqjleqjrnlqkjfkdsnfkjherlkq12u1lorhjvnlaflkhqwrqlwraf'
res=re.findall(r'af',s)







import re
s = '我我...我我...我要..要要...要要...学学学...学学...编编编..编程..程.程...程...程'
res=re.sub(r'\W+','',str(s))
ret=re.sub(r'(\w)\1+',r'\1',res)




s="i love you not because of who you are, but because of who i am when i am with you"

res=re.findall(r'^\w+|\s\w',s)
content=re.findall(r"\b\w",s)

s="i love you not because 12sd 34er 56df e4 54434"
res=re.findall(r'\b\d',s)

s="i love you not because\n12sd 34er 56\ndf e4 54434"
res=re.findall(r'^(\w+\s*){1,}',s,re.I|re.M)





