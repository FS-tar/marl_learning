# MARL Learning

本项目用于学习多智能体强化学习（Multi-Agent Reinforcement Learning, MARL）环境与基础算法实现。

## 项目目标

学习多智能体强化学习环境，从 PettingZoo MPE 环境入手，逐步理解多智能体交互、随机策略、独立学习算法以及主流 MARL 方法。

## 学习阶段

### 第一阶段：PettingZoo MPE

- 熟悉 PettingZoo 的 AEC API 和 Parallel API。
- 运行 MPE 中的 `simple_spread_v3` 环境。
- 理解 agent、observation、action、reward、termination、truncation 的含义。

### 第二阶段：random policy

- 使用环境自带的 action space 随机采样动作。
- 观察每个 agent 的 reward 和状态变化。
- 建立最小可运行 demo，作为后续算法实验的 baseline。

### 第三阶段：Independent Q-Learning

- 为每个 agent 维护独立的 Q-learning 逻辑。
- 学习如何记录 transition、更新 value、统计实验结果。
- 对比 random policy 与 Independent Q-Learning 的表现。

### 第四阶段：MAPPO / QMIX

- 学习集中训练、分散执行的基本思想。
- 尝试理解 MAPPO 的 actor-critic 结构。
- 尝试理解 QMIX 的 value decomposition 思路。
- 为后续更完整的 MARL 训练框架做准备。

## 安装依赖

建议先创建并激活虚拟环境，然后安装依赖：

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 运行 demo

运行 PettingZoo MPE `simple_spread_v3` random policy demo：

```powershell
python envs/test_simple_spread.py
```

程序会打印每个 agent 的 observation shape、action space 和 reward。
