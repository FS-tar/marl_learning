# MPE 环境检查报告

Random policy episodes per environment: 3

## simple_spread_v3

- agents: `['agent_0', 'agent_1', 'agent_2']`

| agent | observation_space | action_space | reset observation shape | average reward |
| --- | --- | --- | --- | --- |
| `agent_0` | `Box(-inf, inf, (18,), float32)` | `Discrete(5)` | `(18,)` | -21.527987 |
| `agent_1` | `Box(-inf, inf, (18,), float32)` | `Discrete(5)` | `(18,)` | -21.361320 |
| `agent_2` | `Box(-inf, inf, (18,), float32)` | `Discrete(5)` | `(18,)` | -21.027987 |

## simple_adversary_v3

- agents: `['adversary_0', 'agent_0', 'agent_1']`

| agent | observation_space | action_space | reset observation shape | average reward |
| --- | --- | --- | --- | --- |
| `adversary_0` | `Box(-inf, inf, (8,), float32)` | `Discrete(5)` | `(8,)` | -28.475550 |
| `agent_0` | `Box(-inf, inf, (10,), float32)` | `Discrete(5)` | `(10,)` | 8.688558 |
| `agent_1` | `Box(-inf, inf, (10,), float32)` | `Discrete(5)` | `(10,)` | 8.688558 |

## simple_tag_v3

- agents: `['adversary_0', 'adversary_1', 'adversary_2', 'agent_0']`

| agent | observation_space | action_space | reset observation shape | average reward |
| --- | --- | --- | --- | --- |
| `adversary_0` | `Box(-inf, inf, (16,), float32)` | `Discrete(5)` | `(16,)` | 16.666667 |
| `adversary_1` | `Box(-inf, inf, (16,), float32)` | `Discrete(5)` | `(16,)` | 16.666667 |
| `adversary_2` | `Box(-inf, inf, (16,), float32)` | `Discrete(5)` | `(16,)` | 16.666667 |
| `agent_0` | `Box(-inf, inf, (14,), float32)` | `Discrete(5)` | `(14,)` | -18.484905 |
