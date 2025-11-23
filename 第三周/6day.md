## transformer学习
### transformer 微调
https://huggingface.co/learn/llm-course/zh-CN/chapter3/3
教程没看太懂怎么微调的

## langChain
中文官网：https://www.langchain.com.cn/

### langChain提供的组件
- LLMs 使用的大模型语言目前LangChain基本都能对接,厂家在开发的过程中也会优先去兼容LangChain
- langchain支持的提示词模板
- mermory 记录聊条历史做上下文管理
- chains 处理业务流
- document laders 加载外部数据 对数据进行向量处理
- vector stores 向量数据库 存放处理完的向量
- agent 能通过外部访问的接口

### langChain的构成
- 开发  使用langchain的开源构建块 组件和第三方继承来构建应用程序
- 产品化 使用langSmith来检查和评估
- 部署 使用langGraph Cloud将LangGraph应用程序装变为生产就绪的api和助手


### langChain的安装和使用
- pip install langchain
- pip install langchain-openai

### 消息的类型
- HumanMessage  代表用户发送的消息
- AIMessage 代表模型发送的消息
- SystemMessage 代表系统消息 告诉模型如何行为，比如告诉模型 你是xx方面的专家，并非每个模型都支持这一点
- FunctionMessage 代表函数调用的结果 除了role和content 此消息还有一个name参数

###
