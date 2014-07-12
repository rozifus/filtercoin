

def model_item(**kw):
    item = {}
    item['id'] = kw.get("id") or "Item"
    item['name'] = kw.get("name") or "Name"
    item['alias'] = kw.get("alias") or []
    item['sub'] = kw.get("sub") or []


