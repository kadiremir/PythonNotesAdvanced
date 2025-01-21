"""Proxy Design Pattern Example 2: Access Control Proxy."""
# The Proxy Design Pattern provides a surrogate or placeholder for another object to control access to it.
# This example demonstrates a simple Access Control Proxy that restricts access to content based on user subscription.
# The ContentProvider class provides access to content, while the ContentProxy class controls access to the ContentProvider.
# The ContentProxy checks the user's subscription before granting access to the content.


class ContentProvider:
    """The Real Subject: Provides access to content."""

    @staticmethod
    def fetch_content(content_id):
        print(f"ContentProvider: Streaming content with ID {content_id}.")


class ContentProxy:
    """The Proxy: Controls access to the ContentProvider."""
    def __init__(self, user_subscription: str):
        self._content_provider = ContentProvider()
        self._user_subscription = user_subscription

    def fetch_content(self, content_id):
        # Check user subscription before granting access
        if self._has_access():
            print(f"Proxy: Access granted to content ID {content_id}.")
            self._content_provider.fetch_content(content_id)
        else:
            print("Proxy: Access denied. Upgrade your subscription!")

    def _has_access(self) -> bool:
        # Simulate access control based on subscription
        return self._user_subscription == "premium"


# Example Usage
def main():
    print("Scenario 1: User with basic subscription:")
    basic_user = ContentProxy(user_subscription="basic")
    basic_user.fetch_content(content_id=101)

    print("\nScenario 2: User with premium subscription:")
    premium_user = ContentProxy(user_subscription="premium")
    premium_user.fetch_content(content_id=101)


main()
