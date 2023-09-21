from tcp_latency import measure_latency

# Specify the host you want to measure latency to (e.g., "google.com")
host_to_measure = "deriv.com"

# Measure TCP latency to the specified host
latency_results = measure_latency(host=host_to_measure)

# Check if latency measurements were obtained
if latency_results:
    # Calculate minimum, maximum, and average latency values
    min_latency = min(latency_results)
    max_latency = max(latency_results)
    avg_latency = sum(latency_results) / len(latency_results)

    # Print the latency results
    print(f"Latency to {host_to_measure}:")
    print(f"Minimum: {min_latency} ms")
    print(f"Maximum: {max_latency} ms")
    print(f"Average: {avg_latency} ms")
else:
    print(f"Failed to measure latency to {host_to_measure}")
