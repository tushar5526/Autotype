import time


def progress_bar(total_time):
    start_time = time.time()
    end_time = start_time + total_time
    bar_length = 40

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        progress = elapsed_time / total_time
        progress_bar = int(bar_length * progress)
        remaining_bar = bar_length - progress_bar

        print(
            f"[{'=' * progress_bar}{' ' * remaining_bar}] {int(progress * 100)}%",
            end="\r",
        )
        time.sleep(0.1)  # Adjust this value for smoother or faster updates

    print("\nProgress complete!")
