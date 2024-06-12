def schedule_flights_greedy(flights):
    # Mengurutkan penerbangan berdasarkan waktu keberangkatan
    flights.sort(key=lambda x: x[1])
    
    # Penerbangan pertama langsung ditambahkan ke jadwal
    schedule = [flights[0]]
    
    for flight in flights[1:]:
        if flight[0] >= schedule[-1][1]:
            # Jika waktu keberangkatan penerbangan saat ini setelah waktu kedatangan penerbangan sebelumnya,
            # tambahkan penerbangan saat ini ke jadwal
            schedule.append(flight)
    
    return schedule

# Contoh penggunaan
flights = [("Flight1", 9), ("Flight2", 12), ("Flight3", 11), ("Flight4", 15), ("Flight5", 13)]
schedule = schedule_flights_greedy(flights)
print("Jadwal penerbangan (Greedy):")
for flight in schedule:
    print(flight[0])
