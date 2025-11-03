import numpy


class NdarrayUtil:
    @staticmethod
    def pad_zeros(array: numpy.ndarray, target_shape: list) -> numpy.ndarray:
        """
        ndarrayを指定サイズにzero-paddingする

        Parameters:
        -----------
        array : ndarray
            パディング対象の配列
        target_shape : tuple or list
            目標とする形状

        Returns:
        --------
        ndarray : パディング後の配列
        """
        # 各次元でのパディング幅を計算
        pad_width = [(0, target_shape[i] - array.shape[i]) for i in range(array.ndim)]
        return numpy.pad(array, pad_width, mode="constant", constant_values=0)
