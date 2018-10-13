from mimesis.providers.base import BaseDataProvider

__all__ = ['Industry']


class Industry(BaseDataProvider):

    def __init__(self, *args, **kwargs) -> None:
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def api_well_number(self) -> str:
        """Generate random API well number

            :return: Generated API well number

            :Example: 42-501-20130-03-00
            """

        state_codes = list(range(1, 52)) + [55, 56, 61, 62]

        state_code = self.random.choice(state_codes)
        county_code = self.random.randrange(1, 999, 2)
        uq_well_id = self.random.randint(10000, 99999)
        dir_sidetrack_code = '0' + str(self.random.randint(1, 9))
        event_seq_code = '0' + str(self.random.randint(1, 9))

        #ADJUST LENGTH WITH ZEROS
        state_code = str(state_code).rjust(2, '0')
        county_code = str(county_code).rjust(3, '0')

        api_well = '-'.join((str(_)) for _ in [state_code, county_code, uq_well_id, dir_sidetrack_code, event_seq_code])

        return api_well

    def plu_code(self) -> int:
        """Generating random Price look-up (PLU) code in range 3000-4961

        :return: Returns plu code
        """
        return self.random.randint(3000, 4961)


