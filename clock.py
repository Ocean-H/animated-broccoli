import time

def focus_timer(duration):
    print(f"Focus for {duration} seconds.")
    time.sleep(duration)
    print("Time's up!")

# 使用专注时钟，例如专注300秒（5分钟）
focus_timer(300)
