# Who will pay the bill?

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

index = random.randint(0, len(friends) - 1)

print(friends[index])

# Better solution
print(random.choice(friends))
