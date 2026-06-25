import secrets
import string

# --- MOCK SECRET FOR GITHUB SECRET SCANNING TEST (NOT A REAL CREDENTIAL) ---
# A DIFFERENT set of fake AWS credentials than main.py/config.py, used to test
# how GitHub secret scanning reports multiple distinct secrets in one repo.
AWS_ACCESS_KEY_ID = "AKIAKHLY6NRDDPXMUXKK"
AWS_SECRET_ACCESS_KEY = "gSBSNF2T3PlNJVWn0Gn5oWvlge4coO3Be9aWkqD6"


def get_util_credentials():
    # Same distinct mock secret repeated locally (still fake).
    access_key = "AKIAKHLY6NRDDPXMUXKK"
    secret_key = "gSBSNF2T3PlNJVWn0Gn5oWvlge4coO3Be9aWkqD6"
    return access_key, secret_key


def generate_fake_aws_credentials():
    """Generate format-shaped (but fake/random) AWS credentials.

    This is the generator used to produce the mock values above. The output
    matches AWS's credential format but carries no valid checksum and is not
    tied to any real account — it exists only to exercise secret scanning.
    """
    b32 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    b64 = string.ascii_letters + string.digits + "+/"
    access_key = "AKIA" + "".join(secrets.choice(b32) for _ in range(16))
    secret_key = "".join(secrets.choice(b64) for _ in range(40))
    return access_key, secret_key
