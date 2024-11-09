class HashMapBase(MapBase):
    """Lớp cơ sở trừu tượng cho map sử dụng bảng băm với nén MAD."""

    def __init__(self, cap=11, p=109345121):
        """Tạo một bảng băm rỗng."""
        self._table = cap * [None]
        self._n = 0                          # số lượng mục trong map
        self._prime = p                      # số nguyên tố cho nén MAD
        self._scale = 1 + randrange(p-1)     # hệ số từ 1 đến p-1 cho MAD
        self._shift = randrange(p)           # độ dịch từ 0 đến p-1 cho MAD

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def _getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)    # có thể raise KeyError

    def _setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)        # subroutine duy trì self._n
        if self._n > len(self._table) // 2:  # giữ hệ số tải <= 0.5
            # số lẻ 2x - 1 thường là số nguyên tố
            self._resize(2 * len(self._table) - 1)

    def _delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)           # có thể raise KeyError
        self._n -= 1

    def _resize(self, c):                    # thay đổi kích thước mảng bucket thành capacity c
        # dùng iteration để ghi lại các mục hiện có
        old = list(self.items())
        # sau đó reset bảng về kích thước mong muốn
        self._table = c * [None]
        self._n = 0                          # n được tính lại trong các lần add tiếp theo
        for (k, v) in old:
            self[k] = v                      # thêm lại các cặp key-value cũ
