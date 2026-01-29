### 今日做的事情






#### astream_events 核心生命周期
- on_chain_start: 整个图或整个内部链开始执行
- on_chain_stream: 当 Runnable（如 LangGraph）产生流式输出时触发
- on_chain_end: 整个图或某个内部链执行完毕

#### astream_events 节点与工具时间
- on_chat_model_start: 聊天模型（LLM）收到输入并准备生成。
- on_chat_model_stream: 模型正在流式输出 Token。如果你想实现打字机效果，通常会监听这个事件。
- on_chat_model_end: 模型生成完毕。
- on_tool_start / on_tool_end: 某个自定义工具开始执行或结束。
