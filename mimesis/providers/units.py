from mimesis.data import SI_PREFIXES
from mimesis.exceptions import WrongArgument

from .base import BaseProvider


class UnitSystem(BaseProvider):
    """Class for generating name of unit.
    """

    @staticmethod
    def mass(symbol=False):
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
    def information(symbol=False):
        if not symbol:
            return 'byte'
        return 'b'

    @staticmethod
    def thermodynamic_temperature(symbol=False):
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
    def amount_of_substance(symbol=False):
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
    def angle(symbol=False):
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
    def solid_angle(symbol=False):
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
    def frequency(symbol=False):
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
    def force(symbol=False):
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
    def pressure(symbol=False):
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
    def energy(symbol=False):
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
    def power(symbol=False):
        """Get unit name of power.

        :param symbol: Symbol of unit.
        :return: Unit name of power.
        :Example:
            watt
        """
        if not symbol:
            return 'watt'
        return 'W'

    def flux(self, symbol=True):
        return self.power(symbol)

    @staticmethod
    def electric_charge(symbol=False):
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
    def voltage(symbol=False):
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
    def electric_capacitance(symbol=False):
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
    def electric_resistance(symbol=False):
        """Get name of electric resistance.

        :param symbol: Symbol of unit.
        :return: Name of electric resistance.
        :Example:
            Ω
        """
        if not symbol:
            return 'ohm'
        return 'Ω'

    def impedance(self, symbol=False):
        return self.electric_resistance(symbol)

    def reactance(self, symbol=False):
        return self.electric_resistance(symbol)

    @staticmethod
    def electrical_conductance(symbol=False):
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
    def magnetic_flux(symbol=False):
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
    def magnetic_flux_density(symbol=False):
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
    def inductance(symbol=False):
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
    def temperature(symbol=False):
        """Get unit name of temperature.

        :param symbol:
        :return:
        """
        if not symbol:
            return 'Celsius'
        return '°C'

    @staticmethod
    def radioactivity(symbol=False):
        """Get unit name of radioactivity.

        :param symbol: Symbol of unit.
        :return: Unit name of radioactivity.
        :Example:
            Bq
        """
        if not symbol:
            return 'becquerel'
        return 'Bq'

    def prefix(self, sign='positive', symbol=False):
        """Get a random prefix for the International System of Units (SI)

        :param sign: Sing of number (positive, negative)
        :param symbol: Return symbol of prefix.
        :return: Prefix for SI.
        :rtype: str
        :Example:
            mega
        """
        sign = sign.lower()

        if symbol:
            prefixes = SI_PREFIXES['_sym_']
        else:
            prefixes = SI_PREFIXES

        try:
            return self.random.choice(prefixes[sign])
        except KeyError:
            raise WrongArgument(
                "Unsupported sign. Use: 'positive' or 'negative'")
