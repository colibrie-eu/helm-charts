# Runtime configuration for Sentry

Frontend and Onboarding charts default to `sentry.enabled: false`. To activate
the SDK, provision a namespaced Kubernetes Secret with key `dsn`, then configure
the chart's `sentry.existingSecret`. Both `SENTRY_DSN` and `PUBLIC_SENTRY_DSN`
refer to that key. The SDK must have its own collection limits and event
sanitization; these chart references only supply the ingestion endpoint.

The prepared Staging/Production values use `frontend-sentry` and
`onboarding-sentry`. Create these Secrets before changing the Argo chart pins
to frontend `0.7.21` and onboarding `0.5.7`. The chart refuses enabled Sentry
without a Secret name/key. No DSN or upload token is stored in the values files.

The applications supply their environment and release from the image's version
metadata. Source-map upload credentials are build-only secrets managed by the
shared Docker workflow, never runtime Kubernetes secrets.

`sentry.diagnosticsUntil` optionally supplies the same ISO deadline to server and
browser diagnostics. The prepared values set `2026-10-21T23:59:59Z`, matching the
requested three-week transition. After that deadline, applications keep
reporting errors but remove the temporary richer user/request context. Changing
the deadline is a runtime configuration change and does not require an image rebuild.

Activate Staging first and verify an isolated technical event and its alert.
Then activate Production and read back image readiness, Secret references and a
person-free technical event. Customer login and registration actions are not
required for these probes.
