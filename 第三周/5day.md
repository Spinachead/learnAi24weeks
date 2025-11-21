## pipeline函数的使用方法

```
from transformers import pipeline

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
6. tokenizer采用基于子词（subword)方式拆分句子
7. inputs ID 的转换由 tokenizer 的 convert_tokens_to_ids() 方法实现：
8.  `` ids = tokenizer.convert_tokens_to_ids(tokens) ``
9.  解码（Decoding) 从一个inputs ID到一个字符串是通过decode()方法实现  `` decoded_string = tokenizer.decode([7993, 170, 11303, 1200, 2443, 1110, 3014]) ``
10.  tokenizer的用法
11. 子词分词的例子有 wordPiece  BPE（byte pair encoding) unigram
12. 
> 简单来说，Tokenizer 是连接人类可读文本和机器可处理数字之间的桥梁。深度学习模型无法直接处理文本字符串，必须将其转换为数字向量，这就是 Tokenizer 的核心功能。

### 加载和保存模型
1. 加载已经训练过的Transformers模型使用 from_pretrained()
2. 保存模型使用 save_pretrained()
```
from transformers import BertConfig, BertModel
config = BertConfig()
model = BertModel(config)
model = BertModel.from_pretrained("bert-base-cased")
```
3. 保存模型后会有两个文件 config.json  model.safetensors文件
4. config.json 文件包含构建模型架构所需要的属性
5. model.safetensors文件被称为state dictionary (状态字典) 他包含了模型的所有权重


### 模型头 （head层)  
> 一个附加组件 通常由一个或几个层组成 用于将transformer的预测转换为特定任务的输出


## conda 下载huggingface dataset
`` pip install datasets accelerate -u ``


