def simulate_second_degree_follower(
    omega_n: float,
    zeta: float,
    dt: float,
    total_time: float,
    initial_y: float = 0.0,
    initial_v: float = 0.0,
    leader_trajectory: callable = None
):
    if leader_trajectory is None:
        leader_trajectory = lambda t: 1.0 if t >= 0 else 0.0

    time_points = []
    leader_positions = []
    follower_positions = []

    y = initial_y
    v = initial_v
    current_time = 0.0

    while current_time <= total_time:
        x = leader_trajectory(current_time)

        time_points.append(current_time)
        leader_positions.append(x)
        follower_positions.append(y)

        acceleration = omega_n**2 * (x - y) - 2 * zeta * omega_n * v

        y = y + v * dt
        v = v + acceleration * dt

        current_time += dt

    return list(zip(time_points, leader_positions, follower_positions))

if __name__ == "__main__":
    natural_frequency = 5.0
    damping_ratio = 0.707
    time_step = 0.01
    simulation_duration = 5.0

    def step_leader(t):
        return 1.0 if t >= 0.1 else 0.0

    results = simulate_second_degree_follower(
        omega_n=natural_frequency,
        zeta=damping_ratio,
        dt=time_step,
        total_time=simulation_duration,
        initial_y=0.0,
        initial_v=0.0,
        leader_trajectory=step_leader
    )

    print("Time (s)\tLeader (x)\tFollower (y)")
    print("---------------------------------------")
    for i in range(min(10, len(results))):
        t, x, y = results[i]
        print(f"{t:.2f}\t\t{x:.4f}\t\t{y:.4f}")

    if len(results) > 20:
        print("...")
        for i in range(len(results) - 10, len(results)):
            t, x, y = results[i]
            print(f"{t:.2f}\t\t{x:.4f}\t\t{y:.4f}")
    elif len(results) > 10:
        for i in range(10, len(results)):
            t, x, y = results[i]
            print(f"{t:.2f}\t\t{x:.4f}\t\t{y:.4f}")

    print("\n--- Simulating with a Ramp Leader ---")
    def ramp_leader(t):
        return t if t < 2.0 else 2.0

    ramp_results = simulate_second_degree_follower(
        omega_n=natural_frequency,
        zeta=damping_ratio,
        dt=time_step,
        total_time=simulation_duration,
        initial_y=0.0,
        initial_v=0.0,
        leader_trajectory=ramp_leader
    )

    print("Time (s)\tLeader (x)\tFollower (y)")
    print("---------------------------------------")
    for i in range(min(10, len(ramp_results))):
        t, x, y = ramp_results[i]
        print(f"{t:.2f}\t\t{x:.4f}\t\t{y:.4f}")

    if len(ramp_results) > 20:
        print("...")
        for i in range(len(ramp_results) - 10, len(ramp_results)):
            t, x, y = ramp_results[i]
            print(f"{t:.2f}\t\t{x:.4f}\t\t{y:.4f}")
    elif len(ramp_results) > 10:
        for i in range(10, len(ramp_results)):
            t, x, y = ramp_results[i]
            print(f"{t:.2f}\t\t{x:.4f}\t\t{y:.4f}")