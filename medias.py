from time import sleep
print('bem vindo ao calculador de medias 2000')
n1 = int(input('me diz sua nota do teste por favor: '))
n2 = int(input('me diz sua nota na prova: '))
m= (n1+n2)/2
print('sua media ficou sendo {}'.format(m))
if m>7:
    print('parabens, você foi aprovado')
elif m<5:
    print('desculpa mas você foi reprovado')
elif (7>m>5):
    j=14-m
    print('você esta de recuperação')
    sleep(2)
    print('para passar vc precisa tira {}.'.format(j))
    n3 = float(input('qual foi sua nota da recuperação??: '))
    mp=(m+n3)/2
    if mp > 7:
        print('parabens, você conawguiu ser aprovado')
    elif mp < 5:
        print('desculpa, tentamos ao maximo te ajudar mas você foi reprovado')

