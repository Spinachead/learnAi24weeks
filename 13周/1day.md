### 今日做的事情
1. 看了langgraph的官方文档 对怎样实现agent graph有了理解
2. 更改了graph_chat接口 完全实现用graphp的方式实现
3. 对astream_events有了具体的认识； 他就是一个监控 可以详细的看到每个节点做了什么；


### 遇到的坑

#### 在astream_event中判断我用event["event"] == on_chat_model_strame 来流式获取content 以实现打字机的效果 但是发现没有on_chat_model_stream
原因实际因为每次节点内部调用 llm.invoke时候没有显式传递confid对象， 内部的llm调用就无法感知它正处于一个astream_events的上下文中。 
这就导致了内部产生的 on_chat_model_stream 事件被“截断”了，无法向上传递
