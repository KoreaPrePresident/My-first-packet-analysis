from scapy.all import sniff, raw
import numpy as np

# 1️⃣ TCP 패킷 100개 캡처
packets = sniff(filter="tcp", count=100)

# 2️⃣ raw 바이트 추출
packet_bytes = [raw(pkt) for pkt in packets]

# 3️⃣ 최대 길이 구하기 (패딩용)
max_len = max(len(p) for p in packet_bytes)

# 4️⃣ 0으로 패딩
padded_packets = [
    p + b'\x00' * (max_len - len(p))
    for p in packet_bytes
]

# 5️⃣ NumPy 배열로 변환 (0~255 값)
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

# 결과 보기
for row, count in zip(unique_rows, counts):
    print(f"{row} : {count}번")

unique_rows, counts = np.unique(dst_addr, axis=0, return_counts=True)

# 결과 보기
for row, count in zip(unique_rows, counts):
    print(f"{row} : {count}번")

