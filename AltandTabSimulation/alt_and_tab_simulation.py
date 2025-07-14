def simulate_alt_tab(windows, initial_window, num_alt_tabs):
    initial_idx = windows.index(initial_window)
    final_idx = (initial_idx + num_alt_tabs) % len(windows)
    return windows[final_idx]