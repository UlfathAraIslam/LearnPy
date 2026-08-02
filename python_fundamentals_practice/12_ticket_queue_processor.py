def serve_queue(queue):
    served = []
    q = queue[:]
    while q:
        ticket = q.pop(0)
        if ticket == "END":
            break
        served.append(ticket)
    return served
print(serve_queue([101, 102, 103, "END", 104]))

