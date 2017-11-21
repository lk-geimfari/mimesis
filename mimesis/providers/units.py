from typing import Optional

from mimesis.enums import PrefixSign
from mimesis.exceptions import NonEnumerableError
from mimesis.data import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.providers.base import BaseProvider


class UnitSystem(BaseProvider):
    """Class for generating name of unit.
    """

    @staticmethod
    def mass(symbol: bool = False) -> str:
        """Get a mass unit name.

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol:  Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
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

        :param bool symbol: Symbol of unit.
        :return: Unit of temperature.

        """
        if not symbol:
            return 'Celsius'
        return '°C'

    @staticmethod
    def radioactivity(symbol: bool = False) -> str:
        """Get unit name of radioactivity.

        :param bool symbol: Symbol of unit.
        :return: Unit name of radioactivity.

        :Example:
            Bq
        """
        if not symbol:
            return 'becquerel'
        return 'Bq'

    def prefix(self, sign: Optional[PrefixSign] = None,
               symbol: bool = False) -> str:
        """Get a random prefix for the International System of Units (SI)

        :param sign: Sing of number (positive, negative)
        :param symbol: Return symbol of prefix.
        :return: Prefix for SI.
        :raises KeyError: if sign is not supported.

        :Example:
            mega
        """
        prefixes = SI_PREFIXES_SYM if \
            symbol else SI_PREFIXES

        if sign is None:
            sign = PrefixSign.get_random_item()

        if sign in PrefixSign:
            return self.random.choice(prefixes[sign.value])
        else:
            raise NonEnumerableError('PrefixSign')
