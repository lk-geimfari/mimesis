import re

import pytest

from mimesis import Science
from mimesis.datasets.int.scientific import SI_PREFIXES, SI_PREFIXES_SYM
from mimesis.enums import MeasureUnit, MetricPrefixSign
from mimesis.exceptions import NonEnumerableError

from .. import patterns


class TestScience:
    @pytest.fixture
    def science(self):
        return Science()

    def test_str(self, science):
        assert re.match(patterns.PROVIDER_STR_REGEX, str(science))

    def test_rna_sequence(self, science):
        result = science.rna_sequence(length=10)
        assert isinstance(result, str)
        assert len(result) == 10

    def test_dna_sequence(self, science):
        result = science.dna_sequence(length=10)
        assert isinstance(result, str)
        assert len(result) == 10

    @pytest.mark.parametrize(
        "name",
        [
            MeasureUnit.MASS,
            MeasureUnit.INFORMATION,
            MeasureUnit.THERMODYNAMIC_TEMPERATURE,
            MeasureUnit.AMOUNT_OF_SUBSTANCE,
            MeasureUnit.ANGLE,
            MeasureUnit.SOLID_ANGLE,
            MeasureUnit.FREQUENCY,
            MeasureUnit.FORCE,
            MeasureUnit.PRESSURE,
            MeasureUnit.ENERGY,
            MeasureUnit.POWER,
            MeasureUnit.ELECTRIC_CHARGE,
            MeasureUnit.VOLTAGE,
            MeasureUnit.ELECTRIC_CAPACITANCE,
            MeasureUnit.ELECTRIC_RESISTANCE,
            MeasureUnit.ELECTRICAL_CONDUCTANCE,
            MeasureUnit.MAGNETIC_FLUX,
            MeasureUnit.MAGNETIC_FLUX_DENSITY,
            MeasureUnit.INDUCTANCE,
            MeasureUnit.TEMPERATURE,
            MeasureUnit.RADIOACTIVITY,
        ],
    )
    def test_measure_unit(self, science, name):
        result = science.measure_unit(name)
        assert result in name.value
        symbol = science.measure_unit(name, symbol=True)
        assert symbol in name.value

    @pytest.mark.parametrize(
        "sign, symbol",
        [
            (MetricPrefixSign.POSITIVE, True),
            (MetricPrefixSign.POSITIVE, False),
            (MetricPrefixSign.NEGATIVE, True),
            (MetricPrefixSign.NEGATIVE, False),
        ],
    )
    def test_prefix(self, science, sign, symbol):
        prefix = science.metric_prefix(sign=sign, symbol=symbol)
        prefixes = SI_PREFIXES_SYM if symbol else SI_PREFIXES
        assert prefix in prefixes[sign.value]
        with pytest.raises(NonEnumerableError):
            science.metric_prefix(sign="nil")


class TestSeededScience:
    @pytest.fixture
    def s1(self, seed):
        return Science(seed=seed)

    @pytest.fixture
    def s2(self, seed):
        return Science(seed=seed)

    def test_rna_sequence(self, s1, s2):
        assert s1.rna_sequence() == s2.rna_sequence()
        assert s1.rna_sequence(length=22) == s2.rna_sequence(length=22)

    def test_dna_sequence(self, s1, s2):
        assert s1.dna_sequence() == s2.dna_sequence()
        assert s1.dna_sequence(length=10) == s2.dna_sequence(length=10)
