import ctypes


class DynamicArray:
    """Một mảng động có thể mở rộng như list của Python."""

    def __init__(self):
        """Tạo một mảng rỗng."""
        self._n = 0                                 # số phần tử thực tế
        self._capacity = 1                          # kích thước của mảng cơ bản
        self._A = self._make_array(self._capacity)  # mảng cấp thấp lưu trữ

    def __len__(self):
        """Trả về số phần tử trong mảng."""
        return self._n

    def __getitem__(self, k):
        """Trả về phần tử ở vị trí k."""
        if not 0 <= k < self._n:
            raise IndexError('Chỉ số không hợp lệ')
        return self._A[k]

    def append(self, obj):
        """Thêm đối tượng vào cuối mảng."""
        if self._n == self._capacity:              # cần mở rộng mảng
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Thay đổi kích thước mảng nội bộ thành c."""
        B = self._make_array(c)                    # tạo mảng mới
        for k in range(self._n):                   # sao chép các phần tử
            B[k] = self._A[k]
        self._A = B                                # dùng mảng mới thay mảng cũ
        self._capacity = c

    def _make_array(self, c):
        """Trả về một mảng mới có kích thước c."""
        return (c * ctypes.py_object)()            # xem thêm ctypes documentation
