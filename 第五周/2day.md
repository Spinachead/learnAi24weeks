### langchain中初始化模型的方法有一下几种

#### 使用特定提供商的模型类 如
1. ChatOpenAI()
2. ChatAnthropic()

#### 使用init_chat_model函数（统一接口）
`` model = init_chat_model("gpt-4", model_provider="openai") ``

#### 社区继承模型
```
from langchain_community.chat_models import ChatOllama
model = ChatOllama(model="llama2")
# Hugging Face
from langchain_community.chat_models import ChatHuggingFace
model = ChatHuggingFace(model="mistralai/Mistral-7B-v0.1")
```
#### 自定义模型类

```
from langchain_core.language_models.chat_models import BaseChatModel
class CustomChatModel(BaseChatModel):
    # 实现必要的方法
    pass
```






### 疑问点
#### 长期记忆怎样实现跨会话分享记忆？ 我目前使用postgresql实现长期记忆
