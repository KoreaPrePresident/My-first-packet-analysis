from scapy.all import sniff, raw
import numpy as np

packets = sniff(filter="tcp", count=100)

packet_bytes = [raw(pkt) for pkt in packets]

max_len = max(len(p) for p in packet_bytes)

padded_packets = [
    p + b'\x00' * (max_len - len(p))
    for p in packet_bytes
]

np_array = np.array([list(p) for p in padded_packets], dtype=np.uint8)

print("Shape:", np_array.shape)

# for i in range(100):
#     print(f'{i+1}번째')
#     print('Src:',np_array[i][26:30])
#     print('Dst', np_array[i][30:34])
#     print(' ')
src_addr = np_array[:, 26:30]
dst_addr = np_array[:, 30:34]

unique_rows, counts = np.unique(src_addr, axis=0, return_counts=True)

for row, count in zip(unique_rows, counts):
    print(f"{row} : {count}번")

unique_rows, counts = np.unique(dst_addr, axis=0, return_counts=True)

for row, count in zip(unique_rows, counts):
    print(f"{row} : {count}번")

