## pipeline函数的使用方法

``` from transformers import pipeline

ner = pipeline("ner",
               model="dslim/bert-base-NER",
               tokenizer="dslim/bert-base-NER",
               grouped_entities=True)
result = ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
print(result)
```

> 这段代码展示了如何使用 pipeline 进行命名实体识别(NER)任务：
"ner" 指定任务类型为命名实体识别
model 和 tokenizer 参数指定使用的具体模型和分词器
grouped_entities=True 将连续的相同实体组合在一起
直接调用 ner 对象处理文本，返回识别出的实体信息

### pipeline支持的任务类型
1. 文本分类(sentiment-analysis)
2. 命名实体识别(ner)
3. 问答(question-answering)
4. 文本摘要(summarization)
5. 文本生成(text-generation)
6. 翻译(translation)
7. 特征提取(feature-extraction)

### tokenizer 分词器
Tokenizer（分词器）是自然语言处理（NLP）中的重要组件，它的主要作用包括：
1. 文本分割：将输入的文本分割成更小的单元，如单词、子词或字符
2. 文本编码：将分割后的文本转换为模型可以处理的数字ID序列
3. 特殊标记处理：添加特殊标记如[CLS]、[SEP]、[MASK]等，帮助模型理解文本结构
4. 填充和截断：处理不同长度的文本，使其符合模型输入要求
5. 解码：将模型输出的数字序列还原为可读文本

> 简单来说，Tokenizer 是连接人类可读文本和机器可处理数字之间的桥梁。深度学习模型无法直接处理文本字符串，必须将其转换为数字向量，这就是 Tokenizer 的核心功能。

