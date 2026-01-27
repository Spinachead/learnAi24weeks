### add_conditional_edges的几种用法

#### 官方预置的工具路由
```
from langgraph.prebuilt import tools_condition

# 如果 llm_call 节点决定调工具，tools_condition 返回 "tools"，跳到 tools 节点
# 如果 llm_call 节点决定回答，tools_condition 返回 "__end__"，流程结束
workflow.add_conditional_edges(
    "llm_call",
    tools_condition
)
```
#### 自定义逻辑路由（根据内容分类）
```
def router(state: GraphChatState):
    if "投诉" in state["query"]:
        return "human_service"
    else:
        return "ai_reply"

workflow.add_conditional_edges(
    "classifier_node",
    router,
    {
        "human_service": "support_node", # 映射返回值到具体的节点名
        "ai_reply": "llm_node"
    }
)
```
#### 基于计数的循环控制（防止无限死循环）
```
def should_continue(state: GraphChatState):
    if state["retry_count"] < 3:
        return "try_again"
    return "fail_end"

workflow.add_conditional_edges(
    "worker_node",
    should_continue,
    {
        "try_again": "worker_node", # 回到自己，形成循环
        "fail_end": END             # 直接结束
    }
)
```
