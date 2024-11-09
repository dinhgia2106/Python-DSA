from Empty import Empty


class ArrayStack:
    """Ngăn xếp LIFO được triển khai bằng list Python làm bộ nhớ."""

    def __init__(self):
        """Tạo một ngăn xếp rỗng."""
        self._data = []                  # khởi tạo list không công khai

    def __len__(self):
        """Trả về số lượng phần tử trong ngăn xếp."""
        return len(self._data)

    def is_empty(self):
        """Trả về True nếu ngăn xếp rỗng."""
        return len(self._data) == 0

    def push(self, e):
        """Thêm phần tử e vào đỉnh của ngăn xếp."""
        self._data.append(e)             # phần tử mới được lưu ở cuối list

    def top(self):
        """Trả về (nhưng không xóa) phần tử ở đỉnh của ngăn xếp.

        Raise Empty exception nếu ngăn xếp rỗng.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]            # phần tử cuối cùng trong list

    def pop(self):
        """Xóa và trả về phần tử từ đỉnh của ngăn xếp (theo LIFO).

        Raise Empty exception nếu ngăn xếp rỗng.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()          # xóa phần tử cuối cùng từ list
