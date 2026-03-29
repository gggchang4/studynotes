---
date: "2025"
tags:
  - 前端
  - JavaScript
---
/# 一. WEB API
### a. 在 WEB API 中声明变量 `const` 优先
### b. 作用和分类
#### i. 作用
使用 JavaScript 去操作 HTML 和浏览器。
#### ii. 分类
1. **DOM（文档对象模型）**  
2. **BOM（浏览器对象模型）**  
#### iii. DOM 作用
开发网页内容特效和实现用户交互。
#### iv. DOM 树
1. 将 HTML 文档以树状结构直观地表现出来，称之为文档树或 DOM 树。  
2. 描述网页关系的名词。  
3. **作用**：文档树直观地体现了标签与标签之间的关系。  
#### v. DOM 对象
1. 浏览器根据 HTML 标签生成的 JavaScript 对象。  
2. 所有的标签属性都可以在这个对象上找到。  
3. 修改这个对象的属性会自动映射到标签身上。  
4. **DOM 核心思想**：把网页内容当作对象来处理。  
#### vi. `document` 对象
1. 是 DOM 里提供的一个对象。  
2. 所以它提供的属性和方法都是用来访问和操作网页内容的。  
3. 网页所有内容都在 `document` 里。  
---
# 二. 获取 DOM 对象
### a. 根据 CSS 选择器来获取 DOM 元素
#### i. 选择匹配的第一个元素
1. **语法**：`document.querySelector('CSS选择器')`  
2. **参数**：包含一个或多个有效的 CSS 选择器字符串。  
3. **返回值**：CSS 选择器匹配的第一个元素，一个 `HTMLElement` 对象。  
   • 如果没有匹配到，返回 `null`。  
4. **说明**：获取一个元素可以直接对其进行修改操作。  
**示例**：
```javascript
let element = document.querySelector('.class-name');
```
#### ii. 选择匹配的多个元素
1. **语法**：`document.querySelectorAll('CSS选择器')`  
2. **返回值**：CSS 选择器匹配的 `NodeList` 对象集合。  
3. **说明**：  
   • 获取多个对象不能直接修改，只能通过遍历的方式逐个对每个对象进行修改。  
   • 得到的是一个伪数组：  
     ◦ 有长度和索引号的数组。  
     ◦ 没有 `pop()`、`push()` 等数组方法。  
   • 想要得到里面的每一个对象，需要遍历（`for`）的方式获得。  
**示例**：
```javascript
let elements = document.querySelectorAll('.class-name');
for (let element of elements) {
  console.log(element);
}
```
### b. 其他获取 DOM 方法
1. **通过 ID 获取**：`document.getElementById('id')`  
   • 返回匹配的单个元素。  

2. **通过标签名获取**：`document.getElementsByTagName('tag')`  
   • 返回匹配的 `HTMLCollection` 集合。  

3. **通过类名获取**：`document.getElementsByClassName('class')`  
   • 返回匹配的 `HTMLCollection` 集合。  
**示例**：
```javascript
let elementById = document.getElementById('id');
let elementsByTag = document.getElementsByTagName('div');
let elementsByClass = document.getElementsByClassName('class-name');
```
---
# 三. 操作元素内容

### a. 操作标签本质上就是操作 DOM 对象
### b. 修改标签元素里面的内容
#### i. `对象.innerText` 属性
1. 将文本内容添加/更新到任意标签位置。  
2. 显示纯文本，不解析标签。  
**示例**：
```javascript
element.innerText = "Hello, World!";
```
#### ii. `对象.innerHTML` 属性
1. 将文本内容添加/更新到任意标签位置。  
2. 会解析标签，多标签建议使用模板字符串。  
**示例**：
```javascript
element.innerHTML = "<strong>Hello, World!</strong>";
```
### c. 操作元素的属性
#### i. 操作常用属性
• **语法**：`对象.属性 = 值`  
**示例**：
```javascript
element.src = "image.jpg";
```
#### ii. 操作元素样式属性
1. **通过 `style` 属性操作 CSS**  
   • **语法**：`对象.style.样式属性 = 值`  
   • 如果属性有 `-` 连接符，需要转化为小驼峰命名法。  
   **示例**：
   ```javascript
   element.style.backgroundColor = "red";
   ```
2. **通过 `className` 操作 CSS**  
   • 如果修改的样式比较多，直接通过 `style` 属性修改比较繁琐，可以借助 CSS 类名。  
   • **语法**：`元素.className = 'active'`  
   • **注意**：  
     ◦ 由于 `class` 是关键字，所以用 `className` 代替。  
     ◦ `className` 是使用新值换旧值，如果需要添加一个类，需要保留之前的类名（覆盖之前的类名）。  
   **示例**：
   ```javascript
   element.className = "active";
   ```
3. **通过 `classList` 操作类控制 CSS（常用）**  
   • **语法**：  
     ◦ 追加一个类：`元素.classList.add('类名')`  
     ◦ 删除一个类：`元素.classList.remove('类名')`  
     ◦ 切换一个类：`元素.classList.toggle('类名')`（有就删掉，没有就加上）  
   **示例**：
   ```javascript
   element.classList.add("active");
   element.classList.remove("inactive");
   element.classList.toggle("highlight");
   ```
#### iii. 操作表单元素属性
1. **获取**：`DOM对象.属性名`  
2. **设置**：`DOM对象.属性名 = 新值`  
3. **注意**：`innerHTML` 得不到表单的内容。  
4. **表单属性**：  
   • 添加就有效果，移除就没有效果，一律用布尔值表示。  
   • `true` 代表添加了该属性，`false` 代表移除了该属性。  
   • 例如：`disabled`、`checked`、`selected`。  
**示例**：
```javascript
input.disabled = true;
checkbox.checked = false;
```
#### iv. 自定义属性
1. **标准属性**：标签天生自带的属性，可以直接用点语法操作。  
2. **自定义属性**：  
   • 在 HTML5 中推出专门的 `data-` 自定义属性。  
   • 在标签上一律以 `data-` 开头。  
   • 在 DOM 对象上一律以 `dataset` 对象方式获取。  
**示例**：
```html
<div id="myDiv" data-user-id="123"></div>
<script>
  let userId = document.getElementById("myDiv").dataset.userId;
  console.log(userId); // 123
</script>
```
---
## 四. 定时器-间歇函数

### a. 开启定时器
```javascript
setInterval(函数名, 间隔时间);
```
1. **作用**：每隔一段时间调用这个函数。  
2. **间隔时间单位**：毫秒（ms）。  
3. **调用的函数**：  
   • 可以是声明过的函数（不加 `()` 或加上引号再加 `()`）。  
   • 也可以是匿名函数（必须加 `()`）。  
4. **定时器返回值**：一个 `id` 数字（用于关闭定时器）。  
**示例**：
```javascript
// 使用声明过的函数
function myFunction() {
  console.log("Hello");
}
setInterval(myFunction, 1000);

// 使用匿名函数
setInterval(function() {
  console.log("Hello");
}, 1000);
```
### b. 关闭定时器
```javascript
let 变量名 = setInterval(函数, 间隔时间);
clearInterval(变量名);
```
1. **说明**：一般不会在创建定时器后立即关闭，而是满足一定条件后再关闭。  
**示例**：
```javascript
let timer = setInterval(function() {
  console.log("Hello");
}, 1000);

// 5 秒后关闭定时器
setTimeout(function() {
  clearInterval(timer);
}, 5000);
```
---
# 五. 事件监听
## a. 什么是事件
• 事件是在编程时系统内发生的动作或者发生的事情，例如：单击按钮
## b. 什么是事件监听
• 让程序检测是否有事件发生，一旦有事件触发，就立即调用一个函数做出响应
• 也称为绑定事件或者注册事件
## c. 事件监听
### i. 语法
```javascript
元素对象.addEventListener('事件类型', 要执行的函数)
```
### ii. 事件监听三要素
1. **事件源**：哪个DOM元素被事件触发了，要获取DOM元素
2. **事件类型**：用什么方式触发，比如：
   • 鼠标单击 `click`
   • 鼠标经过 `mouseover` 等
3. **事件调用的函数**：要做什么事
### iii. 旧语法
```javascript
事件源.on事件 = function() {}
```
示例：
```javascript
button.onclick = function() {}
```
**区别**：
• `on` 方式会被覆盖
• `addEventListener` 方式可绑定多次，拥有事件更多特性，更推荐
## d. 事件类型
### i. 鼠标事件
1. `click` 鼠标点击
2. `mouseenter` 鼠标经过
3. `mouseleave` 鼠标离开
### ii. 表单获得光标
1. `focus` 获得焦点
2. `blur` 失去焦点
### iii. 键盘触发
1. `keydown` 键盘按下触发
2. `keyup` 键盘抬起触发
### iv. 表单输入触发
1. `input` 用户输入事件
### v. 获取事件对象event
#### 1. 什么是事件对象
• 事件对象也是对象，对象里有事件触发时的相关信息
#### 2. 使用场景
• 可以判断用户按下哪个键
• 可以判断鼠标点击了哪个元素，从而执行相应的操作
#### 3. 语法：如何获取
• 在事件绑定的回调函数的第一个参数就是事件对象
• 一般命名为 `event`, `ev`, `e`
```javascript
元素.addEventListener('click', function(event) {})
```
#### 4. 属性（部分常用）
| 属性 | 描述 |
|------|------|
| `type` | 获取当前的事件类型 |
| `clientX/clientY` | 获取光标相对于浏览器可见窗口左上角的位置 |
| `offsetX/offsetY` | 获取光标相对于当前DOM元素左上角的位置 |
| `key` | 用户按下的键盘键的值（现在不提倡使用keyCode） |

### vi. 环境对象
#### 1. 定义
• 指的是函数内部特殊的变量 `this`
• 代表着当前函数运行时所处的环境
#### 2. 作用
• 弄清 `this` 的指向可以使代码更加简洁
#### 3. 特点
• 每个函数里都有 `this` 环境对象
• 函数的调用方式不同，`this` 指代的对象也不同
• **判断规则**：谁调用，`this` 就是谁
### vii. 回调函数
#### 1. 定义
• 如果函数A作为参数传递给函数B时，我们称函数A为回调函数
#### 2. 特点
• 回调函数本质还是函数，只不过把它当作参数使用
• 使用匿名函数作为回调函数比较常见

---
# 六. 事件流
## a. 事件流与两个阶段说明
### i. 事件流定义
• 事件流指的是事件完整执行过程中的流动路径
### ii. 事件流的两个阶段
1. **捕获阶段**（从外到内）
2. **冒泡阶段**（从内到外）
### iii. 执行顺序
• 捕获阶段：从父元素到子元素
• 冒泡阶段：从子元素到父元素
### iv. 实际应用
• 工作中主要使用事件冒泡模式
## b. 事件捕获
### i. 概念
• 从DOM的根元素开始执行对应的事件（从外到里）
### ii. 代码实现
```javascript
DOM.addEventListener(事件类型, 事件处理函数, 是否使用捕获机制)
```
• 第三个参数：
  • `true`：捕获阶段触发
  • `false`（默认）：冒泡阶段触发
> 注意：事件捕获在实际开发中较少使用
## c. 事件冒泡
• 默认的事件传播模式
• 从触发事件的元素开始，逐级向上传播到DOM树的最外层
## d. 阻止冒泡
### i. 必要性
• 默认的冒泡模式可能导致事件影响到父级元素
### ii. 实现方法
```javascript
事件对象.stopPropagation()
```
• 需要先获取事件对象(event)
• 此方法可以阻断事件流动传播，在捕获和冒泡阶段都有效
### iv. 阻止元素默认行为
• 语法：
```JavaScript
事件对象.preventDeefault()
```
## e. 解绑事件

### i. on事件方式解绑
```javascript
btn.onclick = function() {
  alert('点击事件');
}
// 解绑
btn.onclick = null;
```
### ii. addEventListener方式解绑
```javascript
function handleClick() {
  console.log('点击事件');
}

btn.addEventListener('click', handleClick);
// 解绑
btn.removeEventListener('click', handleClick);
```
> 注意：匿名函数无法被解绑
## f. 鼠标经过事件的区别

| 事件类型                  | 冒泡效果 | 推荐程度 |
| --------------------- | ---- | ---- |
| mouseover/mouseout    | 有冒泡  | 不推荐  |
| mouseenter/mouseleave | 无冒泡  | 推荐   |
|                       |      |      |

• 实际开发中推荐使用`mouseenter`和`mouseleave`，避免不必要的冒泡影响

---
# 七. 事件委托
## a. 基本概念
• **定义**：利用事件冒泡机制优化事件处理的技术
• **优点**：
  • 减少事件注册次数
  • 提高程序性能
  • 动态添加的子元素也能自动拥有事件处理
## b. 核心思想
• 将子元素的事件监听委托给父元素统一处理
## c. 实现原理
### i. 事件冒泡机制
• 当子元素触发事件（如点击）时，事件会向上冒泡到父元素
### ii. event.target属性
• 通过事件对象的`target`属性获取实际触发事件的子元素
• `event.currentTarget`指向绑定事件的元素（父元素）
### iii. 条件判断
• 根据`target`的标识（标签名、类名、ID等）执行特定操作
## d. 实现方式
### 基本实现代码
```javascript
parentElement.addEventListener('click', function(event) {
  // 检查实际点击的元素是否是目标元素
  if(event.target.tagName === 'LI') {
    // 执行操作
    console.log('点击了列表项:', event.target.textContent);
  }
});
```
### 更灵活的匹配方式
```javascript
parentElement.addEventListener('click', function(event) {
  // 匹配类名
  if(event.target.classList.contains('item')) {
    // 执行操作
  }
  
  // 匹配特定属性
  if(event.target.dataset.action === 'delete') {
    // 执行删除操作
  }
});
```
## e. 实际应用场景
1. **动态列表**：新增列表项自动拥有事件处理
2. **表格操作**：处理大量表格单元格的点击事件
3. **导航菜单**：处理具有相似行为的菜单项
4. **按钮组**：处理一组功能相似的按钮
## f. 注意事项
1. 确保目标元素确实是期望的元素（防止事件代理到不需要的元素）
2. 对于需要阻止冒泡的情况要谨慎处理
3. 某些事件（如focus/blur）不支持冒泡，不能使用事件委托
4. 性能敏感场景下避免在委托处理函数中做复杂判断
---
# 八. 其他事件
## a. 页面加载事件
### i. 基本概念
• 加载外部资源（图片、外联CSS和JS等）加载完毕时触发的事件
• 事件名：`load`
### ii. 监听页面所有资源加载完毕
```javascript
window.addEventListener('load', function() {
  // 所有资源加载完成后执行的代码
});
```
### iii. 监听单个资源加载
```javascript
const img = document.querySelector('img');
img.addEventListener('load', function() {
  // 图片加载完成后执行的代码
});
```
### iv. 监听DOM加载完毕（不等待样式表/图片等）
```javascript
document.addEventListener('DOMContentLoaded', function() {
  // DOM结构加载完成后执行的代码
});
```
## b. 页面滚动事件
### i. 基本概念
• 监听页面滚动行为
• 常用于实现动态效果（如懒加载、固定导航栏）
• 事件名：`scroll`
### ii. 监听页面滚动
```javascript
window.addEventListener('scroll', function() {
  // 页面滚动时执行的代码
});
```
### iii. 监听元素内部滚动
```javascript
const element = document.querySelector('.scrollable');
element.addEventListener('scroll', function() {
  // 元素内部滚动时执行的代码
});
```
### iv. 获取滚动位置

#### 常用属性
| 属性 | 描述 |
|------|------|
| `scrollLeft` | 获取/设置元素内容向左滚动的距离 |
| `scrollTop` | 获取/设置元素内容向上滚动的距离 |

#### 使用示例
```javascript
// 获取页面垂直滚动距离
const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;

// 获取元素内部滚动距离
const elementScrollTop = document.querySelector('.scrollable').scrollTop;

// 设置滚动位置
document.documentElement.scrollTop = 500;
```
#### 特点
1. 返回数字型值（不带单位）
2. 可读写属性
3. 常用于实现滚动到指定位置、返回顶部等功能
### v. 滚动到指定位置
#### scrollTo方法可以把内容滚动到指定位置
```JavaScript
元素.scrollTo(x,y)
```
## c. 页面尺寸事件
### i. 窗口尺寸变化事件
```javascript
window.addEventListener('resize', function() {
  // 窗口尺寸改变时执行的代码
  console.log('窗口宽度:', window.innerWidth);
  console.log('窗口高度:', window.innerHeight);
});
```
### ii. 获取元素尺寸
```javascript
// 获取元素可视区域尺寸（包含padding，不包含border）
const clientWidth = element.clientWidth;
const clientHeight = element.clientHeight;

// 获取元素完整尺寸（包含padding和border）
const offsetWidth = element.offsetWidth;
const offsetHeight = element.offsetHeight;

// 获取元素内容实际尺寸（包含padding，可能超出可视区域）
const scrollWidth = element.scrollWidth;
const scrollHeight = element.scrollHeight;
```
### iii. 应用场景
1. 响应式布局调整
2. 元素位置动态计算
3. 图片/内容懒加载
4. 无限滚动列表实现
## d. 元素尺寸与位置
### 1. 元素尺寸属性

|属性|描述|包含内容|
|---|---|---|
|`offsetWidth`|元素整体宽度|内容+padding+border+滚动条|
|`offsetHeight`|元素整体高度|内容+padding+border+滚动条|
|`clientWidth`|可视区域宽度|内容+padding|
|`clientHeight`|可视区域高度|内容+padding|

### 2. 元素位置属性
```javascript
// 获取相对于定位父元素的位置
const element = document.querySelector('.box');
console.log(`位置: ${element.offsetLeft}px, ${element.offsetTop}px`);

// 获取相对于视口的位置和尺寸
const rect = element.getBoundingClientRect();
console.log(rect); // 包含left, top, right, bottom, width, height等
```
### 3. 实际应用示例
```javascript
// 检测元素是否进入视口
function isElementInViewport(el) {
  const rect = el.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}
```
## 总结

| 属性                       | 作用                   | 说明                                   |
| ------------------------ | -------------------- | ------------------------------------ |
| scrollLeft和scrollTop     | 被卷去的头部和左侧            | 配合页面滚动来用，可读写                         |
| clientWidth和clientHeight | 获得元素宽度和高度            | 不包含border, margin，滚动条用于js获取元素大小，只读属性 |
| offsetWidth和offsetHeight | 获得元素宽度和高度            | 包含border、padding，滚动条等，只读             |
| offsetLeft和offsetTop     | 获取元素距离自己定位父级元素的左、上距离 | 获取元素位置的时候使用，只读属性                     |
|                          |                      |                                      |
