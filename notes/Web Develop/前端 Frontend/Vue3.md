## Vue简述
Vue是一个用于构建用户界面的渐进式框架

**Vue两种使用方式**
- Vue核心包开发
	- 场景：局部模块开发
- Vue核心包&Vue组件 工程化开发
	- 场景：整站开发

**Vue核心特质**：响应式

---
## Vue实例创建
**核心步骤：**
	1.准备容器
	2.引入核心包（开发时使用开发版本，部署时使用生产版本）
		一旦引入Vue核心包，在全局环境就有了Vue构造函数
	3.创建Vue实例：new Vue()
	4.指定配置项
```HTML
//准备容器
<div id="app">
//用于渲染的代码逻辑
</div>

//引入核心包
<script src="http://cdn.jsdelivr.net/npm/vue@2.7.14/dist/vue.js"><script>
<script>
	const app = new Vue({
		//通过el选择配置器，指定Vue管理的是哪个盒子
		el:'#app',
		//通过data提供渲染数据
		data:{}
	})
</script>
```

---
## Vue语法
### **插值表达式**

插值表达式是Vue的模板语法
作用：利用表达式插值，渲染到页面上
语法：{{ 表达式 }}
注意：
	（1）使用的数据必须存在
	（2）插入的是表达式不是语句
	（3）不能再标签属性中使用
	（4）插值表达式不具备解析标签的能力
```Vue
<div id="app">
	{{msg}}
</div>
...
<script>
	...
	data:{
		msg:Hello World!
	}
</script>
```

## Vue指令
Vue中的指令：带有v- 前缀的特殊标签属性

### v-html
作用：设置元素的innerHTML
语法：v-html = "表达式"
### v-show

### v-if

### v-else

### v-else-if

### v-on

### v-bind

### v-for
### v-model
### v-slot


