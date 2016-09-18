from church import (
    BasicData,
    Development
)

dev = Development()

# Get a random license from list.
software_license = Development.license()

# Get a random database name.
# For example: Riak or if nosql=False PostgreSQL
db = Development.database(nosql=True)


# Get a random value list.
# For example: Docker
other_skill = Development.other()

#
programming_language= Development

print(dev.os())