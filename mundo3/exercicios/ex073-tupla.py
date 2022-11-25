times = ('Atlético-GO','Atlético-MG','Athletico-PR',
        'Avaí','Botafogo','Internacional','Bragantino',
        'Ceará','Corinthians','Palmeiras','Juventude',
        'Coritiba','América-MG','Santos','São Paulo',
        'Athletico','Cuiabá','Flamengo','Fluminense',
        'Goiás','Fortaleza'
        )
print('-='*15)
print(f'{times}')
print('-='*15)
print(f'Os 5 primeiros times são : {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*15)
print(f'Os times em Ordem alfabética são: {sorted(times)}')
print('-='*15)
print(f' A posição do Ceará é a de {times.index("Corinthians")}ª  ')#usar aspas duplas ou .format() pois estava '' dentro de ''



""" for time in times:
    print(time) """
