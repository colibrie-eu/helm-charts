# Helm Charts

## Add

```
$ helm repo add colibrie-eu https://colibrie-eu.github.io/helm-charts
```

## Update

```
$ helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "colibrie-eu" chart repository
```

## Search

```
$ helm search repo colibrie-eu
NAME                    CHART VERSION   APP VERSION     DESCRIPTION
colibrie-eu/onboarding  0.1.0           1.16.0          A Helm chart for colibrie's onboarding process
```
## Install

```
$ helm upgrade --install onboarding colibrie-eu/onboarding --version 0.1.0
Release "onboarding" does not exist. Installing it now.
NAME: onboarding
LAST DEPLOYED: Fri Mar 14 09:26:58 2025
NAMESPACE: production
STATUS: deployed
REVISION: 1
NOTES:
1. Get the application URL by running these commands:
  https://onboarding.colibrie.eu/
```
