class ConvertID(object):
    def __init__(self):
        self.wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1, ]
        self.vi = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2, ]

    def __get_verity(self, eighteen_card: str) -> str:
        ai = []
        remaining = ''
        if len(eighteen_card) == 18:
            eighteen_card = eighteen_card[0:-1]
        if len(eighteen_card) == 17:
            s = 0
            for i in eighteen_card:
                ai.append(int(i))
            for i in range(17):
                s = s + self.wi[i] * ai[i]
            remaining = s % 11
        return 'X' if remaining == 2 else str(self.vi[remaining])

    def up_to_eighteen(self, fifteen_card: str) -> str:
        """
        convert from 15 digits to 18 digits
        :param fifteen_card:
        :return:
        """
        eighteen_card = fifteen_card[0:6] + '19' + fifteen_card[6:15]
        return eighteen_card + self.__get_verity(eighteen_card)

    def down_to_fifteen(self, eighteen_card: str) -> str:
        """
        convert from 18 digits to 15 digits
        :param eighteen_card:
        :return:
        """
        return eighteen_card[0:6] + eighteen_card[8:17]
