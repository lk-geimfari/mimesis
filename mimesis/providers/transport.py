from mimesis.data import AIRPLANES, CARS, TRUCKS, VR_CODES, VRC_BY_LOCALES
from mimesis.providers.base import BaseProvider
from mimesis.utils import custom_code


class Transport(BaseProvider):
    """Class that provides dummy data about transport."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def truck(self, model_mask: str = '#### @@') -> str:
        """Generate a truck model.

        :param str model_mask: Mask of truck model. Here '@' is a \
        placeholder of characters and '#' is a placeholder of digits.
        :return: Dummy truck model.

        :Example:
            Caledon-966O.
        """
        model = custom_code(mask=model_mask)
        truck = self.random.choice(TRUCKS)
        return '{}-{}'.format(truck, model)

    def car(self) -> str:
        """Get a random vehicle.

        :return: A vehicle.

        :Example:
            Tesla Model S.
        """
        return self.random.choice(CARS)

    def airplane(self, model_mask: str = '###') -> str:
        """Generate a dummy airplane model.

        :param str model_mask: Mask of truck model. Here '@' is a \
        placeholder of characters and '#' is a placeholder of digits.
        :return: Airplane model.

        :Example:
            Boeing 727.
        """
        model = custom_code(mask=model_mask)
        plane = self.random.choice(AIRPLANES)
        return '{} {}'.format(plane, model)

    def vehicle_registration_code(self, allow_random: bool = True) -> str:
        """Get vehicle registration code of country.

        :param allow_random: If False return only code
            for current locale (country).
        :return: Vehicle registration code.
        """

        if not allow_random:
            return VRC_BY_LOCALES[self.locale]

        return self.random.choice(VR_CODES)
