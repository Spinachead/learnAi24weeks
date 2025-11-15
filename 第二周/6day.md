# logistic Regression 逻辑斯蒂回归 (名字叫回归其实是分类）

### 回归问题
> 比如前两章学到了 x=1 y=2; x=2 y=4; x=3 y=6; 预测x=4时 y等于多少； 此时就是回归问题，是让神经网络训练逻辑预测
- 
### 分类问题
> 比如识别手写数字1~9 这个就是个分类问题； 输出是那个数字的概率最高；此时就是分类问题  是让神经网络判断这个概率
- 采用的BCE损失函数
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
