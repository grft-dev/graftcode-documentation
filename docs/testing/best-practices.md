---
title: "Testing Best Practices"
description: "Best practices for organizing, maintaining, and optimizing your Graftcode test suite."
---

# Testing Best Practices

## 1. Test Organization

- **Structure**: Organize tests mirroring source code structure
- **Naming**: Use descriptive test names that explain what is being tested
- **Isolation**: Each test should be independent and not rely on others

## 2. Test Data Management

- **Fixtures**: Use test data factories for consistent test data
- **Cleanup**: Always clean up test data after tests
- **Isolation**: Use unique identifiers to avoid conflicts

## 3. Assertions

- **Specific**: Make assertions specific and meaningful
- **Complete**: Test both success and failure cases
- **Readable**: Use custom assertion helpers for complex checks

## 4. Performance

- **Fast**: Keep unit tests fast (< 100ms each)
- **Parallel**: Run tests in parallel when possible
- **Selective**: Use test filters to run only relevant tests during development

## 5. Maintenance

- **Update**: Keep tests updated with code changes
- **Refactor**: Refactor tests along with code
- **Document**: Document complex test scenarios

## 6. Coverage

- **Target**: Aim for 80%+ code coverage
- **Meaningful**: Focus on meaningful coverage, not just numbers
- **Critical**: Ensure 100% coverage for critical paths
