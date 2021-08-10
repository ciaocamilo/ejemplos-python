def matricularCurso(estudiantes: list) -> str:
    matriculados = 'Identificación\tNombre\tPuntaje\tGrupo\n'
    for estudiante in estudiantes:
        datos_estudiante = ''
        if estudiante[2] >= 0 and estudiante[2] <= 30:
            estudiante.append('A-Principiante')
        elif estudiante[2] >= 31 and estudiante[2] <= 70:
            estudiante.append('B-Intermedio')
        elif estudiante[2] >= 71 and estudiante[2] <= 100:
            estudiante.append('C-Avanzado')
        for dato in estudiante:
            datos_estudiante += f'{dato}\t'
        matriculados += f'\n{datos_estudiante[:-1]}'
    return matriculados

print(matricularCurso([['1110033495', 'Violeta Murcia', 63], ['1110783206', 'Claudia Gallego', 77], ['1110953217', 'Manuel Gonzalez', 45]]))