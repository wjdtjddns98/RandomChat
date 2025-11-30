from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(128) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztll1vmzAUhv8K4qqTtiphSRvtjmaZmmlJppZ9qNOEHHCIFbApNkujLv99PgZiPkKUSp"
    "vaSLuD97wHn/OAfXg0I+bjkJ9/4Tjh5jvj0aQowvKiGnhtmCiOtQyCQPNQOdOdZc5Fgjwh"
    "xQUKOZaSj7mXkFgQRqVK0zAEkXnSSGigpZSS+xS7ggVYLHEiAz9+SplQHz9gXtzGK3dBcO"
    "hXCiU+rK10V2xipY2p+KCMsNrc9ViYRlSb441YMrpzEypADTDFCRIYHi+SFMqH6vI2i46y"
    "SrUlK7GU4+MFSkNRavdIBh6jwE9Wk72JAFZ5Y3V7l73B24veQFpUJTvlcpu1p3vPEhWBqW"
    "NuVRwJlDkURs0NXpu6btAbLlGyH185pwZRll6HWCB7VooRenBDTAOxlLf9zgFkX+2b4bV9"
    "c9bvvIJOmPyUsw98mkcsFQKqmmKMOF+zZM832E6xnPN3KBaCxqg34L/g2LUGR4CUrlaSKl"
    "ZF6SUYWnaRaMJ8LyOCRHg/0GpmDamfp54XFy8UsOzBn9Fwk++BA3yd8WR069iTz9BJxPl9"
    "qBDZzggillI3NfXsovYqdg8xvo2dawNujbvZdKQIMi6CRK2ofc6dCTWhVDCXsrWL/NJ2Ld"
    "QCzBaO68WqdPCAMEfeao0S321EmMXavM1QZEV1BVEUqNcCcKHMfHzZOCHect9gyyMHJxvS"
    "nv+j7YRG2y/5QwIlPeFMLqWc5pFs9ftHHMnS1Xokq1j1SIat8QSIuf00AXY7x/wcSFf7TO"
    "s0fg/kigLTPQPt4+1s2jLMdEp9khFPGL+NkPDGpn4ZQA/wg34r46rAdjaxv9eJDj/Nrupz"
    "CB5wJek+62DZ/gH4sTR0"
)
