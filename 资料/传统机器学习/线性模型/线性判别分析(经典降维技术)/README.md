输入：训练样本集 $X_{\text{train}}$，包含 $n$ 个样本，每个样本有 $d$ 个特征
       训练样本的类别标签 $y_{\text{train}}$，包含 $n$ 个类别标签

1. 对每个类别，计算类别内散度矩阵 $S_w$ 和类别间散度矩阵 $S_b$：
   1.1 初始化 $S_w$ 和 $S_b$ 为 $d$ 维的零矩阵
   1.2 对于每个类别 $c$：
       1.2.1 提取属于类别 $c$ 的样本集 $X_c$
       1.2.2 计算类别内散度矩阵 $S_{w_c} = (X_c - \text{mean}(X_c))(X_c - \text{mean}(X_c))^T$
       1.2.3 计算类别间散度矩阵 $S_{b_c} = n_c(\text{mean}(X_c) - \text{mean}(X))(\text{mean}(X_c) - \text{mean}(X))^T$
       1.2.4 将 $S_{w_c}$ 和 $S_{b_c}$ 累加到 $S_w$ 和 $S_b$ 中

2. 计算 $S_w$ 的逆矩阵 $S_w^{-1}$ 和 $S_w$ 与 $S_b$ 的乘积 $S_w^{-1}S_b$：
   2.1 计算 $S_w^{-1} = \text{inv}(S_w)$
   2.2 计算 $S_w^{-1}S_b = S_w^{-1}S_b$

3. 对 $S_w^{-1}S_b$ 进行特征值分解：
   3.1 计算 $S_w^{-1}S_b$ 的特征值 $eigenvalues$ 和对应的特征向量 $eigenvectors$

4. 选择前 $k$ 个最大的特征值对应的特征向量作为投影矩阵 $W$：
   4.1 将 $eigenvectors$ 按照对应的 $eigenvalues$ 降序排列
   4.2 选择前 $k$ 个特征向量作为投影矩阵 $W$

5. 将训练样本集投影到低维空间：
   5.1 计算投影后的样本集 $X_{\text{train\_lda}} = X_{\text{train}} \cdot W$

输出：投影后的样本集 $X_{\text{train\_lda}}$ 和对应的类别标签 $y_{\text{train}}$

![image-20230904010428914](http://image.zzzsleep.icu/202309040104065.png)
