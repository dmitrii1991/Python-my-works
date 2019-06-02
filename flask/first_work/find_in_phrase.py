def find(phrase: str, letters: str):
    let = set()
    for i in list(phrase):
        for x in list(letters):
            if i == x:
                let.add(x)
    return let
