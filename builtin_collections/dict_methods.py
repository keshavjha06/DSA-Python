# No duplicate keys, but different keys can map to same value.
# Python dicts keep insertion order (Java's HashMap does not).

country_map = {}
country_map["India"] = "New Delhi"
country_map["France"] = "Paris"
country_map["Japan"] = "Tokyo"
print(country_map)
print(country_map["India"])
print("India" in country_map)  # containsKey
print("New Delhi" in country_map.values())  # containsValue
print(len(country_map))
print(country_map.pop("India"))  # New Delhi
print(list(country_map.keys()))  # ['France', 'Japan']
print(list(country_map.values()))  # ['Paris', 'Tokyo']
print(list(country_map.items()))  # [('France', 'Paris'), ('Japan', 'Tokyo')]
print(country_map.get("France", "NONE"))  # Paris

# replace: only updates if the key exists, returns the old value
old_value = None
if "France" in country_map:
    old_value = country_map["France"]
    country_map["France"] = "New York"
print(old_value)  # Paris
print(country_map)
country_map.clear()
print(country_map)
print(len(country_map) == 0)

numbers = {}
numbers[1] = "One"
numbers[2] = "Two"

for key, value in numbers.items():
    print("key:", key, "value:", value)
