### 使用ollama加载分词器
```
from langchain_ollama import OllamaEmbeddings
    embedding = OllamaEmbeddings(
        model="bge-small-zh-v1.5",
        base_url="http://localhost:11434"
    )
```
