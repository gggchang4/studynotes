# Callout高亮提示框
obsidian内置Callout块，用> [!note]语法
> [!note] 提示
> 这里是一个普通提示框。

> [!warning] 警告
> 小心踩坑！

> [!example] 示例
> ```cpp
> int main() {
>   cout << "Hello World";
> }
> ```

常用类型：

- `[!note]` 提示
    
- `[!info]` 信息
    
- `[!warning]` 警告
    
- `[!example]` 示例
    
- `[!tip]` 小技巧

# 自定义CSS
1. 在 Vault 目录下创建 `.obsidian/snippets/` 文件夹
    
2. 新建 `custom.css`，写样式：

### 例1：图片居中
```CSS
.markdown-preview-view img {
  display: block;
  margin: auto;
}
```

### 例2：代码块圆角 + 背景
```CSS
pre code {
  border-radius: 8px;
  background: #1e1e1e;
  color: #dcdcdc;
  padding: 10px;
}
```
### 例3：高亮 Callout 更显眼

```CSS
.callout[data-callout="warning"] {
  border-left: 4px solid red;
  background: #ffeaea;
}
```

3. Obsidian → 设置 → 外观 → CSS 代码片段 → 启用 `custom.css`

# 可用插件
1. **Style Settings**
    
    - 给主题加自定义配色、字体、行距。
        
2. **Image Toolkit**
    
    - 图片缩放、旋转、拖动，增强显示效果。
        
3. **Minimal Theme** / **Obsidian Nord**
    
    - 更现代的主题，适合搭配 CSS 美化。
        
4. **Advanced Tables**
    
    - 让 Markdown 表格更好编辑。