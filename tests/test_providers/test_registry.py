from mimesis import Generic
from mimesis.providers.base import BaseProvider, ProviderRegistry


class TestProviderRegistry:
    def test_provider_registry_has_all_providers(self):
        registered = ProviderRegistry.get_all()
        expected = {
            "address",
            "binaryfile",
            "finance",
            "choice",
            "code",
            "datetime",
            "development",
            "file",
            "food",
            "hardware",
            "internet",
            "numeric",
            "path",
            "payment",
            "person",
            "science",
            "text",
            "transport",
            "cryptographic",
        }

        assert expected.issubset(set(registered.keys()))

    def test_generic_not_in_registry(self):
        registered = ProviderRegistry.get_all()
        assert "generic" not in registered

    def test_provider_registry_get_method(self):
        person_provider = ProviderRegistry.get("person")
        assert person_provider is not None
        assert person_provider.Meta.name == "person"

        non_existent = ProviderRegistry.get("nonexistent")
        assert non_existent is None

    def test_custom_provider_registration(self):
        class CustomProvider(BaseProvider):
            class Meta:
                name = "custom_test_provider"
                auto_register = True

            def custom_method(self):
                return "custom"

        assert "custom_test_provider" in ProviderRegistry.get_all()

        if "custom_test_provider" in ProviderRegistry._providers:
            del ProviderRegistry._providers["custom_test_provider"]

    def test_custom_provider_no_auto_register(self):
        class NoRegisterProvider(BaseProvider):
            class Meta:
                name = "no_register_test"
                auto_register = False

            def some_method(self):
                return "value"

        assert "no_register_test" not in ProviderRegistry.get_all()

    def test_registry_returns_copy(self):
        registry1 = ProviderRegistry.get_all()
        registry2 = ProviderRegistry.get_all()

        assert registry1.keys() == registry2.keys()
        assert registry1 is not registry2


class TestGenericWithRegistry:
    def test_generic_still_works(self, generic):
        assert generic.person.username() is not None
        assert generic.address.city() is not None
        assert generic.numeric.integer_number() is not None

    def test_generic_has_all_providers(self, generic):
        providers = generic.__dir__()

        expected = [
            "address",
            "binaryfile",
            "finance",
            "choice",
            "code",
            "datetime",
            "development",
            "file",
            "food",
            "hardware",
            "internet",
            "numeric",
            "path",
            "payment",
            "person",
            "science",
            "text",
            "transport",
            "cryptographic",
        ]

        for provider in expected:
            assert provider in providers

    def test_custom_provider_with_generic(self):
        class MyProvider(BaseProvider):
            class Meta:
                name = "myprovider_test"
                auto_register = False

            def method(self):
                return 42

        g = Generic()
        g.add_provider(MyProvider)

        assert g.myprovider_test.method() == 42

    def test_generic_initialization_performance(self):
        import time

        start = time.time()
        for _ in range(10):
            _ = Generic()
        elapsed = time.time() - start
        assert elapsed < 0.5

    def test_locale_dependent_providers_lazy_loaded(self, generic):
        assert hasattr(generic, "_person")
        assert isinstance(generic._person, type)

        person = generic.person
        assert person is not None
        assert hasattr(generic, "person")

    def test_locale_independent_providers_eager_loaded(self, generic):
        assert hasattr(generic, "numeric")
        assert not hasattr(generic, "_numeric")
        assert generic.numeric is not None


class TestProviderSynchronization:
    def test_all_providers_in_init_are_in_registry(self):
        from mimesis.providers import __all__

        exported = set(__all__) - {
            "BaseProvider",
            "BaseDataProvider",
            "ProviderRegistry",
            "Generic",
        }

        registered_classes = set()
        for name, cls in ProviderRegistry.get_all().items():
            if cls.__name__ in exported:
                registered_classes.add(cls.__name__)

        assert registered_classes == exported

    def test_no_duplicate_provider_names(self):
        registry = ProviderRegistry.get_all()
        provider_classes = list(registry.values())
        assert len(provider_classes) == len(set(provider_classes))
