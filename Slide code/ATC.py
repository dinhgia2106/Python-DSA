class Tree:
    """Lớp cơ sở trừu tượng biểu diễn cấu trúc cây."""

    # ------------------------ lớp Position lồng nhau ------------------------
    class Position:
        """Trừu tượng hóa vị trí của một phần tử đơn lẻ."""

        def element(self):
            """Trả về phần tử được lưu tại Position này."""
            raise NotImplementedError('phải được triển khai bởi lớp con')

        def __eq__(self, other):
            """Trả về True nếu other Position biểu diễn cùng một vị trí."""
            raise NotImplementedError('phải được triển khai bởi lớp con')

        def __ne__(self, other):
            """Trả về True nếu other Position không biểu diễn cùng vị trí."""
            return not (self == other)    # ngược lại của __eq__

    # ----------- các phương thức trừu tượng mà lớp con phải hỗ trợ -----------
    def root(self):
        """Trả về Position biểu diễn gốc của cây (hoặc None nếu rỗng)."""
        raise NotImplementedError('phải được triển khai bởi lớp con')

    def parent(self, p):
        """Trả về Position biểu diễn cha của p (hoặc None nếu p là gốc)."""
        raise NotImplementedError('phải được triển khai bởi lớp con')

    def num_children(self, p):
        """Trả về số lượng con của Position p."""
        raise NotImplementedError('phải được triển khai bởi lớp con')

    def children(self, p):
        """Tạo một iteration của các Position biểu diễn con của p."""
        raise NotImplementedError('phải được triển khai bởi lớp con')

    def __len__(self):
        """Trả về tổng số phần tử trong cây."""
        raise NotImplementedError('phải được triển khai bởi lớp con')

    # ----------- các phương thức cụ thể được triển khai trong lớp này -----------
    def is_root(self, p):
        """Trả về True nếu Position p biểu diễn gốc của cây."""
        return self.root() == p

    def is_leaf(self, p):
        """Trả về True nếu Position p không có bất kỳ con nào."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Trả về True nếu cây rỗng."""
        return len(self) == 0
