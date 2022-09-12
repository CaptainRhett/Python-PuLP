# Python-PuLP库学习
数据处理与建模系列
<h1>PuLP 解线性规划问题</h1>
<h2>线性规划问题概述</h2>
<p>一般线性规划问可以表述为</p>
<p><img src="https://img2022.cnblogs.com/blog/2966064/202209/2966064-20220911225115687-427097305.png" /></p>
<p>其中a、b、c均是已知的参数</p>
<p>满足所有约束条件的解，称为线性规划问题的可行解；</p>
<p>所有可行解构成的集合，称为可行域。</p>
<p>使目标函数达到最小值的解，称为最优解。</p>
<p>线性规划问题的解决通常为以下过程：</p>
<ol>
<li>确定变量、约束条件</li>
<li>构造目标函数、建立数学方程、确定参数</li>
<li>解出可行域和最优解</li>
</ol>
<h2>用PuLP库解线性规划模型</h2>
<p>例题1 ：</p>
<p><img src="https://img2022.cnblogs.com/blog/2966064/202209/2966064-20220911225915196-1824363137.png" /></p>
<h3>导入PuLP库</h3>
<pre class="language-python highlighter-hljs"><code>import pulp</code></pre>
<h3>问题初始化</h3>
<pre class="language-python highlighter-hljs"><code>LPprob = pulp.LpProblem("Lpproblem",sense = pulp.LpMaximize)
#代码中的LpProblem方法是定义问题的构造函数
#&ldquo;Lpproblem&rdquo;是定义的问题名称，用于输出信息
#参数 sense是用来指定优化方向（是求最大还是最小）
#最大值用参数 pulp.LpMaximize
#最小值用参数 pulp.LpMinimize</code></pre>
<h3>定义变量</h3>
<p>基本方法</p>
<pre class="language-python highlighter-hljs"><code>x1 = pulp.LpVariable('x1',lowBound = 0 , upBound = 7, cat = 'Continuous')
x2 = pulp.LpVariable('x2',lowBound = 0 , upBound = 7, cat = 'Continuous')
x3 = pulp.LpVariable('x3',lowBound = 0 , upBound = 7, cat = 'Continuous')
#&lsquo;x1&rsquo;是定义的变量名
#lowBound和upBound 是定义变量取值的上下界 ， 可以不加定义，默认为负无穷大到正无穷大
#cat 定义变量类型 
##&lsquo;Continuous&rsquo;是连续型变量（默认）
##&lsquo;Integer&rsquo; 表示离散变量（用于整数规划问题）
##&lsquo;Binary&rsquo;表示0/1变量（用于0-1规划问题）</code></pre>
<p>&nbsp;</p>
<h3>定义目标函数</h3>
<pre class="language-python highlighter-hljs"><code>LPprob += 2*x1 + 3*x2 - 5*x3
#在问题初始化中定义的问题变量名称 += 目标函数式</code></pre>
<h3>添加约束条件</h3>
<pre class="language-python highlighter-hljs"><code>LPprob += (2*x1 - 5*x2 + x3 &gt;= 10)  # 不等式约束
LPprob += (x1 + 3*x2 + x3 &lt;= 12)  # 不等式约束
LPprob += (x1 + x2 + x3 == 7)  # 等式约束
#问题变量名 +=(约束条件表达式)
#特别注意等于是两个等号！</code></pre>
<h3>&nbsp;输出求解结果</h3>
<pre class="language-python highlighter-hljs"><code>LPprob.solve() #
print('Status:',pulp.LpStatus[LPprob.status])#输出求解状态 有可能是无解
for i in LPprob.variables():
    print(i.name,"=" , i.varValue) #输出每个变量的最优解
print（"F(x) = " , pulp.value(LPprob.objective)) #输出最优解所对应的目标函数值</code></pre>
<p>&nbsp;</p>
