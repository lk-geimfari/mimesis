"""Tests for mimesis.builder.SchemaBuilder."""

from __future__ import annotations

import pytest

from mimesis import SchemaBuilder, SchemaRef
from mimesis.builder import SchemaBuilder as BuilderFromPackage
from mimesis.builder.resolver import (
    FieldRef,
    LazyChoice,
    LazyField,
    LazyWeightedChoice,
    NestedSchema,
    SchemaRefProxy,
)
from mimesis.enums import TimestampFormat
from mimesis.locales import Locale


SEED = 0xFF


@pytest.fixture
def sb() -> SchemaBuilder:
    return SchemaBuilder(Locale.EN, seed=SEED)


class TestExports:
    def test_public_export_is_builder(self) -> None:
        assert SchemaBuilder is BuilderFromPackage
        assert SchemaBuilder.__module__ == "mimesis.builder.core"

    def test_schema_ref_exported(self) -> None:
        assert SchemaRef.__module__ == "mimesis.builder.schema"


class TestLazyPrimitives:
    def test_f_returns_lazy_field(self, sb: SchemaBuilder) -> None:
        field = sb.f("username")
        assert isinstance(field, LazyField)
        assert "LazyField" in repr(field)

    def test_choice_returns_lazy_choice(self, sb: SchemaBuilder) -> None:
        choice = sb.choice(["a", "b"])
        assert isinstance(choice, LazyChoice)

    def test_weighted_choice_returns_lazy(self, sb: SchemaBuilder) -> None:
        weighted = sb.weighted_choice(["a", "b"], [0.5, 0.5])
        assert isinstance(weighted, LazyWeightedChoice)

    def test_choice_rejects_empty(self, sb: SchemaBuilder) -> None:
        with pytest.raises(ValueError, match="empty"):
            sb.choice([])

    def test_weighted_choice_length_mismatch(self, sb: SchemaBuilder) -> None:
        with pytest.raises(ValueError, match="same length"):
            sb.weighted_choice(["a", "b"], [1.0])

    def test_weighted_choice_empty(self, sb: SchemaBuilder) -> None:
        with pytest.raises(ValueError, match="empty"):
            sb.weighted_choice([], [])


class TestBasicGeneration:
    def test_quick_start_example(self) -> None:
        sb = SchemaBuilder(Locale.EN, seed=SEED)

        users = sb.schema(
            "users",
            {
                "id": sb.f("increment"),
                "name": sb.f("full_name"),
                "email": sb.f("email"),
            },
        )

        posts = sb.schema(
            name="posts",
            schema={
                "id": sb.f("increment"),
                "title": sb.f("sentence", key=str.lower),
                "user_id": sb.ref(users).id,
            },
        )

        data = sb.create(users=10, posts=50)

        assert len(data["users"]) == 10
        assert len(data["posts"]) == 50
        assert isinstance(posts, SchemaRef)

        user_ids = {u["id"] for u in data["users"]}
        assert user_ids == set(range(1, 11))

        for post in data["posts"]:
            assert post["user_id"] in user_ids
            assert post["title"] == post["title"].lower()

    def test_nested_dicts(self, sb: SchemaBuilder) -> None:
        sb.schema(
            "users",
            {
                "id": sb.f("increment"),
                "profile": {
                    "bio": sb.f("text"),
                    "meta": {
                        "city": sb.f("city"),
                    },
                },
            },
        )

        data = sb.create(users=3)
        for user in data["users"]:
            assert isinstance(user["profile"]["bio"], str)
            assert isinstance(user["profile"]["meta"]["city"], str)

    def test_choice_and_weighted_choice(self, sb: SchemaBuilder) -> None:
        statuses = ["draft", "published", "archived"]
        rarities = ["common", "rare", "legendary"]

        sb.schema(
            "items",
            {
                "status": sb.choice(statuses),
                "rarity": sb.weighted_choice(rarities, [0.7, 0.25, 0.05]),
            },
        )

        data = sb.create(items=100)
        for item in data["items"]:
            assert item["status"] in statuses
            assert item["rarity"] in rarities

    def test_choice_resolves_nested_lazy_values(self, sb: SchemaBuilder) -> None:
        sb.schema(
            "rows",
            {
                "notes": sb.choice([None, sb.f("sentence")]),
                "stamp": sb.choice(
                    [None, sb.f("timestamp", fmt=TimestampFormat.ISO_8601)]
                ),
                "nested": sb.choice(
                    [
                        {"ok": True},
                        {"label": sb.f("word")},
                    ]
                ),
            },
        )

        data = sb.create(rows=50)
        for row in data["rows"]:
            assert row["notes"] is None or isinstance(row["notes"], str)
            assert row["stamp"] is None or isinstance(row["stamp"], str)
            assert isinstance(row["nested"], dict)
            if "label" in row["nested"]:
                assert isinstance(row["nested"]["label"], str)

    def test_key_and_provider_kwargs(self, sb: SchemaBuilder) -> None:
        sb.schema(
            "rows",
            {
                "name": sb.f("name", key=str.upper),
                "n": sb.f("integer_number", start=1, end=5),
                "email": sb.f("person.email", domains=["example.com"]),
                "ts": sb.f("timestamp", fmt=TimestampFormat.ISO_8601),
            },
        )

        data = sb.create(rows=20)
        for row in data["rows"]:
            assert row["name"] == row["name"].upper()
            assert 1 <= row["n"] <= 5
            assert row["email"].endswith("@example.com")
            assert "T" in row["ts"]

    def test_lists_and_tuples_in_schema(self, sb: SchemaBuilder) -> None:
        sb.schema(
            "docs",
            {
                "tags": [sb.f("word"), sb.f("word")],
                "pair": (sb.choice([1, 2]), sb.choice([3, 4])),
                "literal": "fixed",
            },
        )

        data = sb.create(docs=5)
        for doc in data["docs"]:
            assert len(doc["tags"]) == 2
            assert isinstance(doc["pair"], tuple)
            assert doc["pair"][0] in (1, 2)
            assert doc["pair"][1] in (3, 4)
            assert doc["literal"] == "fixed"

    def test_reproducible_with_seed(self) -> None:
        def build() -> dict:
            sb = SchemaBuilder(Locale.EN, seed=42)
            sb.schema(
                "users",
                {
                    "id": sb.f("increment"),
                    "email": sb.f("email"),
                    "status": sb.choice(["a", "b", "c"]),
                },
            )
            return sb.create(users=5)

        assert build() == build()


class TestForeignKeys:
    def test_field_ref(self, sb: SchemaBuilder) -> None:
        users = sb.schema("users", {"id": sb.f("increment")})
        ref = sb.ref(users).id
        assert isinstance(ref, FieldRef)

        posts = sb.schema("posts", {"user_id": ref})
        data = sb.create(users=3, posts=10)

        assert isinstance(posts, SchemaRef)
        user_ids = {u["id"] for u in data["users"]}
        assert all(p["user_id"] in user_ids for p in data["posts"])

    def test_whole_record_ref(self, sb: SchemaBuilder) -> None:
        users = sb.schema(
            "users",
            {
                "id": sb.f("increment"),
                "name": sb.f("full_name"),
            },
        )
        proxy = sb.ref(users)
        assert isinstance(proxy, SchemaRefProxy)

        posts = sb.schema(
            "posts",
            {
                "title": sb.f("title"),
                "author": proxy,
            },
        )

        data = sb.create(users=4, posts=8)
        assert isinstance(posts, SchemaRef)
        users_by_id = {u["id"]: u for u in data["users"]}

        for post in data["posts"]:
            author = post["author"]
            assert author == users_by_id[author["id"]]

    def test_dependency_order_independent_of_create_kwargs(
        self, sb: SchemaBuilder
    ) -> None:
        users = sb.schema("users", {"id": sb.f("increment")})
        posts = sb.schema(
            "posts",
            {
                "id": sb.f("increment"),
                "user_id": sb.ref(users).id,
            },
        )
        comments = sb.schema(
            "comments",
            {
                "post_id": sb.ref(posts).id,
                "user_id": sb.ref(users).id,
            },
        )

        data = sb.create(comments=20, posts=5, users=3)

        assert isinstance(comments, SchemaRef)
        user_ids = {u["id"] for u in data["users"]}
        post_ids = {p["id"] for p in data["posts"]}

        assert all(p["user_id"] in user_ids for p in data["posts"])
        assert all(c["user_id"] in user_ids for c in data["comments"])
        assert all(c["post_id"] in post_ids for c in data["comments"])

    def test_multi_level_fk_chain(self, sb: SchemaBuilder) -> None:
        users = sb.schema(
            "users",
            {"id": sb.f("increment"), "email": sb.f("email")},
        )
        posts = sb.schema(
            "posts",
            {
                "id": sb.f("increment"),
                "author_id": sb.ref(users).id,
                "title": sb.f("title"),
            },
        )
        comments = sb.schema(
            "comments",
            {
                "id": sb.f("increment"),
                "post_id": sb.ref(posts).id,
                "user_id": sb.ref(users).id,
                "body": sb.f("text"),
            },
        )

        data = sb.create(comments=30, users=3, posts=10)

        assert isinstance(comments, SchemaRef)
        user_ids = {u["id"] for u in data["users"]}
        post_ids = {p["id"] for p in data["posts"]}

        assert all(p["author_id"] in user_ids for p in data["posts"])
        assert all(c["post_id"] in post_ids for c in data["comments"])
        assert all(c["user_id"] in user_ids for c in data["comments"])

    def test_ref_requires_schema_ref(self, sb: SchemaBuilder) -> None:
        with pytest.raises(TypeError, match="SchemaRef"):
            sb.ref("users")  # type: ignore[arg-type]


class TestNesting:
    def test_nested_schema_count(self, sb: SchemaBuilder) -> None:
        addresses = sb.schema(
            "addresses",
            {
                "city": sb.f("city"),
                "street": sb.f("street_name"),
            },
        )
        nested = addresses(count=3)
        assert isinstance(nested, NestedSchema)

        companies = sb.schema(
            "companies",
            {
                "id": sb.f("increment"),
                "name": sb.f("company"),
                "offices": nested,
            },
        )

        data = sb.create(companies=5)
        assert isinstance(companies, SchemaRef)

        for company in data["companies"]:
            assert len(company["offices"]) == 3
            for office in company["offices"]:
                assert "city" in office
                assert "street" in office

    def test_deep_nesting(self, sb: SchemaBuilder) -> None:
        tags = sb.schema("tags", {"name": sb.f("word")})
        sections = sb.schema(
            "sections",
            {
                "heading": sb.f("title"),
                "tags": tags(count=2),
            },
        )
        articles = sb.schema(
            "articles",
            {
                "title": sb.f("title"),
                "sections": sections(count=2),
            },
        )

        data = sb.create(articles=3)
        assert isinstance(articles, SchemaRef)

        for article in data["articles"]:
            assert len(article["sections"]) == 2
            for section in article["sections"]:
                assert len(section["tags"]) == 2
                assert all("name" in tag for tag in section["tags"])

    def test_nesting_count_must_be_positive(self, sb: SchemaBuilder) -> None:
        tags = sb.schema("tags", {"name": sb.f("word")})
        with pytest.raises(ValueError, match="count"):
            tags(count=0)

    def test_circular_nesting_raises(self, sb: SchemaBuilder) -> None:
        nodes = sb.schema("nodes", {"label": sb.f("word")})
        # Mutate definition after creation to introduce self-nesting
        sb._schemas["nodes"]["children"] = nodes(count=1)
        nodes._definition["children"] = nodes(count=1)

        with pytest.raises(ValueError, match="Circular nesting"):
            sb.create(nodes=1)

    def test_bare_schema_ref_raises(self, sb: SchemaBuilder) -> None:
        users = sb.schema("users", {"id": sb.f("increment")})
        sb.schema("posts", {"author": users})

        with pytest.raises(TypeError, match="Bare SchemaRef"):
            sb.create(posts=1, users=1)


class TestErrors:
    def test_undefined_schema(self, sb: SchemaBuilder) -> None:
        sb.schema("users", {"id": sb.f("increment")})

        with pytest.raises(ValueError, match="not defined"):
            sb.create(users=1, posts=1)

    def test_missing_dependency(self, sb: SchemaBuilder) -> None:
        users = sb.schema("users", {"id": sb.f("increment")})
        sb.schema("posts", {"user_id": sb.ref(users).id})

        with pytest.raises(ValueError, match="not yet generated"):
            sb.create(posts=5)

    def test_missing_field_on_ref(self, sb: SchemaBuilder) -> None:
        users = sb.schema("users", {"id": sb.f("increment")})
        sb.schema("posts", {"name": sb.ref(users).missing})

        with pytest.raises(KeyError, match="missing"):
            sb.create(users=1, posts=1)

    def test_circular_fk_dependency(self, sb: SchemaBuilder) -> None:
        a = sb.schema("a", {"id": sb.f("increment")})
        b = sb.schema("b", {"a_id": sb.ref(a).id})
        # overwrite a to depend on b — create circular FK graph
        sb._schemas["a"] = {"id": sb.f("increment"), "b_id": sb.ref(b).id}
        sb._dependencies["a"] = {"b"}
        sb._dependencies["b"] = {"a"}

        with pytest.raises(ValueError, match="Circular dependency"):
            sb.create(a=1, b=1)

    def test_negative_count(self, sb: SchemaBuilder) -> None:
        sb.schema("users", {"id": sb.f("increment")})
        with pytest.raises(ValueError, match="Count"):
            sb.create(users=-1)


class TestLifecycle:
    def test_clear_keeps_schemas(self, sb: SchemaBuilder) -> None:
        sb.schema("users", {"id": sb.f("increment")})
        first = sb.create(users=2)
        sb.clear()
        second = sb.create(users=2)

        assert first["users"][0]["id"] == 1
        # increment continues after clear because Field state is preserved
        assert second["users"][0]["id"] == 3

    def test_reset_clears_schemas(self, sb: SchemaBuilder) -> None:
        sb.schema("users", {"id": sb.f("increment")})
        sb.create(users=1)
        sb.reset()

        with pytest.raises(ValueError, match="not defined"):
            sb.create(users=1)

    def test_reseed_changes_output(self, sb: SchemaBuilder) -> None:
        sb.schema(
            "users",
            {
                "email": sb.f("email"),
                "status": sb.choice(["a", "b", "c", "d", "e"]),
            },
        )
        first = sb.create(users=5)
        sb.reseed(12345)
        second = sb.create(users=5)
        assert first != second

    def test_repr(self, sb: SchemaBuilder) -> None:
        sb.schema("users", {"id": sb.f("increment")})
        text = repr(sb)
        assert "SchemaBuilder" in text
        assert "users" in text


class TestComplexSchemas:
    def test_ecommerce_domain(self, sb: SchemaBuilder) -> None:
        categories = sb.schema(
            "categories",
            {
                "id": sb.f("increment"),
                "name": sb.f("word", key=str.title),
                "slug": sb.f("slug"),
            },
        )

        products = sb.schema(
            "products",
            {
                "id": sb.f("increment"),
                "sku": sb.f("uuid"),
                "name": sb.f("title"),
                "price": sb.f("price", minimum=1.0, maximum=500.0),
                "category_id": sb.ref(categories).id,
                "status": sb.weighted_choice(
                    ["active", "draft", "archived"],
                    [0.7, 0.2, 0.1],
                ),
                "attributes": {
                    "color": sb.choice(["red", "green", "blue", "black"]),
                    "weight_g": sb.f("integer_number", start=50, end=5000),
                },
            },
        )

        customers = sb.schema(
            "customers",
            {
                "id": sb.f("increment"),
                "email": sb.f("email"),
                "full_name": sb.f("full_name"),
                "addresses": sb.schema(
                    "addresses",
                    {
                        "city": sb.f("city"),
                        "street": sb.f("street_name"),
                        "zip": sb.f("zip_code"),
                    },
                )(count=2),
            },
        )

        orders = sb.schema(
            "orders",
            {
                "id": sb.f("increment"),
                "customer_id": sb.ref(customers).id,
                "status": sb.choice(
                    ["pending", "paid", "shipped", "cancelled"]
                ),
                "total": sb.f("price", minimum=10.0, maximum=2000.0),
            },
        )

        order_items = sb.schema(
            "order_items",
            {
                "id": sb.f("increment"),
                "order_id": sb.ref(orders).id,
                "product_id": sb.ref(products).id,
                "quantity": sb.f("integer_number", start=1, end=5),
            },
        )

        data = sb.create(
            order_items=40,
            orders=10,
            products=15,
            customers=5,
            categories=4,
        )

        category_ids = {c["id"] for c in data["categories"]}
        product_ids = {p["id"] for p in data["products"]}
        customer_ids = {c["id"] for c in data["customers"]}
        order_ids = {o["id"] for o in data["orders"]}

        assert all(p["category_id"] in category_ids for p in data["products"])
        assert all(o["customer_id"] in customer_ids for o in data["orders"])
        assert all(i["order_id"] in order_ids for i in data["order_items"])
        assert all(i["product_id"] in product_ids for i in data["order_items"])

        for customer in data["customers"]:
            assert len(customer["addresses"]) == 2
            for address in customer["addresses"]:
                assert address["city"]
                assert address["street"]
                assert address["zip"]

        for product in data["products"]:
            assert product["status"] in {"active", "draft", "archived"}
            assert product["attributes"]["color"] in {
                "red",
                "green",
                "blue",
                "black",
            }
            assert 50 <= product["attributes"]["weight_g"] <= 5000

    def test_blog_with_mixed_refs_and_nesting(self, sb: SchemaBuilder) -> None:
        authors = sb.schema(
            "authors",
            {
                "id": sb.f("increment"),
                "username": sb.f("username"),
                "profile": {
                    "bio": sb.f("text"),
                    "avatar": sb.f("stock_image_url"),
                },
            },
        )

        tags = sb.schema(
            "tags",
            {
                "id": sb.f("increment"),
                "name": sb.f("word", key=str.lower),
            },
        )

        posts = sb.schema(
            "posts",
            {
                "id": sb.f("increment"),
                "author_id": sb.ref(authors).id,
                "author": sb.ref(authors),
                "title": sb.f("title"),
                "body": sb.f("text"),
                "tags": tags(count=3),
                "status": sb.choice(["draft", "published"]),
                "meta": {
                    "views": sb.f("integer_number", start=0, end=10000),
                    "featured": sb.choice([True, False]),
                },
            },
        )

        comments = sb.schema(
            "comments",
            {
                "id": sb.f("increment"),
                "post_id": sb.ref(posts).id,
                "author_id": sb.ref(authors).id,
                "body": sb.f("text"),
            },
        )

        data = sb.create(comments=25, posts=8, authors=4, tags=6)

        author_ids = {a["id"] for a in data["authors"]}
        post_ids = {p["id"] for p in data["posts"]}
        authors_by_id = {a["id"]: a for a in data["authors"]}

        for post in data["posts"]:
            assert post["author_id"] in author_ids
            assert post["author"] == authors_by_id[post["author"]["id"]]
            assert len(post["tags"]) == 3
            assert all(tag["name"] == tag["name"].lower() for tag in post["tags"])

        for comment in data["comments"]:
            assert comment["post_id"] in post_ids
            assert comment["author_id"] in author_ids

        # tags was also requested as top-level generation
        assert len(data["tags"]) == 6
