bucket_size = 2500 # mm
pieces_to_fit = [1200, 900, 300, 700, 800, 100, 400, 110, 2000, 1200, 20, 90, 1100]
slag = 2

def add_bucket(buckets, index):
    buckets[index] = dict()
    buckets[index]["sum"] = 0
    buckets[index]["pieces"] = []

def add_piece_to_bucket(buckets, index, piece_size):
    buckets[index]["sum"] += piece_size + slag
    buckets[index]["pieces"].append(piece_size)

buckets = dict()
add_bucket(buckets, 0)

for piece_size in sorted(pieces_to_fit, reverse=True):
    # check existing buckets and add
    piece_added = False
    for b in buckets:
        if bucket_size - buckets[b]["sum"] >= piece_size:
            add_piece_to_bucket(buckets, b, piece_size)
            piece_added = True
            break
    if not piece_added:
        next_index = len(buckets)
        add_bucket(buckets, next_index)
        add_piece_to_bucket(buckets, next_index, piece_size)

# print result
print("input: ", pieces_to_fit)
print("result: ")
for b in buckets:
    print("  bucket ", b, ": ")
    print("    ", buckets[b])
print("You should plan for", len(buckets), "buckets.")

# final test
pieces_fitted = 0
for b in buckets:
    pieces_fitted += len(buckets[b]["pieces"])
# print test result
if len(pieces_to_fit) == pieces_fitted:
    print("Final test passed.")
else:
    print("Final test failed.")