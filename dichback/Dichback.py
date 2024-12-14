import abc

class AlgorithmChoiceError(Exception):
    pass

class AlgorithmListIneffectiveError(Exception):
    pass


class AlgorithmSet:
    """
    算法集合，目前只有@Czy_4201b自创的二分回溯算法和普通穷举法、二分法，
    里面所有使用的逻辑单元都是整体逻辑的单元，
    也就是说，在该单元函数中，总是返回所有元素的逻辑与和或逻辑或和
    """

    def __init__(self):
        self.effective_list = []
        self.counts = 0

    @abc.abstractmethod
    def logic_unit(self, effective_list: list) -> bool:
        """
        逻辑与-逻辑或函数单元
        :param effective_list: 逻辑单元函数接收列表作为值，需要遍历所有列表元素，当所有列表元素逻辑判断为True时，函数体才能够返回True,否则返回False
        :return: 布尔值
        """
        pass

    def simple_exhaustion_algorithm(self, effective_list: list) -> list:
        """
        简单穷举法，默认使用逻辑与-逻辑或函数单元
        :param effective_list: 在逻辑与-逻辑函数单元可处理数据集中的数据子集
        :return: 列表
        """
        yes_list = []
        counts = 0
        # 遍历元素
        for i in effective_list:
            # 遍历逻辑单元
            if self.logic_unit([i]):
                yes_list.append(i)
            counts += 1
        self.counts = counts
        return yes_list

    def dichotomy_algorithm(self, effective_list: list) -> list:
        """
        二分法，默认使用逻辑与-逻辑或函数单元，仅适用于寻找一个目标元素
        :param effective_list: 在逻辑与-逻辑或函数单元可处理数据集中的数据子集
        :return: 列表
        """
        # 初始化
        counts = 0
        list_len = len(effective_list)
        min_num = 0
        max_num = list_len//2
        mark = list_len

        while True:
            effective_list_unit = [effective_list[i] for i in range(min_num, max_num)]
            ret = self.logic_unit(effective_list_unit)
            counts += 1

            if ret:
                mark = max_num
                max_num = (mark + min_num) // 2
                # 只剩一个了
                if min_num == max_num:
                    return effective_list[min_num]
            else:
                min_num = max_num
                max_num = (mark + min_num) // 2
                # 只剩一个了
                if min_num == max_num:
                    if self.logic_unit([effective_list[min_num]]):
                        return effective_list[min_num]
                    raise AlgorithmListIneffectiveError("所传入的‘有效数组‘并非有效")

    def dichotomy_backtracking_algorithm(self, effective_list: list) -> list:
        """
        二分回溯算法，默认使用逻辑与-逻辑或函数单元
        :param effective_list: 在逻辑与-逻辑或函数单元可处理数据集中的数据子集
        :return: 列表
        """
        # 初始化
        list_len = len(effective_list)
        if list_len < 4:
            raise AlgorithmChoiceError("It is NOT SUITABLE for THIS METHOD.")
        min_num = 0
        max_num = list_len
        # 最小输出元：这个就是二分区间中左边区间长度的最小值，一旦长度小于lm，将通过一一遍历的方式将左区间输出
        lm = list_len // 3 - 1
        # 记录步数
        counts = 0
        # 二分法边界 最右边区间的上界（端点）
        mark = max_num
        # 上界记录列表
        mark_steps = []
        # 记录所有逻辑判对的列表索引列表
        yes_list = []

        try:
            while True:
                # 生成列表逻辑单元
                # 逻辑单元 可以是任何有关列表的判断单元
                # 这个相当于将range(min_num, max_num)扩展到逻辑单元层次
                # 这个max_num+1别改，目前能跑
                effective_list_unit = [effective_list[i] for i in range(min_num, max_num)]
                ret = self.logic_unit(effective_list_unit)
                counts += 1
                if not ret:
                    # lm是区间长度
                    if max_num - min_num <= lm:
                        # 遍历元素
                        for i in range(min_num, max_num):
                            # 遍历逻辑单元
                            if self.logic_unit([effective_list[i]]):
                                counts += 1
                                yes_list.append(i)

                        min_num = max_num
                        max_num = mark
                        if len(mark_steps) > 1:
                            # 回溯：发生在子分支深度探索完成之后
                            mark_steps.pop()
                            mark = mark_steps[-1]
                        else:
                            # 如果pop之后没有了 那mark不变 但是写一句比较好理解
                            mark = mark_steps[-1]
                            mark_steps.pop()
                    # 左区间长度大于lm，那么就要开辟子分支
                    else:
                        mark = max_num
                        mark_steps.append(mark)
                        max_num = (mark + min_num) // 2

                else:

                    for i in range(min_num, max_num):
                        yes_list.append(i)
                    # 满区间判断true直接break
                    if mark == max_num:
                        break
                    min_num = max_num + 1
                    if len(mark_steps) > 1:
                        # 回溯
                        mark_steps.pop()
                        mark = mark_steps[-1]
                        max_num = (min_num + mark) // 2

                    else:
                        # 回到最右端点之后 相当于重新初始化
                        mark = mark_steps[-1]
                        max_num = mark
                        mark_steps.pop()
        # 结束标志
        except IndexError:
            pass

        self.counts = counts
        return [effective_list[i] for i in yes_list]
