BIR_XONALI ={
    '1':'bir',
    '2':'ikki',
    '3':'uch',
    '4':'to\'rt',
    '5':'besh',
    '6':'olti',
    '7':'yetti',
    '8':'sakkiz',
    '9':'to\'qiz',
    '0':'',
}
ON_XONALI ={
    '1':'o\'n',
    '2':'yigirma',
    '3':'o\'ttiz',
    '4':'qirq',
    '5':'ellik',
    '6':'oltmish',
    '7':'yetmish',
    '8':'sakson',
    '9':'to\'qson',
    '0':'',
}
def yuzlar(number):
    l = len(number)
    if l==1:
        BIR_XONALI['0'] = 'no\'l'
        return (str(BIR_XONALI[number]))
    elif l == 2 :
        BIR_XONALI['0'] = ''
        ba = ' '.join([
            ON_XONALI[number[0]],
            BIR_XONALI[number[1]]
            ])
        return (ba.strip())
    else:
        BIR_XONALI['0'] = ''
        if number[0] !='0':
            ba = ' '.join(
                [BIR_XONALI[number[0]],
                'yuz',
                ON_XONALI[number[1]],
                BIR_XONALI[number[2]]])
        else:
            ba = ' '.join(
                [BIR_XONALI[number[0]],
                ON_XONALI[number[1]],
                BIR_XONALI[number[2]]])
        return (ba.strip())

def nts(number):
    bulim:list = []
    while len(number)>0:
        bulim.append(number[-3:])
        number = list(number)
        number[-3:] = ''
        number = ''.join(number)

    if len(bulim)==1:
        return (yuzlar(bulim[0]))
    elif len(bulim)==2:
        return ' '.join([yuzlar(bulim[1]),'ming',yuzlar(bulim[0])])
    elif len(bulim)==3:
        return ' '.join([yuzlar(bulim[2]),'million',yuzlar(bulim[1]),'ming',yuzlar(bulim[0])])
    elif len(bulim)==4:
        return ' '.join([yuzlar(bulim[3]),'milliard',yuzlar(bulim[2]),'million',yuzlar(bulim[1]),'ming',yuzlar(bulim[0])])
    else:
        return ('Error')