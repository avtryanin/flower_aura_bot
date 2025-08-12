def format_products(products, show_quantity=False):
    if not products:
        return None
    lines = []
    for p in products:
        if show_quantity:
            lines.append(f"{p.id}. {p.name} — {p.price}₽ ({p.quantity} шт.)")
        else:
            lines.append(f"{p.id}. {p.name} — {p.price}₽")
    return "\n".join(lines)
