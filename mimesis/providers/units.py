from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.exceptions import WrongArgument

from mimesis.providers.base import BaseProvider


class UnitSystem(BaseProvider):
    """Class for generating name of unit.
    """

    @staticmethod
    def mass(symbol: bool = False) -> str:
        """Get a mass unit name.

        :param symbol: Symbol of unit.
        :return: Mass unit name.
        :Example:
            gr
        """
        if not symbol:
            return 'gram'
        return 'gr'

    @staticmethod
    def information(symbol: bool = False) -> str:
        if not symbol:
            return 'byte'
        return 'b'

    @staticmethod
    def thermodynamic_temperature(symbol: bool = False) -> str:
        """Get the thermodynamic temperature unit name.

        :param symbol: Symbol of unit.
        :return: Thermodynamic temperature unit name
        :Example:
            K
        """
        if not symbol:
            return 'kelvin'
        return 'K'

    @staticmethod
    def amount_of_substance(symbol: bool = False) -> str:
        """Get unit name of amount of substance.

        :param symbol: Symbol of unit.
        :return: Unit name of amount of substance.
        :Example:
            mol
        """
        if not symbol:
            return 'mole'
        return 'mol'

    @staticmethod
    def angle(symbol: bool = False) -> str:
        """Get unit name of angle.

        :param symbol: Symbol of unit.
        :return: Unit name of angle.
        :Example:
            radian
        """
        if not symbol:
            return 'radian'
        return 'r'

    @staticmethod
    def solid_angle(symbol: bool = False) -> str:
        """Get unit name if solid angle

        :param symbol: Symbol of unit.
        :return: Unit name of solid angle
        :Example:
            ㏛
        """
        if not symbol:
            return 'steradian'
        return '㏛'

    @staticmethod
    def frequency(symbol: bool = False) -> str:
        """Get unit name of frequency.

        :param symbol: Symbol of unit.
        :return: Unit name if frequency.
        :Example:
            Hz
        """
        if not symbol:
            return 'hertz'
        return 'Hz'

    @staticmethod
    def force(symbol: bool = False) -> str:
        """Get unit name of fore.

        :param symbol:  Symbol of unit.
        :return:  Unit name of force.
        :Example:
            N
        """
        if not symbol:
            return 'newton'
        return 'N'

    @staticmethod
    def pressure(symbol: bool = False) -> str:
        """Get unit name of pressure.

        :param symbol: Symbol of unit.
        :return: Unit name of pressure.
        :Example:
            pascal
        """
        if not symbol:
            return 'pascal'
        return 'P'

    @staticmethod
    def energy(symbol: bool = False) -> str:
        """Get unit name of energy.

        :param symbol: Symbol of unit.
        :return: Unit name of energy.
        :Example:
            J
        """
        if not symbol:
            return 'joule'
        return 'J'

    @staticmethod
    def power(symbol: bool = False) -> str:
        """Get unit name of power.

        :param symbol: Symbol of unit.
        :return: Unit name of power.
        :Example:
            watt
        """
        if not symbol:
            return 'watt'
        return 'W'

    def flux(self, symbol: bool = True) -> str:
        return self.power(symbol)

    @staticmethod
    def electric_charge(symbol: bool = False) -> str:
        """Get unit name of electric charge.

        :param symbol: Symbol of unit.
        :return: Unit name of electric charge.
        :Example:
            coulomb
        """
        if not symbol:
            return 'coulomb'
        return 'C'

    @staticmethod
    def voltage(symbol: bool = False) -> str:
        """Get unit name of voltage.

        :param symbol: Symbol of unit.
        :return: Unit name of voltage.
        :Example:
            volt
        """
        if not symbol:
            return 'volt'
        return 'V'

    @staticmethod
    def electric_capacitance(symbol: bool = False) -> str:
        """Get unit name of electric capacitance.

        :param symbol: Symbol of unit.
        :return: Unit name of electric capacitance.
        :Example:
            F
        """
        if not symbol:
            return 'farad'
        return 'F'

    @staticmethod
    def electric_resistance(symbol: bool = False) -> str:
        """Get name of electric resistance.

        :param symbol: Symbol of unit.
        :return: Name of electric resistance.
        :Example:
            Ω
        """
        if not symbol:
            return 'ohm'
        return 'Ω'

    def impedance(self, symbol: bool = False) -> str:
        return self.electric_resistance(symbol)

    def reactance(self, symbol: bool = False) -> str:
        return self.electric_resistance(symbol)

    @staticmethod
    def electrical_conductance(symbol: bool = False) -> str:
        """Get unit name of electrical conductance.

        :param symbol: Symbol of unit.
        :return: Unit name of electrical conductance.
        :Example:
            siemens
        """
        if not symbol:
            return 'siemens'
        return 'S'

    @staticmethod
    def magnetic_flux(symbol: bool = False) -> str:
        """Get unit name of magnetic flux.

        :param symbol: Symbol of unit.
        :return: Unit name of magnetic flux.
        :Example:
            Wb
        """
        if not symbol:
            return 'weber'
        return 'Wb'

    @staticmethod
    def magnetic_flux_density(symbol: bool = False) -> str:
        """Get unit name of magnetic flux density.

        :param symbol: Symbol of unit.
        :return: Unit name of magnetic flux density.
        :Example:
            tesla
        """
        if not symbol:
            return 'tesla'
        return 'T'

    @staticmethod
    def inductance(symbol: bool = False) -> str:
        """Get unit name of inductance.

        :param symbol: Symbol of unit.
        :return: Unit name of inductance.
        :Example:
            H
        """
        if not symbol:
            return 'henry'
        return 'H'

    @staticmethod
    def temperature(symbol: bool = False) -> str:
        """Get unit name of temperature.

        :param symbol:
        :return:
        """
        if not symbol:
            return 'Celsius'
        return '°C'

    @staticmethod
    def radioactivity(symbol: bool = False) -> str:
        """Get unit name of radioactivity.

        :param symbol: Symbol of unit.
        :return: Unit name of radioactivity.
        :Example:
            Bq
        """
        if not symbol:
            return 'becquerel'
        return 'Bq'

    def prefix(self, sign: str = 'positive', symbol: bool = False) -> str:
        """Get a random prefix for the International System of Units (SI)

        :param sign: Sing of number (positive, negative)
        :param symbol: Return symbol of prefix.
        :return: Prefix for SI.
        :Example:
            mega
        """
        sign = sign.lower()

        prefixes = SI_PREFIXES_SYM if \
            symbol else SI_PREFIXES

        try:
            prefixes = self.random.choice(prefixes[sign])  # type: ignore
            return prefixes  # type: ignore
        except KeyError:
            raise WrongArgument(
                "Unsupported sign. Use: 'positive' or 'negative'")
