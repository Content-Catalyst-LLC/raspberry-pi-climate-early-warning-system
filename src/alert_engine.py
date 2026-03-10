def check_alerts(rainfall_mm, river_level_cm):

    if rainfall_mm > 50:
        print("Heavy rainfall warning")

    if river_level_cm > 200:
        print("Flood risk warning")

if __name__ == "__main__":
    check_alerts(60,210)
