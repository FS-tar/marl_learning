from mpe2 import simple_spread_v3


def main():
    env = simple_spread_v3.parallel_env(render_mode=None)
    observations, infos = env.reset(seed=42)

    print("PettingZoo MPE simple_spread_v3 random policy demo")
    print("=" * 60)

    for agent, observation in observations.items():
        action_space = env.action_space(agent)
        print(f"agent: {agent}")
        print(f"observation shape: {observation.shape}")
        print(f"action_space: {action_space}")
        print("-" * 60)

    for step in range(5):
        actions = {
            agent: env.action_space(agent).sample()
            for agent in env.agents
        }
        observations, rewards, terminations, truncations, infos = env.step(actions)

        print(f"step: {step + 1}")
        for agent, reward in rewards.items():
            print(f"agent: {agent}, reward: {reward}")
        print("-" * 60)

        if all(terminations.values()) or all(truncations.values()):
            break

    env.close()


if __name__ == "__main__":
    main()
