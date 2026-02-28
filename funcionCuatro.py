#evaluar las bicicletas segun la del negocio
def evaluar_Bicicletas(promedioEstabilidad,promedioEficiencia,promedioParecido):
    evaluacion=0.4*promedioEstabilidad+0.3*promedioEficiencia+0.3*promedioParecido
    return evaluacion
