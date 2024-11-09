class Progression:
    """Iterator tạo ra một chuỗi tiến triển.

    Mặc định iterator sẽ tạo ra các số nguyên 0, 1, 2, ..."""

    def __init__(self, start=0):
        """Khởi tạo giá trị hiện tại là giá trị đầu tiên của chuỗi."""
        self._current = start

    def _advance(self):
        """Cập nhật self._current thành một giá trị mới.

        Phương thức này nên được ghi đè bởi lớp con để tùy chỉnh chuỗi.

        Theo quy ước, nếu current được đặt là None, điều này biểu thị kết thúc của một chuỗi hữu hạn."""
        self._current += 1

    def __next__(self):
        """Trả về phần tử tiếp theo, hoặc raise StopIteration error."""
        if self._current is None:    # quy ước để kết thúc một chuỗi
            raise StopIteration()
        else:
            answer = self._current   # lưu giá trị hiện tại để trả về
            self._advance()          # tiến tới để chuẩn bị cho lần sau
            return answer            # trả về kết quả

    def __iter__(self):
        """Theo quy ước, một iterator phải trả về chính nó như một iterator."""
        return self

    def print_progression(self, n):
        """In ra n giá trị tiếp theo của chuỗi."""
        print(' '.join(str(next(self)) for j in range(n)))
