from mimesis.builtins.base import BaseSpecProvider


class NetherlandsSpecProvider(BaseSpecProvider):
    """Provides data specific to nl locale"""

    class Meta:
        name = 'nl_provider'

    def bsn(self) -> str:
        """Generate a random, but valid burgerservicenummer (BSN).

        :returns: random BSN

        :Example:
            255159705
        """

        # a bsn is valid when its 9 digits pass the '11 test'
        def _is_valid_bsn(number):
            total = 0
            multiplier = 9

            for char in number:
                multiplier = -multiplier if multiplier == 1 else multiplier
                total += int(char) * multiplier
                multiplier -= 1

            return total % 11 == 0

        sample = str(self.random.randint(100000000, 999999999))
        while not _is_valid_bsn(sample):
            sample = str(self.random.randint(100000000, 999999999))

        return sample
