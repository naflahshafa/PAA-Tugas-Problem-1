import heapq

# Membuat antrian prioritas menggunakan binary heap
priority_queue = []

# Menambahkan elemen ke antrian prioritas
heapq.heappush(priority_queue, (3, 'Pekerjaan 1'))
heapq.heappush(priority_queue, (1, 'Pekerjaan 2'))
heapq.heappush(priority_queue, (2, 'Pekerjaan 3'))

# Mendapatkan elemen dengan prioritas tertinggi
highest_priority = heapq.heappop(priority_queue)
print(highest_priority)  # Output: (1, 'Pekerjaan 2')

# Menambahkan elemen baru dengan prioritas
heapq.heappush(priority_queue, (4, 'Pekerjaan 4'))

# Mendapatkan elemen dengan prioritas tertinggi setelah penambahan
highest_priority = heapq.heappop(priority_queue)
print(highest_priority)  # Output: (2, 'Pekerjaan 3')
