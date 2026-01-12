---
title: "CI/CD Integration"
description: "Integrate Graftcode testing into your CI/CD pipeline with GitHub Actions and GitLab CI examples."
---

## GitHub Actions

`.github/workflows/test.yml`:

```yaml
name: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Start Gateway
      run: |
        npm install -g graftcode-gateway
        gcg.exe --projectKey ${{ secrets.TEST_PROJECT_KEY }} --env TEST --port 9999 &
        sleep 10
    
    - name: Run unit tests
      run: npm run test:unit
    
    - name: Run integration tests
      run: npm run test:integration
      env:
        GRAFTCODE_ENDPOINT: http://localhost:9999
    
    - name: Generate coverage
      run: npm run test:coverage
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
```

## GitLab CI

`.gitlab-ci.yml`:

```yaml
test:
  image: node:18
  services:
    - name: graftcode-gateway
      alias: gateway
  before_script:
    - npm ci
    - npm install -g graftcode-gateway
  script:
    - gcg.exe --projectKey $TEST_PROJECT_KEY --env TEST &
    - sleep 10
    - npm run test:unit
    - npm run test:integration
  coverage: '/Coverage: \d+\.\d+%/'
```
