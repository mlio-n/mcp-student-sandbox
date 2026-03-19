## Security Risk
A hardcoded AWS secret is present in the codebase and is also printed to stdout, creating a high-risk credential leak path.

## Location
- secret_leak.py:1
- secret_leak.py:3

## Evidence
- AWS_SECRET_KEY = "AKIA_FAKE_KEY_123456789_STUDENT_TEST"
- print(f"Connecting with: {AWS_SECRET_KEY}")

## Impact
- Credential exfiltration from source control history and logs
- Unauthorized cloud access if key is valid
- Potential confidentiality, integrity, and availability compromise

## Severity
Critical (CVSS-style assessment: 9.8)

## Recommended Fix
1. Remove hardcoded secret from source and git history where applicable
2. Rotate/revoke the leaked key immediately
3. Load secrets from environment variables or a secrets manager
4. Never print credentials; use redacted logging
5. Add secret scanning in CI/pre-commit (e.g., gitleaks, detect-secrets)

## Acceptance Criteria
- No plaintext secrets in repository
- No credential values printed in runtime logs
- Secret retrieved from environment or vault
- Secret scanning enabled in CI
