
# 个人 Profile 网站规划方案

## 一、项目定位

我准备做的不是传统技术博客，也不是普通简历页，而是一个具有前沿审美、交互设计能力和前端工程能力展示价值的个人 Profile 网站。

这个网站更适合定位为：

> 个人数字展厅 / Interactive Portfolio / Frontend Playground

核心目标是让访问者在打开网站后，能够快速感受到我的：

- 视觉设计审美
- 前端交互能力
- 动效实现能力
- 工程化能力
- AI / Agent / 前端方向的个人品牌

网站不应该做成普通博客模板，而应该更接近一个小型产品官网、创意作品集或交互实验场。

---

## 二、网站核心方向

网站应该重点展示：

```txt
视觉设计能力
页面交互动效
前端工程能力
个人技术品牌
项目作品案例
交互实验 Demo
AI / Agent 探索方向
````

推荐整体气质：

```txt
科技感 + 高级排版 + 交互实验 + 个人品牌
```

中文定位可以写成：

> 一个展示前端工程能力、AI 探索方向与交互审美的个人数字空间。

英文定位可以写成：

> A personal digital space for frontend engineering, AI exploration, and interaction design.

---

## 三、推荐技术栈

### 1. 首选技术栈

```txt
框架：Next.js
语言：TypeScript
UI：React
样式：Tailwind CSS
组件基础：shadcn/ui
动效：Motion for React + GSAP
3D：Three.js / React Three Fiber
内容管理：MDX / JSON / 本地配置文件
部署：Vercel
数据分析：Vercel Analytics
```

### 2. 技术栈说明

|模块|推荐技术|作用|
|---|---|---|
|前端框架|Next.js|页面路由、SEO、静态生成、部署友好|
|开发语言|TypeScript|提升工程质量，展示专业度|
|UI 框架|React|组件化构建页面|
|CSS 方案|Tailwind CSS|快速构建设计系统和响应式布局|
|组件基础|shadcn/ui|提供高质量、可定制的组件基础|
|基础动效|Motion for React|页面入场、组件动画、悬停动画、滚动动画|
|高级动画|GSAP|复杂滚动叙事、时间轴动画、SVG 动效|
|平滑滚动|Lenis|提升页面滚动体验|
|3D/WebGL|Three.js + React Three Fiber|实现 3D Hero、交互模型、空间感页面|
|内容管理|MDX / JSON|管理个人介绍、项目、经历、作品内容|
|部署平台|Vercel|与 Next.js 集成度高，适合个人站部署|
|数据分析|Vercel Analytics|查看访问量、来源、设备信息等|

---

## 四、为什么推荐 Next.js + React

这个网站的目标不是写文章，而是展示个人审美和前端交互能力，因此技术栈的重点不是后台、数据库和 CMS，而是：

```txt
视觉表现力
页面切换动效
滚动叙事
微交互
3D / WebGL
响应式设计
性能优化
代码工程感
```

Next.js + React 的优势在于：

- 适合做现代化个人作品集网站
    
- 组件生态丰富
    
- 动效和 3D 生态成熟
    
- 与 Vercel 部署高度集成
    
- 适合做静态站、动态站和后期扩展
    
- 更容易体现工程能力和前沿前端能力
    

---

## 五、备选技术栈：Vue 方案

如果更想使用 Vue 技术栈，也可以选择：

```txt
Nuxt + Vue + TypeScript + Tailwind CSS + Motion for Vue + GSAP + TresJS
```

对应技术说明：

|模块|技术|
|---|---|
|框架|Nuxt|
|UI 框架|Vue|
|语言|TypeScript|
|样式|Tailwind CSS|
|动效|Motion for Vue / GSAP|
|3D|TresJS / Three.js|
|部署|Vercel / Netlify / Cloudflare Pages|

不过如果目标是打造更国际化、更偏创意前端、更有前沿审美的个人 Profile 网站，首选仍然是：

```txt
Next.js + React + TypeScript + Tailwind CSS + Motion + GSAP + Three.js
```

---

## 六、是否需要后端和数据库

第一版不建议加入后端和数据库。

初期建议保持轻量：

```txt
个人信息：config/profile.ts
项目数据：data/projects.ts
技术栈数据：data/stack.ts
社交链接：data/social.ts
作品内容：MDX
图片资源：public/images
简历文件：public/resume.pdf
联系方式：静态链接
```

只有后期需要以下功能时，再考虑后端：

```txt
留言板
订阅功能
后台编辑
访客统计
动态作品管理
评论系统
CMS 内容管理
```

第一版最重要的不是功能多，而是视觉和交互质量高。

---

## 七、推荐页面结构

```txt
/
├── Home 首页
│   ├── 高质感 Hero 区域
│   ├── 个人定位
│   ├── 动态交互背景
│   └── 核心标签：Frontend / AI / Design / Interaction
│
├── /works 作品集
│   ├── 项目卡片
│   ├── 网站项目
│   ├── AI Agent 项目
│   ├── 前端实验
│   └── 每个项目的 Case Study
│
├── /lab 交互实验室
│   ├── 动效实验
│   ├── 3D 实验
│   ├── WebGL Demo
│   ├── Cursor / Agent 工作流展示
│   └── UI Prototype
│
├── /about 关于我
│   ├── 个人介绍
│   ├── 技术栈
│   ├── 学习方向
│   ├── 设计偏好
│   └── 未来方向
│
├── /stack 技术栈
│   ├── 前端技术
│   ├── 后端基础
│   ├── AI 工具链
│   └── 开发工具
│
└── /contact 联系方式
    ├── GitHub
    ├── Email
    ├── X / Twitter
    ├── LinkedIn
    └── Resume
```

其中最重要的两个页面是：

```txt
/works
/lab
```

`/works` 用于展示做过的项目。  
`/lab` 用于展示前端交互实验、动效能力和 WebGL / 3D 技术能力。

---

## 八、页面内容规划

### 1. 首页 Home

首页应该承担第一印象的作用，不能只是普通头像和文字介绍。

可以包含：

```txt
动态 Hero
高级 Typography
个人定位
鼠标交互光效
3D 背景或粒子背景
精选作品入口
交互实验入口
联系方式入口
```

首页目标：

> 让访问者在 5 秒内记住这个网站。

---

### 2. 作品集 Works

作品集页面不要只放项目截图，建议每个项目做成 Case Study。

每个项目可以包含：

```txt
项目名称
项目背景
我的角色
技术栈
视觉设计
交互亮点
工程实现
最终效果
项目链接
GitHub 链接
```

适合展示的项目类型：

```txt
个人 Profile 网站
品牌展示网站
电商网站
AI Agent 产品
前端组件库
交互实验 Demo
课程设计项目
开源项目
```

---

### 3. 交互实验室 Lab

这是你区别于普通个人网站的关键页面。

可以展示：

```txt
3D Card Tilt
Mouse Trail
Shader Background
Scroll Animation
WebGL Particle
Gesture Interaction
SVG Animation
Magnetic Button
Page Transition
AI Agent UI Prototype
```

这个页面的作用是证明：

> 我不仅会写页面，还能做有审美、有交互、有技术含量的前端体验。

---

### 4. 关于我 About

关于页面不应该写成普通简历。

可以写成更有个人品牌感的结构：

```txt
我是谁
我关注什么方向
我正在学习什么
我喜欢什么设计风格
我目前的技术栈
我未来想做什么
```

可以突出：

```txt
计算机专业背景
前端工程能力
AI / Agent 学习方向
设计审美兴趣
个人项目实践
研究生 / 博士规划
```

---

### 5. 技术栈 Stack

可以用视觉化方式展示技术栈，而不是普通列表。

分类建议：

```txt
Frontend
Backend
AI / Agent
Design
Tools
Deployment
```

示例：

```txt
Frontend:
React / Next.js / Vue / TypeScript / Tailwind CSS

Backend:
Java / Spring Boot / MySQL / PostgreSQL

AI:
Python / PyTorch / LLM / Agent / OpenAI API

Design:
Figma / Typography / Interaction Design

Tools:
Git / GitHub / VS Code / Cursor / Docker

Deployment:
Vercel / Alibaba Cloud / Nginx / Linux
```

---

## 九、推荐视觉风格

### 方向一：高级科技感 / AI Agent 风格

适合展示 AI、Agent、前端工程方向。

关键词：

```txt
Dark Mode
玻璃拟态
细线框
网格背景
渐变光晕
低饱和紫 / 蓝 / 银
动态噪声
3D 粒子
代码感排版
```

适合展示：

```txt
AI Agent 项目
前端工程能力
个人技术品牌
GitHub 项目
未来感交互
```

---

### 方向二：设计师作品集风格

更偏审美、视觉和排版。

关键词：

```txt
大字号 Typography
留白
横向滚动
不对称网格
图片主导
细腻 Hover
页面过渡
Editorial Design
```

适合展示：

```txt
个人审美
网页设计能力
交互原型
品牌设计
视觉探索
```

---

### 方向三：实验型前端 Playground

更偏技术炫技和创意编码。

关键词：

```txt
WebGL
Canvas
Shader
3D Object
Scroll Interaction
Micro Interaction
Gesture
Cursor Trail
Physics Animation
```

适合展示：

```txt
Three.js 能力
动效能力
创意编码
前端底层交互
复杂动画控制
```

---

## 十、推荐最终视觉方向

综合考虑个人定位，推荐采用：

```txt
高级黑白排版
局部荧光色点缀
首屏加入 3D / WebGL / 粒子交互
作品页做 Case Study
单独做 Lab 页面展示交互实验
整体保持克制，不要过度炫技
```

推荐组合：

```txt
整体气质：Rauno Freiberg + Obys
交互亮点：Bruno Simon + Shoya Kajita
作品展示：Eliza Doltu + mw24
技术实验：Lusion + SMSY Gen-02
```

---

## 十一、推荐项目目录结构

```txt
profile-site/
├── app/
│   ├── page.tsx
│   ├── works/
│   │   └── page.tsx
│   ├── lab/
│   │   └── page.tsx
│   ├── about/
│   │   └── page.tsx
│   ├── stack/
│   │   └── page.tsx
│   └── contact/
│       └── page.tsx
│
├── components/
│   ├── layout/
│   │   ├── Navbar.tsx
│   │   ├── Footer.tsx
│   │   └── PageTransition.tsx
│   │
│   ├── sections/
│   │   ├── HeroSection.tsx
│   │   ├── WorksSection.tsx
│   │   ├── LabSection.tsx
│   │   └── AboutSection.tsx
│   │
│   ├── ui/
│   │   └── shadcn components
│   │
│   ├── motion/
│   │   ├── FadeIn.tsx
│   │   ├── RevealText.tsx
│   │   └── MagneticButton.tsx
│   │
│   └── three/
│       ├── HeroScene.tsx
│       └── FloatingObject.tsx
│
├── data/
│   ├── profile.ts
│   ├── projects.ts
│   ├── stack.ts
│   └── social.ts
│
├── content/
│   └── works/
│       ├── complyx.mdx
│       ├── ecommerce-site.mdx
│       └── ai-agent-demo.mdx
│
├── public/
│   ├── images/
│   ├── models/
│   └── resume.pdf
│
├── styles/
│   └── globals.css
│
├── lib/
│   ├── utils.ts
│   └── constants.ts
│
└── package.json
```

---

## 十二、交互能力展示方式

### 1. 首屏动态 Hero

可以实现：

```txt
鼠标移动产生光影变化
文字逐行 Reveal
背景动态粒子
3D 几何体旋转
代码片段浮动
页面进入动效
```

---

### 2. 作品卡片交互

可以实现：

```txt
Hover 时图片位移
卡片 3D 倾斜
磁吸按钮
流动渐变边框
图片遮罩展开
项目标签动态显示
```

---

### 3. 滚动叙事

可以实现：

```txt
文字随滚动逐渐出现
项目时间线跟随滚动展开
背景颜色随章节切换
图片与文字错位滚动
横向滚动作品集
章节切换动画
```

---

### 4. 交互实验室

可以展示：

```txt
Three.js 小 Demo
SVG 动效
Cursor Trail
3D Card Tilt
Shader Background
WebGL Particle
Gesture Interaction
AI Agent UI Prototype
```

---

### 5. 响应式细节

移动端也要保持设计质量，不能只是简单缩小。

需要注意：

```txt
移动端布局重新设计
动效适当简化
触摸交互替代鼠标交互
首屏加载速度优化
字体和间距适配
```

---

## 十三、最小可行版本 MVP

第一版不要追求功能太多，建议先完成：

```txt
1. 首页 Hero
2. 个人介绍
3. 技术栈展示
4. 3 个项目作品卡片
5. 1 个交互实验 Demo
6. 联系方式
7. 响应式适配
8. Vercel 部署
```

第一版目标：

> 打开网站前 5 秒，就能表达这个人懂审美、懂交互、懂工程化。

---

## 十四、参考网站

### 1. 个人 Profile / 作品集类网站

|网站|类型|参考重点|
|---|---|---|
|[Bruno Simon](https://bruno-simon.com/)|3D 游戏化个人作品集|3D 场景、游戏化交互、个人网站记忆点|
|[Rauno Freiberg Portfolio 2025](https://www.awwwards.com/sites/portfolio-2025)|极简高级交互作品集|高级排版、黑白视觉、Hero Reveal、横向滚动、Minimap|
|[Shoya Kajita Portfolio](https://www.awwwards.com/sites/shoya-kajita-portfolio)|手势交互型个人作品集|MediaPipe 手势交互、前沿交互技术、传统网站可用性结合|
|[Eliza Doltu Portfolio 25'](https://www.awwwards.com/sites/portfolio-25)|创意前端 / 设计师作品集|个人介绍、Featured Work、Contact、Parallax、Typography|
|[mw24 / Marchant Web](https://www.awwwards.com/sites/mw24)|独立交互开发者作品集|Vue + Nuxt、WebGPU / WebGL、滚动视差、视频案例展示|
|[Kenta Toshikura Portfolio](https://www.awwwards.com/sites/kenta-toshikura-portfolio)|前端设计师作品集|黑色视觉、WebGL、GSAP、Three.js、Nuxt.js、粒子、转场|
|[SMSY / Gen-02 Portfolio](https://www.awwwards.com/sites/gen-02-smsy-portfolio)|WebGPU / WebGL 沉浸式作品集|3D 世界、沉浸式体验、个人故事表达|

---

### 2. 创意工作室参考网站

这些不是个人站，但视觉、动效和项目陈列方式很值得参考。

|网站|类型|参考重点|
|---|---|---|
|[Lusion](https://lusion.co/)|3D / 交互视觉工作室|3D visual storytelling、沉浸式网页、交互体验、高端科技视觉|
|[Active Theory](https://activetheory.net/)|创意技术工作室|技术感、叙事感、高端商业项目展示|
|[ToyFight](https://www.awwwards.com/sites/toyfight-1)|玩味设计工作室|趣味表达、强视觉、品牌人格、3D 与动画|
|[Obys](https://www.awwwards.com/sites/obys)|概念驱动设计工作室|黑白黄配色、强排版、横向布局、实验性动效|
|[Garden Eight](https://www.awwwards.com/sites/garden-eight)|数字设计工作室|日本 / 国际化设计气质、3D、GSAP、Three.js、GLSL、Nuxt.js|

---

## 十五、参考网站分类整理

### 1. 首屏 Hero 参考

重点看：

```txt
Bruno Simon
Rauno Freiberg
Shoya Kajita
SMSY Gen-02
```

参考方向：

```txt
3D 场景
强字体排版
交互式光效
粒子背景
鼠标驱动视觉变化
页面进入动效
```

---

### 2. 作品集页面参考

重点看：

```txt
Rauno Freiberg
Eliza Doltu
mw24
Kenta Toshikura
Obys
```

参考方向：

```txt
Featured Work 展示
Case Study 页面
横向滚动
项目卡片动效
作品图像排版
文字和图片节奏
```

---

### 3. 交互实验室参考

重点看：

```txt
Bruno Simon
Shoya Kajita
SMSY Gen-02
Lusion
Active Theory
```

参考方向：

```txt
WebGL
Three.js
手势交互
Shader
鼠标交互
沉浸式体验
```

---

### 4. 视觉风格参考

重点看：

```txt
Rauno Freiberg：极简、黑白、高级排版
Obys：强排版、实验性、概念感
ToyFight：趣味、品牌人格、强记忆点
Lusion：科技、3D、沉浸式
Garden Eight：精致、克制、国际化
```

---

## 十六、最优先参考的 5 个网站

优先看这 5 个：

```txt
1. Bruno Simon
2. Rauno Freiberg Portfolio 2025
3. Shoya Kajita Portfolio
4. mw24 / Marchant Web
5. Obys
```

这 5 个基本覆盖了：

```txt
前沿审美
个人品牌
交互技术
作品展示
工程表达
```

---

## 十七、最终建议

这个个人 Profile 网站不应该做成：

```txt
普通简历页
普通技术博客
套模板作品集
静态个人介绍页
```

而应该做成：

```txt
个人数字展厅
交互式作品集
前端实验展示场
AI / Agent / Frontend 个人品牌主页
```

最终推荐方案：

```txt
技术栈：
Next.js + React + TypeScript + Tailwind CSS + shadcn/ui + Motion + GSAP + Three.js

页面结构：
Home / Works / Lab / About / Stack / Contact

内容管理：
MDX + 本地 data 配置文件

部署：
Vercel

视觉方向：
高级黑白排版 + 局部荧光色点缀 + 3D / WebGL / 粒子交互

核心亮点：
高级视觉设计、滚动叙事、页面动效、3D 交互、作品案例展示、个人品牌表达
```

第一版只需要做到：

```txt
精致
克制
有记忆点
有交互亮点
有工程质量
```

不要一开始就堆太多功能。  
核心是让别人打开网站后能够感受到：

> 这个人不是只会写页面，而是懂审美、懂交互、懂工程化的前端开发者。



# Personal Insights
## intro
一个轮盘可以选择网站的不同风格
	轮盘写着网站的不同风格（不同风格间内容大体一致，但展示方式完全不同，交互风格完全新的体验）
通过鼠标hover轮盘的不同选项，网站丝滑预览当前风格

## 内容
