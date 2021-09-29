palavras = ["caracteres", "prescindir", "diligência", "intempérie", "corroborar",
"incipiente", "referência", "presunçoso", "intrínseco", "VerDadeiro"]
for x in palavras:
    print(f'\nNa palavra {x} estão ', end='')
    for consoantes in x:
        if consoantes.lower() in 'bcdfgjklmnpqrstvwxz':
            print(consoantes.lower(), end='')