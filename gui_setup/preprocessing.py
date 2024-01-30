def extract_data(db_values):
    names = []
    durations = []

    for entry in db_values:
        if entry:
            data = entry[0]  # Assuming each entry is a list with a single dictionary
            names.append(data.get('name', ''))
            durations.append(data.get('production_duration_expected', 0.0))

    return names, durations
