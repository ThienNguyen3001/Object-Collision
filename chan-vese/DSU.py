class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Hàm kiểm tra liên thông
def is_connected(image):
    rows, cols = image.shape
    dsu = DSU(rows * cols)

    # Duyệt qua các pixel
    for r in range(rows):
        for c in range(cols):
            if image[r, c] == 0:  # Pixel màu đen
                # Liên kết với các pixel lân cận
                for dr, dc in [(0, 1), (1, 0)]:  # Phải, dưới
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr, nc] == 0:
                        dsu.union(r * cols + c, nr * cols + nc)

    # Kiểm tra có duy nhất một tập chứa tất cả pixel đen
    black_pixels = [r * cols + c for r in range(rows) for c in range(cols) if image[r, c] == 0]
    if not black_pixels:
        return False

    root = dsu.find(black_pixels[0])
    return all(dsu.find(pixel) == root for pixel in black_pixels)