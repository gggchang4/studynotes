# MySQL概述

MySQL Windows Service Name：MySQL80
## MySQL的启动与停止
	方法1:手动 Win+R 输入 services.msc 手动启动关闭MySQL
	方法2：命令行：net start MySQL80/net stop MySQL80

## MySQL客户端连接
	方法1:MySQL提供的客户端命令行工具Command Line Client
	方法2：Windows命令行：首先配置PATH环境变量
	命令：mysql [-h 127.0.0.1] [-p 3306] -u root -p (其中-h-p参数可省略)

## 数据模型
MySQL数据库通过DBMS维护的数据库中的表结构存储数据
### 关系型数据库
建立在关系模型基础上，由多张二维表组成的数据库

# SQL

## SQL通用语法
1. SQL语句可以单行或多行书写，分号结尾
2. SQL语言可以使用空格，缩进
3. MySQL数据库的SQL语言不区分大小写，关键字建议大写
4. 注释：
	1. 单行注释：-- 注释或 # 注释（MySQL特有）
	2. 多行注释：/ * 注释  * /
	3. 
## SQL分类
SQL分以下几类
	1.DDL：数据定义语言，用来定义数据库对象（数据库，表，字段）
	2.DML：数据操作语言，用来对数据库表中的数据进行增删改
	3.DQL：数据查询语言，用来查询数据库表中的记录
	4.DCL：数据控制语言，用来创建数据库用户，控制数据库的访问权限
## DDL
### 数据库操作
1. 查询
	1. 查询所有数据库 `SHOW DATABASES;`
	2. 查询当前数据库 `SELECT DATABASE();`
2. 创建 `CREAT DATABASE [IF NOT EXISTS] 数据库名 [DEFAULT CHARSET 字符集] [COLLATE 排序规则];`
3. 删除 `DROP DATABASE [IF EXISTS]数据库名`;
4. 使用 `USE 数据库名;`

### 表操作
1. 查询
	1. 查询当前数据库所有表 `SHOW TABLES;`
	2. 查询表结构 `DESC 表名;`
	3. 查询指定表的建表语句 `SHOW CREATE TABLE 表名;`
2. 创建
	``` sql
	CREATE TABLE 表名（
		字段1 字段1类型[COMMENT 字段1注释],
		字段2 字段2类型[COMMENT 字段2注释],
		字段3 字段3类型[COMMENT 字段3注释],
		...
		字段n 字段n类型[COMMENT 字段n注释]
	）[COMMENT 表注释];
	```
3. 数据类型
	1. 数值类型
		1. TINYINT
		2. SMALLINT
		3. MEDIUMINT
		4. INT
		5. BIGINT
		6. FLOAT
		7. DOUBLE
		8. DECIMAL
	2. 字符串类型
		1. CHAR
		2. VARCHAR
		3. TINYBLOB
		4. TINYTEXT
		5. BLOB
		6. TEXT
		7. MEDIUMBLOB
		8. MEDIUMTEXT
		9. LONGBLOB
		10. LONGTEXT 
	3. 日期时间类型
## DML
## DQL
## DCL

# 函数

# 约束

# 多表查询

# 事务