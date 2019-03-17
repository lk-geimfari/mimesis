# -*- coding: utf-8 -*-

"""Provides data related to hardware."""

from mimesis.data import (
    CPU,
    CPU_CODENAMES,
    CPU_MODEL_CODES,
    GENERATION,
    GRAPHICS,
    HDD_SSD,
    MANUFACTURERS,
    PHONE_MODELS,
    RAM_SIZES,
    RAM_TYPES,
    RESOLUTIONS,
    SCREEN_SIZES,
)
from mimesis.providers.base import BaseProvider

__all__ = ['Hardware']


class Hardware(BaseProvider):
    """Class for generate data related to hardware."""

    class Meta:
        """Class for metadata."""

        name = 'hardware'

    def resolution(self) -> str:
        """Get a random screen resolution.

        :return: Resolution of screen.

        :Example:
            1280x720.
        """
        return self.random.choice(RESOLUTIONS)

    def screen_size(self) -> str:
        """Get a random size of screen in inch.

        :return: Screen size.

        :Example:
            13″.
        """
        return self.random.choice(SCREEN_SIZES)

    def cpu(self) -> str:
        """Get a random CPU name.

        :return: CPU name.

        :Example:
            Intel® Core i7.
        """
        return self.random.choice(CPU)

    def cpu_frequency(self) -> str:
        """Get a random frequency of CPU.

        :return: Frequency of CPU.

        :Example:
            4.0 GHz.
        """
        return '{}GHz'.format(
            self.random.uniform(
                a=1.5,
                b=4.3,
                precision=1,
            ),
        )

    def generation(self) -> str:
        """Get a random generation.

        :return: Generation of something.

        :Example:
             6th Generation.
        """
        return self.random.choice(GENERATION)

    def cpu_model_code(self) -> str:
        """Get a random CPU model.

        :return: CPU model.
        """
        return self.random.choice(CPU_MODEL_CODES)

    def cpu_codename(self) -> str:
        """Get a random CPU code name.

        :return: CPU code name.

        :Example:
            Cannonlake.
        """
        return self.random.choice(CPU_CODENAMES)

    def ram_type(self) -> str:
        """Get a random RAM type.

        :return: Type of RAM.

        :Example:
            DDR3.
        """
        return self.random.choice(RAM_TYPES)

    def ram_size(self) -> str:
        """Get a random size of RAM.

        :return: RAM size.

        :Example:
            16GB.
        """
        return self.random.choice(RAM_SIZES)

    def ssd_or_hdd(self) -> str:
        """Get a random value from list.

        :return: HDD or SSD.

        :Example:
            512GB SSD.
        """
        return self.random.choice(HDD_SSD)

    def graphics(self) -> str:
        """Get a random graphics.

        :return: Graphics.

        :Example:
            Intel® Iris™ Pro Graphics 6200.
        """
        return self.random.choice(GRAPHICS)

    def manufacturer(self) -> str:
        """Get a random manufacturer.

        :return: Manufacturer.

        :Example:
            Dell.
        """
        return self.random.choice(MANUFACTURERS)

    def phone_model(self) -> str:
        """Get a random phone model.

        :return: Phone model.

        :Example:
            Nokia Lumia 920.
        """
        return self.random.choice(PHONE_MODELS)
