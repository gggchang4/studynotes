---
date: "2025"
tags:
  - 前端
  - HTML
---
HTML文件的扩展名为.html

# HTML基础
1. 标签成对出现，中间包裹内容（<tag>text</tag>）
2. <>里面放标签名
3. .结束标签比开始标签多/
4. 不成对出现的标签是单标签，成对出现的标签是双标签
5. 典型的单标签`<br>`换行，`<hr>`水平线
6. 区分单标签和双标签的方法：需要包裹内容的一定是双标签
---
# HTML框架
1. HTML基本框架是网页模板
```html
<html>
	<head>
	<title>网页标题</title>
	</head>
	<body>
		网页主体
	</body>
<html>
```
	其中html：整个网页
	
	       head：网页头部，存放给浏览器看的代码，例如CSS
	
	         body：网页主体，存放给用户看的代码，如图片文字
	
	       title:网页标签
* 在VS CODE中按`!+Enter/Tab`自动生成网页骨架
---
# 标签的关系
1. 父子关系（嵌套关系）
2. 兄弟关系（平行关系）
---
# 注释
1. `<!--…-->`表示注释
2. 在VS CODE 中，通过`ctrl+/` 增加或删除注释
---
# 标题标签
1. 标签名`h1~h6`，表示六个级别的标题，从1到6级别递减（双标签）
2. 标签独占一行
3. 级别越高字号越大
4. `h1`标签移一般一个网页只用一次，用来放新闻标题或者网页logo

---
#  段落标签

1. 标签名：`<p>`（双标签）  
2. 段落标签独占一行，段落之前存在间隙  
3. 段落文字自动换行
---
#  换行与水平线标签

1. 换行与水平线标签都是单标签  
2. 换行：`<br>`  
3. 水平线：`<hr>`
--- 
# 文本格式化标签
1. 作用：为文本添加特殊格式，常见得文本格式：加粗，倾斜，下划线，删除线

| 标签名    | 标签名 | 效果  |
| ------ | --- | --- |
| strong | b   | 加粗  |
| em     | i   | 倾斜  |
| ins    | u   | 下划线 |
| del    | s   | 删除线 |

--- 
# 图像标签
1. 单标签，形式：`<img src="图片的URL">` 或 `<img src="content" alt="">`  
2. `src` 用于指定图像的位置和名称，是 `<img>` 的必须属性  
3. 一般以 `./` 开始  
4. 图像标签的属性  

| 属性     | 作用    | 说明              |
| ------ | ----- | --------------- |
| alt    | 替换文本  | 图片无法显示的时候显示文字   |
| title  | 提示文本  | 鼠标悬停在图片上的时候显示文字 |
| width  | 图片的宽度 | 值为数字，没有单位       |
| height | 图片的高度 | 值为数字，没有单位       |

---
# 路径

1. **相对路径**：从当前文件位置出发寻找目标文件  
   • `./` 表示进入某个文件夹  
   • `../` 表示进入上一级文件夹  
2. **绝对路径**：从盘符出发查找目标文件  
   • 例如：`<img src="c:\images\xxx.jpg">`  
   • Windows 系统默认是 `\`，其他系统是 `/`，统一写为 `/`  
   • 网址路径也是绝对路径的一种，例如：  
     `<img src="https://www.itheima.com/images/slidead/HOMEPAGE/20250121133546111.jpg">`
---
# 超链接

1. 点击跳转到其他页面  
2. `<a href="http://www.baidu.com">跳转到百度</a>` 双标签  
   • `href` 属性值是跳转地址，是超链接的必须属性  
3. 如果想保存原窗口另打开新的窗口，在 `href` 后面加 `target="_blank"`  
4. 开发初期不知道超链接的跳转地址，`href` 属性值写 `#`，表示空链接，不会跳转
5. <a href="http://www.google.com">跳转到谷歌</a>
---
# 音频标签
1. 标签：`<audio src="音频的URL"></audio>`  
<audio src="音频的URL"></audio>
2. 其他常用属性  

| 属性       | 作用       | 特殊说明                    |
| -------- | -------- | ----------------------- |
| src      | 音频 URL   | 支持格式：MP3、Ogg、Wav        |
| controls | 显示音频控制面板 |                         |
| loop     | 循环播放     |                         |
| autoplay | 自动播放     | 为了提升用户体验，浏览器一般会禁用自动播放功能 |

3. 在 HTML5 里，如果属性名和属性值一样，可以简写为一个单词，例如 `controls` -> `controls="controls"`
--- 
## 十三. 视频标签

1. 标签：`<video src="视频的URL"></video>`  
2. 其他常用属性  

| 属性       | 作用       | 特殊说明                            |
| -------- | -------- | ------------------------------- |
| src      | 视频 URL   | 支持格式：MP4、WebM、Ogg               |
| controls | 显示视频控制面板 |                                 |
| loop     | 循环播放     |                                 |
| autoplay | 自动播放     | 为了提升用户体验，浏览器一般会禁用自动播放功能         |
| muted    | 静音播放     | 在浏览器中，想要 autoplay 必须要有 muted 属性 |

---
# 列表、表格、表单

### 1. 列表

布局排列整齐的区域  
• **无序列表**标签：`<ul>` 嵌套 `<li>`  
  ```html
  <ul>
    <li>第一项</li>
    <li>第二项</li>
    <li>第三项</li>
  </ul>
  ```

• **有序列表**标签：`<ol>` 嵌套 `<li>`  
  ```html
  <ol>
    <li>第一项</li>
    <li>第二项</li>
    <li>第三项</li>
  </ol>
  ```
• **定义列表**标签：`<dl>` 嵌套 `<dt>` 和 `<dd>`  
  ```html
  <dl>
    <dt>列表标题</dt>
    <dd>列表描述/详情</dd>
  </dl>
  ```

### 2. 表格

标签：`<table>` 嵌套 `<tr>`，`<tr>` 嵌套 `<td>` 或 `<th>`  
```html
<table>
  <tr>
    <th>表头单元格</th>
    <td>内容单元格</td>
  </tr>
</table>
```
<table>
  <tr>
    <th>表头单元格</th>
    <td>内容单元格</td>
  </tr>
</table>

• **表格结构标签**：`<thead>`、`<tbody>`、`<tfoot>`  
• **合并单元格**：  
  1. 明确合并目标  
  2. 保留最左最上的单元格，添加属性：  
     ◦ 跨行合并：`rowspan`  
     ◦ 跨列合并：`colspan`  
  3. 删除其他单元格  

### 3. 表单

作用：收集用户信息（登录页面、注册页面、搜索页面）  
• **`<input>` 标签**：  
  ```html
  <input type="text" placeholder="提示信息">
  ```
  
|type 属性值|说明|
|---|---|
|text|文本框，用于输入单行文本|
|password|密码框（输入内容显示为点）|
|radio|单选框|
|checkbox|多选框|
|file|上传文件
• **占位文本**
```html
<input type="…" placeholder="提示信息">
```
<input type="…" placeholder="提示信息">

• **单选框**： 
  ```html
  <input type="radio" name="group" checked>
  ```
<input type="radio" name="group" checked>

|属性名|作用|特殊说明|
|---|---|---|
|name|控件名称|控件分组，同组只能选中一个|
|checked|默认选中|属性名和属性值相同，可简写

• **上传文件**：  
  ```html
  <input type="file" multiple>
  ```
  <input type="file" multiple>
  - 默认情况下，文件上传表单空间只能上传一个文件，添加multiple属性可以实现文件多选功能
---
# 下拉菜单

1. **标签**：`<select>` 嵌套 `<option>`  
   • `<select>` 是下拉菜单整体  
   • `<option>` 是下拉菜单的每一项  
   ```html
   <select>
     <option>选项1</option>
     <option>选项2</option>
     <option>选项3</option>
   </select>
   ```
   <select>
     <option>选项1</option>
     <option>选项2</option>
     <option>选项3</option>
   </select>

2. **默认选中某一项**：在 `<option>` 中添加 `selected` 属性  
   ```html
   <select>
     <option>选项1</option>
     <option selected>默认选中项</option>
     <option>选项3</option>
   </select>
   ```

---
# 文本域

1. **作用**：多行输入文本的表单控件  
2. **标签**：`<textarea>`（双标签）  
   ```html
   <textarea>提示文字</textarea>
   ```
<textarea>提示文字</textarea>

4. **右下角拖拽功能**：默认启用，一般禁用掉  
   ```html
   <textarea style="resize: none;">提示文字</textarea>
   ```
---
# label 标签
1. **作用**：网页中，某个标签的说明文本  
2. **经验**：用 `label` 标签绑定文字和表单控件的关系，增大表单控件的点击范围  
##### 写法一：
• **label 标签只包裹内容，不包裹表单控件**  
• **设置 `label` 标签的 `for` 属性值和表单控件的 `id` 属性值相同**  
  ```html
  <input type="radio" id="man">
  <label for="man">男</label>
  ```
##### 写法二：
• **使用 `label` 标签包裹文字和表单控件，不需要属性**  
  ```html
  <label>
    <input type="radio">男
  </label>
  ```
---
# 按钮

1. **标签**：`<button>`  
   ```html
   <button type="">按钮</button>
   ```
<button type="">按钮</button>

2. **常用属性值**：  

| type 属性值 | 说明                             |
| -------- | ------------------------------ |
| submit   | 提交按钮，点击后可以提交数据到后台（默认功能）        |
| reset    | 重置按钮，点击后将表单控件恢复默认值             |
| button   | 普通按钮，默认没有功能，一般配合 JavaScript 使用 |

3. **注意**：  
   • `reset` 等按钮要发挥功能，需要由 `<form>` 表单区域标签统一管理按钮和文本域  
---
# 无语义的布局标签
**作用**：布局网页（划分网页区域，摆放内容）
1. **`<div>` 标签**：独占一行（大盒子）  
   ```html
   <div>div标签，独占一行</div>
   ```
2. **`<span>` 标签**：不换行  
   ```html
   <span>span标签，不换行</span>
   ```
---
# 字符实体
**作用**：在网页中显示预留字符

| 显示结果 | 描述  | 实体名称     |
| ---- | --- | -------- |
|      | 空格  | `&nbsp;` |
| `<`  | 小于号 | `&lt;`   |
| `>`  | 大于号 | `&gt;`   |

---
html语言只是基础的前端语言只能搭建网站的架构，网站的样式通过[[CSS]]实现，与用户的交互由[[Java Script]]实现


---

DONE

---