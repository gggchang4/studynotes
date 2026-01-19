# STL
Standard Template Library
STL由**容器Container**，**算法Algorithm**，**迭代器Iterator**，仿函数Functors，适配器Adapters，空间配置器组成
STL基于C++模板实现
容器和算法通过迭代器进行连接
- 容器：各种数据结构，如vector，deque等
- 算法：各种常用算法，sort，find，copy等
- 迭代器：容器和算法之间的胶合剂
- 仿函数：行为类似函数，可作为算法的某种策略
- 适配器：一种用来修饰容器或者仿函数或迭代器接口的东西
- 空间配置器：负责空间的配置和管理

## 迭代器Iterator
提供一种方法，使之能够依序访问容器所含的各个元素，而又无需暴露该容器的内部表示方式
每个容器都有自己的专属迭代器
迭代器的使用类似于指针
eg.
```C++
for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it;
}
```

迭代器种类

| 种类      | 功能                           | 支持运算                    |
| ------- | ---------------------------- | ----------------------- |
| 输入迭代器   | 对数据的只读访问                     | ++，== ，！ ， =            |
| 输出迭代器   | 对数据的只写访问                     | ++                      |
| 前向迭代器   | 读写操作，并能向前推进迭代器               | ++ ， == ， ！ ，=          |
| 双向迭代器   | 读写操作，并能向前和向后操作               | ++， -                   |
| 随机访问迭代器 | 读写操作，可以以跳跃的方式访问任意数据，功能最强的迭代器 | ++，--，[n] ,-n，<，<=，>，>= |
常用的容器中迭代器种类为双向迭代器和随机迭代器
如vector：随机迭代器，list/set/map：双向迭代器

## 仿函数Functors
行为像函数的对象
```C++
struct Cmp {
    bool operator()(int a, int b) const {
        return a > b;
    }
};
```
```C++
sort(v.begin(), v.end(), Cmp());

```
## 适配器Adapters
### 容器适配器
|适配器|底层容器|
|---|---|
|`stack`|`deque`|
|`queue`|`deque`|
|`priority_queue`|`vector`|
```C++
priority_queue<int> pq;
```
### 迭代器适配器
```C++
back_inserter(v)
```
# string
本质：
* string是C++风格的字符串，而string本质上是一个类
string和char * 区别：
* char * 是一个指针
* string是一个类，类内部封装了char\*，管理这个字符串，是一个char* 型的容器。
特点：
string 类内部封装了很多成员方法
例如：查找find，拷贝copy，删除delete 替换replace，插入insert
string管理char* 所分配的内存，不用担心复制越界和取值越界等，由类内部进行负责
## 构造函数
构造函数原型：
* `string();`                       //创建一个空的字符串 例如: string str;
- `string(const char* s);`           //使用字符串s初始化
* `string(const string& str);`    //使用一个string对象初始化另一个string对象
* `string(int n, char c);`           //使用n个字符c初始化
```C++
#include <string>
//string构造
void test01()
{
    string s1; //创建空字符串，调用无参构造函数
    cout << "str1 = " << s1 << endl;
    const char* str = "hello world";
    string s2(str); //把c_string转换成了string
    cout << "str2 = " << s2 << endl;
    string s3(s2); //调用拷贝构造函数
    cout << "str3 = " << s3 << endl;
    string s4(10, 'a');
    cout << "str3 = " << s3 << endl;
}
int main() {
    test01();
    system("pause");
    return 0;
}
```

## 赋值
赋值的函数原型：
* `string& operator=(const char* s);`             //char* 类型字符串 赋值给当前的字符串
* `string& operator=(const string &s);`         //把字符串s赋给当前的字符串
* `string& operator=(char c);`                          //字符赋值给当前的字符串
* `string& assign(const char *s);`                  //把字符串s赋给当前的字符串
* `string& assign(const char *s, int n);`     //把字符串s的前n个字符赋给当前的字符串
* `string& assign(const string &s);`              //把字符串s赋给当前字符串
* `string& assign(int n, char c);`                  //用n个字符c赋给当前字符串
```C++
//赋值
void test01()
{
    string str1;
    str1 = "hello world";
    
    string str2;
    str2 = str1;

    string str3;
    str3 = 'a';

    string str4;
    str4.assign("hello c++");

    string str5;
    str5.assign("hello c++",5);

    string str6;
    str6.assign(str5);
    
    string str7;
    str7.assign(5, 'x');
 
}
```
string的赋值方式很多，`operator=`  这种方式是比较实用的

## 字符串拼接
字符串拼接的函数原型
* `string& operator+=(const char* str);`                   //重载+=操作符
* `string& operator+=(const char c);`                         //重载+=操作符
* `string& operator+=(const string& str);`                //重载+=操作符
* `string& append(const char *s); `                               //把字符串s连接到当前字符串结尾
* `string& append(const char *s, int n);`                 //把字符串s的前n个字符连接到当前字符串结尾
* `string& append(const string &s);`                           //同operator+=(const string& str)
* `string& append(const string &s, int pos, int n);`//字符串s中从pos开始的n个字符连接到字符串结尾
```C++
//字符串拼接
void test01()
{
    string str1 = "我";
    str1 += "爱玩游戏";
    str1 += ':';

    string str2 = "LOL DNF";
    str1 += str2;

    string str3 = "I";
    str3.append(" love ");
    str3.append("game abcde", 4);

    str3.append(str2, 4, 3); // 从下标4位置开始 ，截取3个字符，拼接到字符串末尾
}
```

## 字符串的查找和替换
**功能描述：**
* 查找：查找指定字符串是否存在
* 替换：在指定的位置替换字符串
**函数原型：**
* `int find(const string& str, int pos = 0) const;`              //查找str第一次出现位置,从pos开始查找
* `int find(const char* s, int pos = 0) const; `                     //查找s第一次出现位置,从pos开始查找
* `int find(const char* s, int pos, int n) const; `               //从pos位置查找s的前n个字符第一次位置
* `int find(const char c, int pos = 0) const; `                       //查找字符c第一次出现位置
* `int rfind(const string& str, int pos = npos) const;`      //查找str最后一次位置,从pos开始查找
* `int rfind(const char* s, int pos = npos) const;`              //查找s最后一次出现位置,从pos开始查找
* `int rfind(const char* s, int pos, int n) const;`              //从pos查找s的前n个字符最后一次位置
* `int rfind(const char c, int pos = 0) const;  `                      //查找字符c最后一次出现位置
* `string& replace(int pos, int n, const string& str); `       //替换从pos开始n个字符为字符串str
* `string& replace(int pos, int n,const char* s); `                 //替换从pos开始的n个字符为字符串s
```C++
void test01()
{
    //查找
    string str1 = "abcdefgde";
    int pos = str1.find("de");
    if (pos == -1) {
        cout << "未找到" << endl;
    }
    else {
        cout << "pos = " << pos << endl;
    }
    pos = str1.rfind("de");
    cout << "pos = " << pos << endl;
}
void test02()
{
    //替换
    string str1 = "abcdefgde";
    str1.replace(1, 3, "1111");
    cout << "str1 = " << str1 << endl;
}
```
* find查找是从左往后，rfind从右往左
* find找到字符串后返回查找的第一个字符位置，找不到返回-1
* replace在替换时，要指定从哪个位置起，多少个字符，替换成什么样的字符串

## string字符串的比较
**功能描述：**
* 字符串之间的比较
**比较方式：**
* 字符串比较是按字符的ASCII码进行对比
= 返回   0
\> 返回   1
< 返回  -1
**函数原型：**
* `int compare(const string &s) const; `  //与字符串s比较
* `int compare(const char *s) const;`      //与字符串s比较
```C++
void test01()
{
    string s1 = "hello";
    string s2 = "aello";
    int ret = s1.compare(s2);
    if (ret == 0) {
        cout << "s1 等于 s2" << endl;
    }
    else if (ret > 0)
    {
        cout << "s1 大于 s2" << endl;
    }
    else
    {
        cout << "s1 小于 s2" << endl;
    }
}
```
字符串对比主要是用于比较两个字符串是否相等，判断谁大谁小的意义并不是很大

## 字符存取
string中单个字符存取方式有两种
* `char& operator[](int n); `     //通过[]方式取字符
* `char& at(int n);   `                    //通过at方法获取字符
```C++
void test01()
{
    string str = "hello world";
    for (int i = 0; i < str.size(); i++)
    {
        cout << str[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < str.size(); i++)
    {
        cout << str.at(i) << " ";
    }
    cout << endl;
  
    //字符修改
    str[0] = 'x';
    str.at(1) = 'x';
    cout << str << endl;
}
```
string字符串中单个字符存取有两种方式，利用 [ ] 或 at
## 插入和删除
**功能描述：**
* 对string字符串进行插入和删除字符操作
**函数原型：**
* `string& insert(int pos, const char* s);  `                //插入字符串
* `string& insert(int pos, const string& str); `        //插入字符串
* `string& insert(int pos, int n, char c);`                //在指定位置插入n个字符c
* `string& erase(int pos, int n = npos);`                    //删除从Pos开始的n个字符
```C++
//字符串插入和删除
void test01()
{
    string str = "hello";
    str.insert(1, "111");
    cout << str << endl;
    str.erase(1, 3);  //从1号位置开始3个字符
    cout << str << endl;
}
```
## string子串
**功能描述：**
* 从字符串中获取想要的子串
**函数原型：**
* `string substr(int pos = 0, int n = npos) const;`   //返回由pos开始的n个字符组成的字符串
```C++
//子串
void test01()
{
    string str = "abcdefg";
    string subStr = str.substr(1, 3);
    cout << "subStr = " << subStr << endl;

    string email = "hello@sina.com";
    int pos = email.find("@");
    string username = email.substr(0, pos);
    cout << "username: " << username << endl;
}
```
灵活的运用求子串功能，可以在实际开发中获取有效的信息
# vector

**功能：**
* vector数据结构和**数组非常相似**，也称为**单端数组**
**vector与普通数组区别：**
* 不同之处在于数组是静态空间，而vector可以**动态扩展**
**动态扩展：**
* 并不是在原空间之后续接新空间，而是找更大的内存空间，然后将原数据拷贝新空间，释放原空间
![[Pasted image 20251217220518.png|400]]
vector的迭代器是随机访问迭代器

## 构造


# deque

# stack

# queue

# list

# set

# map