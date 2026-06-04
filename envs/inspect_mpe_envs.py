from pathlib import Path

from mpe2 import simple_adversary_v3, simple_spread_v3, simple_tag_v3


EPISODES = 3
REPORT_PATH = Path(__file__).resolve().parents[1] / "notes" / "02_mpe_env_report.md"

ENV_SPECS = [
    ("simple_spread_v3", simple_spread_v3),
    ("simple_adversary_v3", simple_adversary_v3),
    ("simple_tag_v3", simple_tag_v3),
]


def observation_shape(observation):
    return getattr(observation, "shape", "unknown")


def inspect_environment(env_name, env_module):
    env = env_module.parallel_env(render_mode=None)
    observations, infos = env.reset(seed=42)
    agents = list(env.agents)

    agent_info = {}
    for agent in agents:
        agent_info[agent] = {
            "observation_space": str(env.observation_space(agent)),
            "action_space": str(env.action_space(agent)),
            "observation_shape": str(observation_shape(observations[agent])),
        }

    env.close()

    reward_totals = {agent: 0.0 for agent in agents}

    for episode in range(EPISODES):
        env = env_module.parallel_env(render_mode=None)
        observations, infos = env.reset(seed=100 + episode)

        while env.agents:
            actions = {
                agent: env.action_space(agent).sample()
                for agent in env.agents
            }
            observations, rewards, terminations, truncations, infos = env.step(actions)

            for agent, reward in rewards.items():
                reward_totals.setdefault(agent, 0.0)
                reward_totals[agent] += float(reward)

            if terminations and all(terminations.values()):
                break
            if truncations and all(truncations.values()):
                break

        env.close()

    average_rewards = {
        agent: total / EPISODES
        for agent, total in reward_totals.items()
    }

    return {
        "name": env_name,
        "agents": agents,
        "agent_info": agent_info,
        "average_rewards": average_rewards,
    }


def print_environment_report(result):
    print(f"Environment: {result['name']}")
    print("=" * 80)
    print(f"agents: {result['agents']}")
    print()

    for agent in result["agents"]:
        info = result["agent_info"][agent]
        print(f"agent: {agent}")
        print(f"observation_space: {info['observation_space']}")
        print(f"action_space: {info['action_space']}")
        print(f"reset observation shape: {info['observation_shape']}")
        print(f"average reward over {EPISODES} episodes: {result['average_rewards'][agent]:.6f}")
        print("-" * 80)

    print()


def build_markdown_report(results):
    lines = [
        "# MPE 环境检查报告",
        "",
        f"Random policy episodes per environment: {EPISODES}",
        "",
    ]

    for result in results:
        lines.extend([
            f"## {result['name']}",
            "",
            f"- agents: `{result['agents']}`",
            "",
            "| agent | observation_space | action_space | reset observation shape | average reward |",
            "| --- | --- | --- | --- | --- |",
        ])

        for agent in result["agents"]:
            info = result["agent_info"][agent]
            lines.append(
                f"| `{agent}` | `{info['observation_space']}` | "
                f"`{info['action_space']}` | `{info['observation_shape']}` | "
                f"{result['average_rewards'][agent]:.6f} |"
            )

        lines.append("")

    return "\n".join(lines)


def main():
    results = []

    for env_name, env_module in ENV_SPECS:
        result = inspect_environment(env_name, env_module)
        results.append(result)
        print_environment_report(result)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_markdown_report(results), encoding="utf-8")
    print(f"Report written to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
