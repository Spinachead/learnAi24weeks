### 完成的事情
1. 排查和修复search_doc一直查询不到文档的bug
2. 排查retriever根据搜索查询不到文档的bug
3. 排查和处理上传不同文档时候的bug 目前已经处理了pdf和docx上传的bug
4. 解决了一些之前采用langchain0.3的警告


### 学习到知识
1. 查看langchain中retriever和vector store的相关文档
2. 排查retriever的socre_threshold过高导致检索不到文档的问题，改用相似度搜索的方式
