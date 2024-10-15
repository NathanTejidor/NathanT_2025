import json

# Sample JSON data
json_data = '''{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "email": "alice@example.com",
      "active": true,
      "tags": ["friend", "developer"]
    },
    {
      "id": 2,
      "name": "Bob",
      "email": "bob@example.com",
      "active": false,
      "tags": ["friend", "designer"]
    }
  ]
}'''

# Load the JSON data
data = json.loads(json_data)

# 1. Accessing and printing a string variable
print(data['users'][0]['name'])  # Output: Alice

# 2. Updating a boolean variable
data['users'][1]['active'] = True

# 3. Adding a new number variable
data['users'][0]['age'] = 30

# 4. Appending a new string to the tags array
data['users'][1]['tags'].append("artist")

# 5. Adding a new user (dictionary variable)
new_user = {
    "id": 3,
    "name": "Charlie",
    "email": "charlie@example.com",
    "active": True,
    "tags": ["new", "friend"]
}
data['users'].append(new_user)

# Convert back to JSON string
updated_json_data = json.dumps(data, indent=2)
print(updated_json_data)
