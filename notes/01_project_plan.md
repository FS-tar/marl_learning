# MARL 环境学习路线

## 目标

通过 PettingZoo MPE 环境学习多智能体强化学习的基本概念、环境接口、随机策略 baseline 和基础算法实现，为后续学习 MAPPO、QMIX 等方法打基础。

## 第一阶段：理解 PettingZoo MPE

- 安装并运行 PettingZoo MPE 环境。
- 从 `simple_spread_v3` 开始，理解多个 agent 如何共享环境。
- 熟悉 Parallel API 的基本流程：`reset`、构造 actions、`step`、读取 rewards。
- 记录 observation shape、action space 和 reward 的变化。

## 第二阶段：实现 random policy baseline

- 使用每个 agent 的 action space 随机采样动作。
- 运行多个 episode，记录每个 agent 的 reward。
- 将 random policy 作为后续算法效果对比的基准。
- 初步整理实验结果保存方式，例如 CSV、图表和日志。

## 第三阶段：Independent Q-Learning

- 将每个 agent 看作独立学习者。
- 为每个 agent 设计独立的状态表示、动作选择和 Q 值更新逻辑。
- 实现 epsilon-greedy 探索。
- 对比不同探索率、学习率和折扣因子的影响。

## 第四阶段：实验管理

- 在 `experiments/configs/` 中保存实验配置。
- 在 `experiments/results/` 中保存 reward 曲线、日志和统计结果。
- 使用 pandas 和 matplotlib 分析训练过程。
- 为常用环境和算法补充测试，确保实验代码可重复运行。

## 第五阶段：进阶 MARL 算法

- 学习集中训练、分散执行（CTDE）的基本思想。
- 阅读 MAPPO 的 actor-critic 训练流程。
- 阅读 QMIX 的 value decomposition 思路。
- 在理解接口和数据流后，再逐步实现简化版本。

## 建议节奏

1. 先保证 demo 能稳定运行。
2. 再写最小 random policy 实验循环。
3. 然后实现结果记录与可视化。
4. 最后进入 Independent Q-Learning 和进阶算法。
