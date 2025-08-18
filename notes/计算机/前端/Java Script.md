---
date: "2025"
tags:
  - 前端
  - JavaScript
---
## 一. JavaScript 是什么

#### a. 定义
JavaScript 是一种运行在客户端（浏览器）的编程语言，实现人机交互效果。
#### b. 作用
• **网页特效**  
• **表单验证**  
• **数据交互**  
• **服务端编程**（如 `Node.js`）
#### c. 书写位置
##### i. 行内 JS
```html
<button onclick="alert('Hello')">点击我</button>
```
##### ii. 内部 JS
1. 直接写在 HTML 文件里，用 `<script>` 标签包住。  
2. **规范**：`<script>` 标签写在 `</body>` 上面。  
3. **拓展**：`alert('Hello')` 页面弹出警告对话框。  
   ```html
   <body>
     <script>
       alert("Hello");
     </script>
   </body>
   ```
##### iii. 外部 JS
1. 代码写在以 `.js` 结尾的文件里。  
2. **语法**：通过 `<script>` 标签，引入到 HTML 页面中。  
   ```html
   <body>
     <script src="xxx.js"></script>
   </body>
   ```
3. **注意**：外部 JS 中间不允许写内部 JS，否则会被忽略。
#### d. 注释
##### i. 单行注释
1. **符号**：`//`  
2. **快捷键**：`Ctrl + /`  
   ```javascript
   // 这是单行注释
   ```
##### ii. 块注释
1. **符号**：`/* */`  
2. **快捷键**：`Shift + Alt + A`  
   ```javascript
   /* 这是块注释 */
   ```
#### e. 结束符
在 JavaScript 中，`;` 可写可不写。
#### f. 输入输出语法
##### i. 输出
1. `document.write("xxxx")`  
2. `console.log("xxxx")`  
3. `alert("xxxx")`  
##### ii. 输入
```javascript
prompt("xxxx");
```
---
## 二. 变量
#### a. 声明变量
• **关键字**：`let`  
  ```javascript
  let variableName;
  ```
#### b. 变量赋值
• **语法**：`variable = value`  
• **初始化**：在变量声明时赋值  
  ```javascript
  let variableName = value;
  ```
• **声明多个变量**：与 C 语言一致（不推荐一次声明多个变量）  
  ```javascript
  let a = 1, b = 2, c = 3;
  ```
#### c. 变量命名规范
• 与 C 语言命名规范一致（如驼峰命名法）。
#### d. 拓展
##### i. `let` 和 `var` 的区别
• **`var`**：老版本 JS 中使用，现在一般不再使用。  
  • 可以先使用再声明。  
  • 可以重复声明。  
  • 存在变量提升、全局变量、没有块级作用域等问题。
##### ii. `var` 声明示例
```javascript
console.log(x); // undefined（变量提升）
var x = 10;
var x = 20; // 可以重复声明
```
#### e. 数组
##### i. 声明方式
```javascript
let arrayName = [value1, value2, value3, ..., valueN];
```
或
```javascript
let arr = new Array(value1, value2, ..., valueN);
```
##### ii. 数组操作 - 新增
• `arr.push()`：尾增，返回数组的长度。  
• `arr.unshift()`：头增，返回数组的新长度。
##### iii. 数组操作 - 删除
• `arr.pop()`：尾删，返回该元素的值。  
• `arr.splice(start, deleteCount)`：删除指定元素。  
• `arr.shift()`：头删，返回该元素的值。

---
## 三. 常量

#### a. 概念
• 使用 `const` 声明的变量称为常量。  
• 常量是不可变的值，不允许重新赋值，声明时必须赋值。  
  ```javascript
  const PI = 3.14;
  ```
---
## 四. 数据类型
#### a. 数据类型分两大类
##### i. 基本数据类型

1. **`number` 数字型**  
   ```javascript
   let num = 10;
   ```
2. **`string` 字符串型**  
   • 单引号和双引号都可以。  
   • 字符串相加（`+`），表示字符串拼接。  
   • **模板字符串**：  
     ◦ **使用场景**：拼接字符串和常量。  
     ◦ **语法**：  
       ◦ 使用反引号 `` ` ``。  
       ◦ 内容拼接时，用 `${}` 包住变量。  
     ```javascript
     let name = "Alice";
     let message = `Hello, ${name}!`;
     ```
3. **`boolean` 布尔型**  
   • 只有 `true` 和 `false` 两个值。  
   ```javascript
   let isTrue = true;
   ```
4. **`undefined` 未定义型**  
   • 只有一个值 `undefined`。  
   • 在声明一个变量但未赋值时，默认为 `undefined` 数据类型。  
   ```javascript
   let x;
   console.log(x); // undefined
   ```
5. **`null` 空类型**  
   • 使用场景：把 `null` 作为尚未创建的对象。  
   ```javascript
   let obj = null;
   ```
6. **`undefined` 和 `null` 的区别**  
   • `undefined` 表示没有赋值。  
   • `null` 表示赋值了，但值为空。
##### ii. 引用数据类型

1. **`object` 对象**  
   ```javascript
   let person = { name: "Alice", age: 25 };
   ```
##### iii. 检测数据类型

• **关键词**：`typeof x` 或函数形式 `typeof(x)`。  
  ```javascript
  console.log(typeof 10); // "number"
  console.log(typeof "Hello"); // "string"
  ```
#### b. 类型转换
##### i. 使用表单、`prompt` 取来的数据默认是 `string` 类型，需要转换。
##### ii. 隐式转换
1. 在执行某些运算符时，系统自动将数据类型进行转换。  
2. `+` 号两边只要有一个字符串，会把另一个转成字符串。  
3. `-`、`*`、`/` 等会把数据转换成数字类型。  
4. **缺点**：转换类型不明确。  
5. `+` 号作为正号解析可以转成数字型。  
6. 任何数据和字符串相加结果都是字符串。  
##### iii. 显式转换

1. **`Number(xxx)`**  
   ```javascript
   let str = "123";
   let num = Number(str); // 123
   ```
2. **`parseInt(xxx)`**  
   • 只保留整数。  
   ```javascript
   let str = "123.45";
   let num = parseInt(str); // 123
   ```
3. **`parseFloat(xxx)`**  
   • 可以保留小数。  
   ```javascript
   let str = "123.45";
   let num = parseFloat(str); // 123.45
   ```
---
## 五. 运算符
#### a. 赋值运算符
• `=`：赋值  
• `+=`：加后赋值  
• `-=`：减后赋值  
• `*=`：乘后赋值  
• `/=`：除后赋值  
**示例**：
```javascript
let x = 10;
x += 5; // x = 15
```
#### b. 一元运算符
• `+`：正号  
• `-`：负号  
• **自增自减**：`++`、`--`  
  • **前置**：先运算，后赋值。  
    ```javascript
    let x = 10;
    let y = ++x; // x = 11, y = 11
    ```
  • **后置**：先赋值，后运算。  
    ```javascript
    let x = 10;
    let y = x++; // x = 11, y = 10
    ```
#### c. 比较运算符
• `<`、`>`、`>=`、`<=`、`==`：比较值是否相等。  
• `===`：比较值和类型是否都相等。  
• `!==`：比较值和类型是否不全等。  
**示例**：
```javascript
console.log(10 == "10"); // true
console.log(10 === "10"); // false
```
#### d. 逻辑运算符
• `&&`：逻辑与  
• `||`：逻辑或  
• `!`：逻辑非  
**示例**：
```javascript
let a = true, b = false;
console.log(a && b); // false
console.log(a || b); // true
console.log(!a); // false
```
#### e. 运算符优先级
运算符优先级从高到低依次为：  
1. 一元运算符（`++`、`--`、`!` 等）  
2. 算术运算符（`*`、`/`、`+`、`-` 等）  
3. 比较运算符（`<`、`>`、`==` 等）  
4. 逻辑运算符（`&&`、`||` 等）  
5. 赋值运算符（`=`、`+=` 等）  
---
## 六. 语句
#### a. 顺序
代码从上到下依次执行。  
```javascript
let a = 10;
let b = 20;
console.log(a + b); // 30
```
#### b. 分支
• **`if` 语句**：  
  ```javascript
  if (条件) {
    // 条件为真时执行
  } else {
    // 条件为假时执行
  }
  ```
• **`switch` 语句**：  
  ```javascript
  switch (表达式) {
    case 值1:
      // 执行代码
      break;
    case 值2:
      // 执行代码
      break;
    default:
      // 默认执行代码
  }
  ```
#### c. 循环
• **`for` 循环**：  
  ```javascript
  for (let i = 0; i < 10; i++) {
    console.log(i);
  }
  ```
• **`while` 循环**：  
  ```javascript
  let i = 0;
  while (i < 10) {
    console.log(i);
    i++;
  }
  ```
• **`do...while` 循环**：  
  ```javascript
  let i = 0;
  do {
    console.log(i);
    i++;
  } while (i < 10);
  ```
---
## 七. 函数
#### a. 函数声明
```javascript
function 函数名(参数1, 参数2, 参数3, ..., 参数n) {
  // 函数体
}
```
#### b. 匿名函数
1. **定义**：匿名函数是没有函数名的函数。  
2. **特点**：匿名函数不能直接调用。  
3. **使用方法**：  
   • **函数表达式**：将匿名函数的值赋给一个变量，通过变量来调用函数。  
     ```javascript
     let func = function() {
       console.log("匿名函数");
     };
     func();
     ```
   • **立即执行函数**：避免全局变量之间的污染。  
     ◦ **写法**：`(function(){})();`  
     ◦ **注意**：立即执行函数后面必须加分号。  
     ◦ **参数**：后面一个括号里可以写参数。  
	 ```javascript
    (function(a, b) {
	  console.log(a + b);
	})(10, 20);
     ```
   • **在 API 部分会用到**。  
4. **隐式全局变量**：在函数中使用没有声明的变量，该变量为隐式全局变量。  
---
## 八. 逻辑中断
#### a. 短路
只存在于 `&&` 和 `||` 中，当满足一定条件会让右边的代码不执行。  
#### b. 示例
```javascript
console.log(false && a++); // && 右边的代码不执行
console.log(true || a++);  // || 右边的代码不执行
```
#### c. 返回值规则
• 如果 `&&` 两侧都是真值，则返回最后一个真值。  
• 如果 `||` 两侧都是真值，则返回第一个真值。  
---
## 九. 布尔型转换

#### a. 布尔值转换规则
• 空字符串、`undefined`、`null`、`false`、`NaN` 转换为布尔值后都是 `false`，其余为 `true`。  
#### b. 隐式转换
1. 有字符串的加法 `" " + 1`，结果是 `"1"`。  
2. 减法 `-` 只能用于数字，它会使空字符串变为 `0`。  
3. `null` 经过数字转换后会变为 `0`。  
4. `undefined` 经过数字转换后会变为 `NaN`。  
---
## 十. 对象

#### a. 对象（Object）也是一种数据类型

#### b. 一种无序的数据集合的抽象

#### c. 对象使用

##### i. 声明方式：
1. **字面量声明**：
   ```javascript
   let objectName = {};
   ```
2. **构造函数声明**：
   ```javascript
   let objectName = new Object();
   ```
##### ii. 对象由属性和方法组成
```javascript
let objectName = {
  属性名: 属性值,
  方法名: 函数
};
```
##### iii. 属性
1. 数据描述性信息为属性。  
2. 属性成对出现，包括属性名和属性值，使用 `:` 分隔。  
3. 多个属性值之间用 `,` 分隔。  
4. 属性是依附在对象上的变量。  
**示例**：
```javascript
let person = {
  name: "Alice",
  age: 25
};
```
##### iv. 对象使用方法
1. **查属性**：
   ```javascript
   对象名.属性;  // 或 对象名['属性'];（一定要加引号）
   ```
2. **改属性**：
   ```javascript
   对象名.属性 = 新值;
   ```
3. **增属性**：
   ```javascript
   对象名.新属性 = 新值;
   ```
4. **删属性**：
   ```javascript
   delete 对象名.属性;
   ```
##### v. 方法
1. 数据行为型的信息。  
2. 方法由方法名和函数两部分构成，使用 `:` 分隔。  
3. 多个属性之间使用英文 `,` 分隔。  
4. 方法是依附于对象的函数。  
**示例**：
```javascript
let person = {
  name: "Alice",
  sayHello: function() {
    console.log("Hello!");
  }
};
person.sayHello(); // 调用方法
```
##### vi. 遍历对象
1. 使用 `for...in` 循环遍历对象：
   ```javascript
   for (let k in obj) {
     console.log(k);        // 属性名
     console.log(obj[k]);   // 属性值
   }
   ```
##### vii. 内置对象
1. JS 内部提供的对象，包含各种属性和方法给开发者。  
2. **重要的内置对象**：`Math`  
   • **`random`**：生成 `0~1` 之间的随机数。  
     ◦ 返回一个 `[0,1)` 的随机小数。  
     ◦ 生成 `0-10` 之间的随机数：`Math.floor(Math.random() * (10 + 1))`。  
     ◦ 生成 `5-10` 之间的随机数：`Math.floor(Math.random() * (5 + 1)) + 5`。  
     ◦ 生成 `N-M` 之间的随机数：`Math.floor(Math.random() * (M - N + 1)) + N`。  
   • **`ceil`**：向上取整。  
   • **`floor`**：向下取整。  
   • **`max`**：找最大数。  
   • **`min`**：找最小数。  
   • **`pow`**：幂运算。  
   • **`abs`**：取绝对值。  
---
JavaScript更进阶的用法[[Web API]]


---

DONE

---