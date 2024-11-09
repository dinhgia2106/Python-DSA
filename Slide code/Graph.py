class Graph:
    """Biểu diễn đồ thị đơn giản sử dụng map kề."""

    # ------------------------ lớp Vertex lồng nhau ------------------------
    class Vertex:
        """Cấu trúc đỉnh nhẹ cho đồ thị."""
        __slots__ = '_element'

        def __init__(self, x):
            """Không gọi constructor trực tiếp. Sử dụng Graph.insert_vertex(x)."""
            self._element = x

        def element(self):
            """Trả về phần tử liên kết với đỉnh này."""
            return self._element

        def __hash__(self):      # cho phép đỉnh làm key của map/set
            return hash(id(self))

    # ------------------------ lớp Edge lồng nhau ------------------------
    class Edge:
        """Cấu trúc cạnh nhẹ cho đồ thị."""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            """Không gọi constructor trực tiếp. Sử dụng Graph.insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            """Trả về bộ (u,v) cho các đỉnh u và v."""
            return (self._origin, self._destination)

        def opposite(self, v):
            """Trả về đỉnh đối diện v trên cạnh này."""
            return self._destination if v is self._origin else self._origin

        def element(self):
            """Trả về phần tử liên kết với cạnh này."""
            return self._element

        def __hash__(self):      # cho phép cạnh làm key của map/set
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        """Tạo đồ thị rỗng (mặc định là vô hướng).

        Đồ thị có hướng nếu tham số tùy chọn được đặt là True.
        """
        self._outgoing = {}
        # chỉ tạo map thứ hai cho đồ thị có hướng; dùng alias cho vô hướng
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Trả về True nếu đây là đồ thị có hướng; False nếu vô hướng.

        Thuộc tính dựa trên khai báo ban đầu của đồ thị, không phải nội dung.
        """
        return self._incoming is not self._outgoing  # có hướng nếu maps khác nhau

    def vertex_count(self):
        """Trả về số lượng đỉnh trong đồ thị."""
        return len(self._outgoing)

    def vertices(self):
        """Trả về iteration của tất cả đỉnh trong đồ thị."""
        return self._outgoing.keys()

    def edge_count(self):
        """Trả về số lượng cạnh trong đồ thị."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # với đồ thị vô hướng, đảm bảo không đếm trùng cạnh
        return total if self.is_directed() else total // 2

    def edges(self):
        """Trả về tập hợp tất cả cạnh của đồ thị."""
        result = set()       # tránh báo cáo trùng cạnh của đồ thị vô hướng
        for secondary_map in self._outgoing.values():
            # thêm cạnh vào tập kết quả
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """Trả về cạnh từ u đến v, hoặc None nếu không kề."""
        return self._outgoing[u].get(v)    # trả về None nếu v không kề

    def degree(self, v, outgoing=True):
        """Trả về số lượng cạnh (đi ra) kề với đỉnh v trong đồ thị.

        Nếu đồ thị có hướng, tham số tùy chọn dùng để đếm cạnh đi vào.
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """Trả về tất cả cạnh (đi ra) kề với đỉnh v trong đồ thị.

        Nếu đồ thị có hướng, tham số tùy chọn dùng để yêu cầu cạnh đi vào.
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Chèn và trả về một Vertex mới với phần tử x."""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}    # cần map riêng cho cạnh đi vào
        return v

    def insert_edge(self, u, v, x=None):
        """Chèn và trả về một Edge mới từ u đến v với phần tử phụ x."""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e


def main():
    # Tạo đồ thị vô hướng
    g = Graph()

    # Tạo các đỉnh
    hcm = g.insert_vertex("Hồ Chí Minh")
    hn = g.insert_vertex("Hà Nội")
    dn = g.insert_vertex("Đà Nẵng")
    ct = g.insert_vertex("Cần Thơ")

    # Thêm các cạnh với khoảng cách (km)
    g.insert_edge(hcm, hn, 1160)    # HCM - Hà Nội: 1160km
    g.insert_edge(hcm, dn, 850)     # HCM - Đà Nẵng: 850km
    g.insert_edge(hcm, ct, 169)     # HCM - Cần Thơ: 169km
    g.insert_edge(hn, dn, 764)      # Hà Nội - Đà Nẵng: 764km

    # In thông tin về đồ thị
    print(f"Số đỉnh: {g.vertex_count()}")
    print(f"Số cạnh: {g.edge_count()}")

    # In các thành phố (đỉnh)
    print("\nCác thành phố:")
    for v in g.vertices():
        print(f"- {v.element()}")

    # In các kết nối (cạnh) và khoảng cách
    print("\nCác kết nối:")
    for e in g.edges():
        u, v = e.endpoints()
        print(f"{u.element()} - {v.element()}: {e.element()}km")

    # Kiểm tra bậc của mỗi đỉnh
    print("\nSố kết nối của mỗi thành phố:")
    for v in g.vertices():
        print(f"{v.element()}: {g.degree(v)} kết nối")

    # Tìm các thành phố kề với HCM
    print("\nCác thành phố kề với Hồ Chí Minh:")
    for e in g.incident_edges(hcm):
        v = e.opposite(hcm)
        print(f"- {v.element()} (cách {e.element()}km)")


if __name__ == '__main__':
    main()
