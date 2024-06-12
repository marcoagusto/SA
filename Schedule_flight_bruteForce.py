import itertools

def calculate_score(schedule):
    # Menghitung skor jadwal berdasarkan kriteria tertentu
    # Misalnya, jumlah penerbangan yang dijadwalkan dengan sukses
    score = 0
    for flight in schedule:
        if flight[1] >= score:
            score += 1
    return score

def schedule_flights_brute_force(flights):
    best_schedule = []
    best_score = -1
    
    # Menghasilkan semua kemungkinan jadwal menggunakan permutations
    for schedule in itertools.permutations(flights):
        score = calculate_score(schedule)
        
        if score > best_score:
            # Jika skor jadwal saat ini lebih baik dari skor terbaik sebelumnya,
            # simpan jadwal dan skor baru sebagai yang terbaik
            best_schedule = schedule
            best_score = score
    
    return best_schedule

# Contoh penggunaan
flights = [("Flight1", 9), ("Flight2", 12), ("Flight3", 11), ("Flight4", 15), ("Flight5", 13)]
schedule = schedule_flights_brute_force(flights)
print("Jadwal penerbangan (Brute Force):")
for flight in schedule:
    print(flight[0])