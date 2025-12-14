from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "login_id" VARCHAR(255) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "nickname" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(128) NOT NULL,
    "birthday" DATE,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "admin" BOOL NOT NULL DEFAULT False
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";"""


MODELS_STATE = (
    "eJztl21P2zAQx79KlVdMYqh0PIl3LXSiE20nCNsEQpEbu4lVxw6xM6gQ3x2fkzQPTat2og"
    "OkvnP/d5fc/c6Nz89WIDBhcu9GkqgPS+u08WxxFBC9mDfuNiwUhrkJBIVGzHjH2s14jKSK"
    "kKu0NkZMEi1hIt2IhooKrlUeMwaicLUj5V4uxZw+xMRRwiPK1087bdzda5lyTJ6IzH6GE2"
    "dMCcOlXCmGdxvdUdPQaD2uvhtHeNvIcQWLA547h1PlCz7zplyB6hFOIqQIPF5FMaQP2aVV"
    "ZhUlmeYuSYqFGEzGKGaqUO6KDFzBgZ/ORpoCPXjL19b+wfHBybejgxPtYjKZKccvSXl57U"
    "mgITCwrRdjRwolHgZjzo0Jj3Knjt6Zj6J6fMWYCkSdehVihuxdKQboyWGEe8oHdIeHS5j9"
    "al+dXbSvdrTXF6hF6M2c7PBBamolNgCbgyQBomwdirOALcIUIafuxKzXoFiM2YJMQfpI+g"
    "Q7IZLyUURr/bdrQt8GaybkXPPTYRNg91snK4DVXgvBGlsZ7IhGysdoOk/0XKOoJ1qMqaDU"
    "X2WiaED2YLEC1HQn/kemSxCet+1uBY8bEUjeQaoeENRaD6kcuQwTLD7o/tM14CFn07RTS9"
    "jZvX732m73f0IlgZQPLCMKlpZRpxV156iyU2cPafzu2RcN+Nm4HQ66hqCQyovMG3M/+9aC"
    "nFCshMPFo4Nw4fOWqRmYUmPjEP9jY8uR28a+a2PT5PO+IhxQPt/SjhCMIF7f0VlMpZkjHb"
    "Sp/q17kVj9K9YZDi9Lver07MqBcNPvdPVJYZqknahKLhdmtIb7yHhSmKxBGCF38ogi7MxZ"
    "REss8p03Ba2gqiCOPIMI6oSq0itam0TU9a2ay1tq2V12c0O5z/bu9pbfjQ3f3f6SSEJKa4"
    "x3hZDPOdZtZF6Gv8YaEFP3zwlwv9lcZS5uNhfPxWCrDH6CK8JrhoMf18PBgokvD6mAvOG6"
    "wDtMXbXbYFSq+4+JdQlFqLp0qGTwdvrtP1WuZ5fDTvVkhwd03vt4eXkFps9tYA=="
)
