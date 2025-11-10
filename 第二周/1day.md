# 识别手写数字1到9
## 识别手写数字1到9实现步骤
1. 数据下载与加载  对应文件dataset/mnist.py
2. 使用两层神经网络进行训练，输入层784个神经元对应28x28像素图像；隐藏层50个神经元，使用sigmoid激活函数；输出层10个神经元，对应0~9十个数字，使用softmax函数输出概率分布； 对应文件 ch04/two_layer_net.py ch04/train_neuralnet.py
3. 训练完成后将网格参数保存为pickle文件 对应文件：ch04/train_neuralnet.py 和 recognize_digit.py 在train_neuralnet.py中保存为trained_model.pkl

### 实际使用流程
当运行recognize_digit.py时，程序会：
1. 加载MNIST数据集
2. 创建两层神经网络
3. 进行简短训练（在实际应用中应加载预训练模型）
4. 对测试样本进行预测并显示结果
5. 计算整体准确率
