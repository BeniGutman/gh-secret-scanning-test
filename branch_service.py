"""Service module added on a feature branch (mock credentials for scanning tests)."""

AWS_ACCESS_KEY_ID = "AKIAQ7XZP3M2VNLD5RTK"
AWS_SECRET_ACCESS_KEY = "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"


def get_branch_credentials():
    return AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


if __name__ == "__main__":
    print(get_branch_credentials())
