### 今天做的事情
1. 查看langsimth的文档和教程  知道了怎么自定义trade
2. 想要实现用户点评这个功能； 问了grok和千问两种实现方法 打算采用grok提供的方案； 先把用户的评价存储在本地然后在批量进行处理
3. 记录对话， 学习使用traceable;  尝试获取trace_id




### 踩的坑
我想获取trace_id记录到message表中方便用户后续对大模型的回答评分；但是在获取trace_id这一步遇到坑了； 我想用的 run_tree = get_current_run_tree() 获取到trace_id; 但是获取的是None; 后面我又在llm.astream中获取get_current_run_tree()还是为None;
我的想法是llm.astream中langsmith会自动跟踪此时 在llm.astream中肯定是能获取到trace_id的结果还是为None; 后面经过仔细排查和阅读文档才发现：

在 LangChain 中，虽然 llm.astream 会自动触发追踪（如果环境变量已配置），但这种自动追踪仅限于 llm 内部。你的 async for 循环和外层的 knowledge_base_chat_iterator 函数并没有被定义为一个“Run”，因此 LangSmith 的上下文变量中没有当前运行树的信息。

因为我的一个生成器有多个chat_openAI的调用这样就导致会产生多个互不关联的trace; 后面的解决方法是在生成器的顶部用@traceable装饰器 这样只生成一个trace就能获取到trace_id了 而且这样一个生成器也不会产生多个互不关联的trace了
