#### 知识库助手怎样记住历史对话

#### ChatPromptTemplate.from_messages中传入的历史对话记录该怎样传入
1. 使用sqlLite记录对话记录 async with aiosqlite.connect("checkpoints.sqlite") as conn: checkpointer = AsyncSqliteSaver(conn)
2. 大模型运行的时候使用该checkpoint
3. 从数据库中读取历史消息 state_snapshot = await checkpointer.aget(config) history_messages = state_snapshot.get('channel_values', {}).get('messages',  []) if state_snapshot else []
4. 新消息追加的历史后面   all_messages = history_messages + [HumanMessage(content=query)]


### 怎样让大模型使用历史对话
1. 提示词模板中要有该变量如{history}
2. 要把历史消息构建为使用与模板的历史记录字符串



### 提示词模板的用法
1. promptTemplate
2. ChatPromptTemplate
3. FewShotPromptTemplate


#### fewshotPromptTemplate的用法
1. 定义示例
2. 创建提示词模板
3. 创建fewshot提示词模板

#### messagesPlaceholder用法

#### RunnableWithMessageHistory的用法

### 生产级会话记忆管理方案
1. graphiti 时序知识图谱上下文管理
2. Mem0 AI大模型记忆集中管理框架
