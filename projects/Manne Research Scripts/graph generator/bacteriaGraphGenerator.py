import csv, pygal

with open('data.csv', newline='', encoding='UTF-8') as csv_file:
    
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    headers = next(reader)
    categories = headers[1:]

    data = {category: [] for category in categories}
    for row in reader:
        for i, category in enumerate(categories, start=1):
            value = float(row[i].split()[0])
            data[category].append(value)

# makes a radar graph
    radar_chart = pygal.Radar()
    radar_chart.title = 'Bacterial Growth (Antibiotics Vs. Control)'
    radar_chart.x_labels = [f"Dish {i+1}" for i in range(len(next(iter(data.values()))))]
    for category in categories:
        radar_chart.add(category, data[category])
    radar_chart.render_to_file("radar_chart.svg")

# makes a line graph
    line_graph = pygal.Line()
    line_graph.title = 'Bacterial Growth (Antibiotics Vs. Control)'
    line_graph.x_labels = [f"Dish {i+1}" for i in range(len(next(iter(data.values()))))]
    for category in categories:
        line_graph.add(category, data[category])
    line_graph.render_to_file("line_graph.svg")
