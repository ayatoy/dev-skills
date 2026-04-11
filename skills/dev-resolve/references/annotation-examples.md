# Annotation Examples

Use the lightest style that matches the source document.

## Bullet Question

Question:
- Should retries happen before or after the token refresh?

Suggested annotation:
- Inferred answer: Retry after refresh to avoid replaying an already-invalid token.
- Confidence: medium
- Basis: The surrounding auth flow refreshes tokens before retrying other failures.

## Inline Prose Question

Question:
Should this command remain synchronous?

Suggested annotation:
Proposed answer: Keep it synchronous for now because later steps depend on immediate file output (inference, confidence: low).
