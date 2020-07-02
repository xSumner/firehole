class Covert(object):
    def __init__(self):
        self.wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1, ]
        self.vi = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2, ]

    def get_verity(self, eighteen_card: str) -> str:
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
        15位转18位
        :param fifteen_card:
        :return:
        """
        eighteen_card = fifteen_card[0:6] + '19' + fifteen_card[6:15]
        return eighteen_card + self.get_verity(eighteen_card)

    def down_to_fifteen(self, eighteen_card: str) -> str:
        """
        18位转15位
        :param eighteen_card:
        :return:
        """
        return eighteen_card[0:6] + eighteen_card[8:17]


if __name__ == '__main__':
    c = Covert()
    test_id_number = "342425199209045710"
    fifteen = c.down_to_fifteen(test_id_number)
    eighteen = c.up_to_eighteen(fifteen)
    print(fifteen, "<-->", eighteen)  # 342425920904571 <--> 342425199209045710
