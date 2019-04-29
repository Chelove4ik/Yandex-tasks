def get_spn(toponym):
    f_1, f_2 = map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split())
    s_1, s_2 = map(float, toponym['boundedBy']['Envelope']['upperCorner'].split())

    a = str(s_1 - f_1).split('.')
    b = str(s_2 - f_2).split('.')

    spn = ','.join(['.'.join([a[0], a[1][:6]]), '.'.join([b[0], b[1][:6]])])
    return spn
