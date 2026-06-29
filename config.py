# --- MOCK SECRET FOR GITHUB SECRET SCANNING TEST (NOT A REAL CREDENTIAL) ---






# Same fake AWS credentials as main.py, duplicated in a second file to test
# how GitHub secret scanning reports the same secret across multiple locations.
AWS_ACCESS_KEY_ID = "AKIAUI5EZDWUKJFC2UVQ"
AWS_SECRET_ACCESS_KEY = "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"


def load_config():
    return {
        "aws_access_key_id": AWS_ACCESS_KEY_ID,
        "aws_secret_access_key": AWS_SECRET_ACCESS_KEY,
    }
