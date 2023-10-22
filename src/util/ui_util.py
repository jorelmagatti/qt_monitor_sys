import sys
import psutil

def get_percentual_usage_cpu() -> float:
    return psutil.cpu_percent()

def get_percentual_usage_memory_ram() -> float:
    return psutil.virtual_memory().percent

def get_percentual_usage_memory_swap() -> float:
    return psutil.swap_memory().percent

def get_percentual_usage_disk_root() -> float:
    return psutil.disk_usage("/").percent
