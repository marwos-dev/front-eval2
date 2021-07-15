def add_link(
        items: list,
        type: str):
    for i in range(len(items)):
        items[i]['link_edit'] = f'{type}/{items[i]["id"]}/edit'
        return items
