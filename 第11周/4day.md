### 今日做的事情
1. 看了短期记忆和长期记忆的相关文档 知道了如何利用长期记忆的方案 如：用ostgresql存储用户长期记忆 用户提问时提取摘要注入到prompt中
2. 




### 阅读lamgchain有关memory的相关文档

#### memory type
<img width="694" height="163" alt="image" src="https://github.com/user-attachments/assets/d199e9fb-1df4-47c8-9565-4e189e8fc080" />




#### 我的rag知识库助手目前使用长期记忆的工作流程

```
用户请求 → 获取 user_id
    ↓
加载用户长期记忆（user_profile）
    ↓
注入到 generate_queries（影响知识库选择和查询改写）
    ↓
执行检索
    ↓
注入到最终 Prompt（影响回答风格）
    ↓
生成回
