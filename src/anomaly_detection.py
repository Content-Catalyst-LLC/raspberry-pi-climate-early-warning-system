import statistics

pressure_series = [1008,1007,1009,1008,996]

mean = statistics.mean(pressure_series)
stdev = statistics.pstdev(pressure_series)

latest = pressure_series[-1]

if latest < mean - 2 * stdev:
    print("Rapid pressure drop detected — possible storm system.")
else:
    print("No anomaly detected.")
