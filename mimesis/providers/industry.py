from mimesis.providers.base import BaseDataProvider

__all__ = ['Industry']


class Industry(BaseDataProvider):

    def __init__(self, *args, **kwargs):
        """Initialize attributes.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def api_well_number(self) -> str:
        """"Consists of:
                State Code (01 - 51; 55, 56, 61, 62)
                County Code (odd numbers starting at 001)
                Unique Well Identifier (five digit)
                Directional Sidetrack Codes (two digit)
                Event Sequence Code (two digit)

            Example number: 42-501-20130-03-00

            :return: Generated API well number
            """

        # GENERATE VALID STATE CODES (01 - 51; 55, 56, 61, 62)
        state_codes = [i for i in range(1, 52)]
        [state_codes.append(i) for i in [55, 56, 61, 62]]

        state_code = self.random.choice(state_codes)
        county_code = self.random.randrange(1, 999, 2)
        uq_well_id = self.random.randint(10000, 99999)
        dir_sidetrack_code = '0' + str(self.random.randint(1, 9))
        event_seq_code = '0' + str(self.random.randint(1, 9))

        #ADJUST LENGTH WITH ZEROS
        state_code = str(state_code).rjust(2, '0')
        county_code_ = str(county_code).rjust(3, '0')

        api_well = '-'.join((str(_)) for _ in [state_code, county_code_, uq_well_id, dir_sidetrack_code, event_seq_code])

        return api_well

    def plu_code(self) -> int:
        """Generating random Price look-up (PLU) code in range 3000-4961

        :return: Returns plu code
        """
        plu = self.random.randint(3000, 4961)

        return plu

