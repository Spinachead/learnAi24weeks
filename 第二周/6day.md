# logistic Regression 逻辑斯蒂回归 (名字叫回归其实是分类）

### 回归问题
> 比如前两章学到了 x=1 y=2; x=2 y=4; x=3 y=6; 预测x=4时 y等于多少； 此时就是回归问题，是让神经网络训练逻辑预测
- 
### 分类问题
> 比如识别手写数字1~9 这个就是个分类问题； 输出是那个数字的概率最高；此时就是分类问题  是让神经网络判断这个概率
- 二分类采用的BCE损失函数
- 逻辑斯蒂回归和线性模型的明显区别是在线性模型的后面，添加了激活函数(非线性变换)
- 分布的差异：KL散度，cross-entropy交叉熵
<img width="1107" height="201" alt="image" src="https://github.com/user-attachments/assets/da03e999-960d-4093-aca3-5116d79961cb" />
<img width="1012" height="296" alt="image" src="https://github.com/user-attachments/assets/5e353714-155d-4e27-91cc-4c29666b3bda" />


### 处理多维特征的输入



### 相关知识点
1. torchvision 可以用来设置数据集
2. CIRFAR10数据集 包含有10种不同的物体图像 如：airplane automobile bird cat...
3. 饱和函数的概念 logistic函数就是饱和函数
4. 满足sigmoid functions的条件是；  函数值有极限 如-1到1、都是增函数、 饱和函数


### 不同的激活函数
<img width="842" height="787" alt="image" src="https://github.com/user-attachments/assets/146ec5ef-7a97-4c99-83a3-74d3bc55c30a" />


### 加载数据集
1. epoch  one forward pass and on backward pass of all the training examples
2. batch-size the number of training examples in one forward backward pass
3. iteration number of passes each pass using [batch size] number of examples


### 解决多分类问题
1. 在输出层之后要加一个softmax层 把输出转化为分布
2. softmax层是怎样把输出的总和概率转化为1的；是怎样把输出层的概率确保大于0的
3. crossEntropyLoss() 交叉熵损失

### 第八节作业
taitannic数据集
<img width="1033" height="450" alt="image" src="https://github.com/user-attachments/assets/e15b01e7-654a-4015-846f-307a28bb4ea4" />


### 第九节作业
阅读文档 <img width="1512" height="571" alt="image" src="https://github.com/user-attachments/assets/100945a9-43cf-4eae-b17f-2a4a08cdc039" />

crossEntryopyLoss()  交插商损失图解
<img width="1775" height="495" alt="image" src="https://github.com/user-attachments/assets/e53359d1-92e5-4abe-af56-27885475e28e" />

<img width="1051" height="434" alt="image" src="https://github.com/user-attachments/assets/c599fe42-4b27-42c2-9d82-33b168853bf4" />

### 配置kaggle下载数据集
1. conda activate torch_env
2. pip install kaggle
3. 获取kaggle的api Token; 需要登录kaggle点击个人账户 点击设置找到api部分
4. 把下载的kaggle.json存放到C:\Users\<你的用户名>\.kaggle\kaggle.json 并且设置文件权限
5. 运行kaggle的文件下载命令 如：kaggle competitions download -c titanic
