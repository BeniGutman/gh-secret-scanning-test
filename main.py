# --- MOCK SECRET FOR GITHUB SECRET SCANNING TEST (NOT A REAL CREDENTIAL) ---
# These are fake AWS credentials used only to verify GitHub secret scanning fires.
AWS_ACCESS_KEY_ID = "AKIAUI5EZDWUKJFC2UVQ"
AWS_SECRET_ACCESS_KEY = "+LtfXhFIXmKYx74MmPxzXBLL3jWbqBu/m/ExdpEQ"


def main():
    print("Hello from test-secret-scanning!")


if __name__ == "__main__":
    main()
