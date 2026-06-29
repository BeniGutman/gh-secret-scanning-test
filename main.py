# --- MOCK SECRET FOR GITHUB SECRET SCANNING TEST (NOT A REAL CREDENTIAL) ---
# These are fake AWS credentials used only to verify GitHub secret scanning fires.





AWS_ACCESS_KEY_ID = "AKIAUI5EZDWUKJFC2UVQ"
AWS_SECRET_ACCESS_KEY = "+LtfXhFIXmKYx74MmPxzXBLL3jWbqBu/m/ExdpEQ"


def get_credentials():
    # Same hardcoded mock secret repeated in a second location (still fake).
    access_key = "AKIAUI5EZDWUKJFC2UVQ"
    secret_key = "+LtfXhFIXmKYx74MmPxzXBLL3jWbqBu/m/ExdpEQ"
    return access_key, secret_key


def main():
    print("Hello from test-secret-scanning!")


if __name__ == "__main__":
    main()
