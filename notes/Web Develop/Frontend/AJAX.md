# 什么是AJAX
Asynchronous JavaScript and XML
AJAX 是 “Asynchronous JavaScript and XML”（异步 JavaScript 和 XML）的缩写，是一种创建交互式 Web 应用的网页开发技术，核心是通过异步通信与服务器交换数据并局部更新页面，无需刷新整个页面，显著提升用户体验与交互效率。它并非单一技术，而是整合了 JavaScript、XMLHttpRequest（XHR）/Fetch API、HTML/CSS、DOM 等现有技术的编程范式

# axios
## axios使用
语法：
1. 引入axios.js：https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js
2. 使用axios函数
	1. 传入配置对象
	2. 再用.then函数接受结果，并做后续处理
```JavaScript
axios({
	url:'targetURL'
}).then((result)=>{
	//返回服务器做后续的处理
})
```
## 查询参数
### URL查询参数
定义：浏览器给服务器额外信息，让服务器返回想要的数据
语法：http://xxx.com/xxx/xxx?参数名1=值1&参数名2=值2...
### axios查询参数
语法：使用axios提供的params选项
注意：axios在运行时会把参数名和参数值，拼接到url后
```javascript
axios({
	URL:XXXXX
	params:{
		参数名：值
	}
}).then()
```
