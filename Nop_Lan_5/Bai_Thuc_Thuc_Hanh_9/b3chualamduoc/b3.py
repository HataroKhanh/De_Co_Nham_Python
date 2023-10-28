segments = [[-100,10], [0,6], [-5,10]]  # Danh sách các đoạn thẳng (đầu điểm và độ dài)

covered_length = 0  # Độ dài trên trục số bị phủ
previous_end = None  # Điểm kết thúc của đoạn thẳng trước đó

for segment in segments:
    start = segment[0]  # Điểm bắt đầu của đoạn thẳng
    end = segment[0] + segment[1]  # Điểm kết thúc của đoạn thẳng

    if previous_end is not None and start <= previous_end:
        # Đoạn thẳng hiện tại có giao điểm với đoạn thẳng trước đó
        if end > previous_end:
            # Đoạn thẳng hiện tại kéo dài xa hơn đoạn thẳng trước đó
            covered_length += end - previous_end
    else:
        # Đoạn thẳng hiện tại không giao điểm với đoạn thẳng trước đó
        covered_length += segment[1]

    previous_end = end

print("Độ dài trên trục số bị phủ:", covered_length)

