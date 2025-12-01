### 知识库助手调优
1. 使用langgraph实现短期记忆功能
2. 如果用数据库实现长期记忆


### 短期记忆长时间对话超过LLM的上下文窗口的处理方法
- 修剪消息 在调用LLM之前删除首尾N条消息
- 永久删除LangGraph状态下的消息
- 摘要消息  总结历史中早期的消息并用摘要替换
- 管理检查点以存储和检索历史消息
- 自定义策略 例如消息过滤等


工具调用 结构化输出和短期记忆是定制大模型几个必备的条件

### langchain教程
#### 备选模型机制
```
llm = ChatOpenAI(model="gpt-4o-mini-xxx", max_retries=0)
anther_llm = ChatAnthropic(model="claude-3-7-sonnet-20250219")
为llm添加备选模型
llm_with_fallback = llm.with_fallbacks([ahther_llm])
```

### LCEL表达式运用
1. Runnable对象
2. RunnableSequence对象 （实质上就是一个顺序执行的Runnable的集合）
3. RunnableLambda 封装函数为Runnable对象
4. RunnableParallel 并行执行Runnable对象
5. RunnablePassthrough() 直接传递原始输入
6. RunnableConfig参数管理
7. configurable_fields 可以在运行过程中动态的调整参数
```
隐式写法（常用）
chain1 = prompt | model | parser
显式写法
chain2 = RunnableSequence(first=prompt,middle=[model], last=parser)
```
```
RunnablePassthrough的经典用法
runnable = {
 "llm1": fake_llm,
 "llm2": fake_llm,
} | RunnablePassthrough.assign(
 total_chars=lambda inputs: len(input["llm1"] + inputs["llm2"])
)
```
### 要做的事情
1. api/chat-process方法采用stream的方式流式输出
2. 
