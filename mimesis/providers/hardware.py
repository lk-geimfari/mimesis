from mimesis.data import (CPU, CPU_CODENAMES, GENERATION, GENERATION_ABBR,
                          GRAPHICS, HDD_SSD, MANUFACTURERS, PHONE_MODELS,
                          RESOLUTIONS, SCREEN_SIZES)
from mimesis.providers import BaseProvider


class Hardware(BaseProvider):
    """Class for generate data about hardware."""

    def resolution(self):
        """Get a random screen resolution.

        :return: Resolution of screen.
        :Example:
            1280x720.
        """
        return self.random.choice(RESOLUTIONS)

    def screen_size(self):
        """Get a random size of screen in inch.

        :return: Screen size.
        :Example:
            13″.
        """
        return self.random.choice(SCREEN_SIZES)

    def cpu(self):
        """Get a random CPU name.

        :return: CPU name.
        :Example:
            Intel® Core i7.
        """
        return self.random.choice(CPU)

    def cpu_frequency(self):
        """Get a random frequency of CPU.

        :return: Frequency of CPU.
        :Example:
            4.0 GHz.
        """
        cf = self.random.uniform(1.5, 4.3)
        return '{0:.1f}GHz'.format(cf)

    def generation(self, abbr=False):
        """Get a random generation.

        :return: Generation of something.
        :Example:
             6th Generation.
        """
        if not abbr:
            return self.random.choice(GENERATION)

        return self.random.choice(GENERATION_ABBR)

    def cpu_codename(self):
        """Get a random CPU code name.

        :return: CPU code name.
        :Example:
            Cannonlake.
        """
        return self.random.choice(CPU_CODENAMES)

    def ram_type(self):
        """Get a random RAM type.

        :return: Type of RAM.
        :Example:
            DDR3.
        """
        ram_types = ('DDR2', 'DDR3', 'DDR4')
        return self.random.choice(ram_types)

    def ram_size(self):
        """Get a random size of RAM.

        :return: RAM size.
        :Example:
            16GB.
        """
        sizes = ('4', '6', '8', '16', '32', '64')
        return self.random.choice(sizes) + 'GB'

    def ssd_or_hdd(self):
        """Get a random value from list.

        :return: HDD or SSD.
        :Example:
            512GB SSD.
        """
        return self.random.choice(HDD_SSD)

    def graphics(self):
        """Get a random graphics.

        :return: Graphics.
        :Example:
            Intel® Iris™ Pro Graphics 6200.
        """
        return self.random.choice(GRAPHICS)

    def manufacturer(self):
        """Get a random manufacturer.

        :return: Manufacturer.
        :Example:
            Dell.
        """
        return self.random.choice(MANUFACTURERS)

    def phone_model(self):
        """Get a random phone model.

        :return: Phone model.
        :Example:
            Nokia Lumia 920.
        """
        return self.random.choice(PHONE_MODELS)
