from growth_engine import mom_growth, is_flagged


data = {
    "Ethnic Wear": (185107.61, 76371.53),
    "Western Wear": (86998.18, 97415.64),
    "Kids Wear": (45793.78, 56737.78),
    "Home & Kitchen": (91152.57, 129971.22),
    "Beauty & Personal Care": (35542.11, 37559.07)
}


print("May vs April")
print("-" * 50)

for category, (previous, current) in data.items():
    growth = mom_growth(previous, current)
    status = is_flagged(growth)

    print(
        f"{category}: {growth}% -> {status}"
    )