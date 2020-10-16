# <center>1.4 单元测试-执行</center>   

---   

## 目标
	1. 回顾UnitTest框架使用
	2. 基于UnitTest测试三角形案例
	3. 在UnitTest框架中使用数据分离

---  
## 什么是单元测试执行？

	概念：通过单元测试框架对要进行测试代码的实践过程

---

## 1. 练习1
	
	1. 通过Python语言编写一个运算的类(Calc)，类中包含两个函数：

		1) add(self,a,b) 返回a+b之和
		2) sub(self,a,c) 返回a-c之差

	提示：通过练习1，我们先简单复习下UnitTest框架的使用

### 1.1 练习1 步骤分析
	
	1. 新建Calc类
	2. 在Calc类中新建add函数
	3. 在Calc类中新建sub函数
	4. 调用对象中方法

### 1.2 练习1 单元测试   
	
	1. 导包 UnitTest 、Calc类
	2. 新建单元测试类 (集成 unitTest.TestCase)
	3. 新建testAdd()函数
	4. 新建testSub()函数
	5. 执行测试

### 1.3 总结
	
	1. 导包
	2. setUp 函数作用
	3. tearDown 函数作用
	4. 断言
	5. 运行测试函数

### 1.4 问题
	
	1. 练习1我们数据直接写入代码中，如果数量庞大，我们需要频繁改动数据或复制冗余代码进行实现数据测试目的。
	2. 做不到数据分离(代码和数据分开)，不便维护；

---

## 参数化
	概念：根据需求动态获取数据并进行赋值的过程

## 2. 参数化-方式
	
	1. XML格式（1）
	3. CSV格式（2）
	2. JSON串 （3）
	4. TXT文本（4）

	提示：括号内为推荐使用优先级，从小到大;1-2为扩展了解，3-4建议重点了解     

---

## 3. XML是什么？
	概念：XML是一种标记语句，很类似HTML标记语言；后缀 .xml

### 3.1 XML与HTML区别？
	XML是传输和存储数据，焦点在数据；HTML是显示数据，焦点在外观；

### 3.2 XML格式是什么？
	<?xml version="1.0" encoding="UTF-8"?>
	<book category="面授">
		  <title>单元测试</title> 
		  <author>XST</author> 
		  <year>2008</year> 
		  <price>39.95</price> 
	</book>

	1. 必须有XML声明语句：<?xml version="1.0" encoding="UTF-8"?>
	2. 必须要有一个根元素，如：<book>
	3. 标签大小写敏感
	4. 属性值用双引号
	5. 标签成对
	6. 元素正确嵌套
	7. 标签名可随意命名,但有以下限制
		1) 不能以数字或者标点符号开始参
		2）不能以字符 “xml”（或者 XML、Xml）开始
		3) 名称不能包含空格

### 3.3 需求

	对三角形案例单元测试使用XML格式进行参数化

### 3.4 操作步骤
	
	1. 编写XML数据文件
	2. 编写读取XML模块函数
	3. 单元测试模块中引用XML读取函数
	4. 执行

### 3.5 重点分析    

	1. 导入XML包 from xml.dom import minidom
	2. 加载解析 dom=minidom.parse(filename)
	3. 获取对象  root=dom.documentElement
	4. 获取子元素 aas=root.getElementsByTagName(one)[0]
	5. 获取子元素值 aas.getElementsByTagName(two)[0].firstChild.data

### 3.6 XML-总结
	
	1. 读取方式
	2. 什么是XML
	3. XML与HTML区别
	4. XML编写格式
	5. 缺点：不适合大量参数化数据时使用    

---

## 4. CSV格式
	概念：CSV是一种以逗号做分割的表格格式; 后缀 .csv

### 4.1 使用CSV实现三角形案例参数化-操作步骤

	1. 创建CSV文件
	2. 编写CSV读取模块函数
	3. 单元测试-引用CSV读取函数
	4. 执行

### 4.2 重点分析
	
	1. 导包 import csv
	2. 打开csv文件 
			with open("../Data/sjx.csv","r",encoding="utf-8") as f:
				lines=csv.reader(f)

### 4.3 CSV-总结
	
	1. 读取方式
	2. 生成CSV文件方式
	3. 编码

---

## 5. 什么是JSON？
	概念：一种轻量级数据交换格式；后缀名 .json
	提示：
		接口测试一般使用JSON为接口传递数据规范格式，所以我们有必要对如何获取JSON数据做个了解；   

### 5.1 JSON格式
	格式：{"name":"张三","age":28}
	提示：由键值对组成,健名和值之间使用分号(:)分割，多个键值对之间使用逗号(,)分割

### 5.2 使用JSON实现三角形案例参数化-操作步骤
	
	1. 编写JSON文件
	2. 编写JSON读取模块函数
	3. 单元测试-引用JSON读取函数
	4. 执行

### 5.3 难点分析
	
	1. 导入JSON包（import JSON）
	2. 打开JSON文件并解析
		with open('../DataXML/sjx.json','r',encoding='utf-8') as f:
            file=json.load(f)

### 5.4 JSON-总结
	
	1. JSON概念
	2. JSON格式
	3. 如何导入JSON包
	4. 如何加载JSON

---   

## 6. TXT文本
	概念：一种纯文本格式; 后缀名 .txt

### 6.1 TXT文本优点：
	
	1. 编写测试数据方便
	2. 使用模块函数读取时便捷

### 6.2 使用TXT实现三角形案例参数化-操作步骤
	
	1. 创建txt文本并写入测试数据
	2. 编写读取txt模块函数
	3. 单元测试-引用JSON读取函数
	4. 执行

### 6.3 难点分析
	
	1. 如何读取txt文本？
			with open(r'../DataXML/三角形.txt','r',encoding='utf-8') as f:
	2. 如何去除行尾/n换行符？
			line.strip()

### 6.4 TXT总结
	
	1. TXT文本读取
	2. 去除行尾回车符(/n)    

---

## 7. 参数化-总结
	
	1. XML
	2. CSV
	3. JSON
	4. TXT
