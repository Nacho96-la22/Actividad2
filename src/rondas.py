roundsGlobals = {
    'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'score': 0},
    'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'score': 0},
    'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'score': 0},
    'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'score': 0},
    'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'MVP': 0, 'score': 0}
}

# Calcular en la estadistica
def calcularEstadistica(stats):
    pointKill = stats['kills']*3
    pointAssist = stats['assists']*1
    pointDeath = int(stats['deaths'])*1
    return pointKill, pointAssist, pointDeath

# Puntos por ronda
def rondaPorPuntaje(pointKill, pointAssist, pointDeath):
    puntajePorRonda = pointKill + pointAssist - pointDeath
    return puntajePorRonda

# Sumatorio en los jugadores por ranking globals
def calcularEstadisticaGlobals(jugador,kill,assist,death,puntaje):
    roundsGlobals[jugador]['kills'] += kill
    roundsGlobals[jugador]['assists'] += assist
    roundsGlobals[jugador]['deaths'] += death
    roundsGlobals[jugador]['score'] += puntaje
    return roundsGlobals

# Imprimir los jugadores por ronda
def toStringPorRonda(jugadores_puntos,actualMVP):
    for jugador,estadistica,puntaje in jugadores_puntos:
        print(f"{jugador}: {estadistica} | {puntaje}")
    print(f"- MVP de la ronda: {actualMVP}")
    print("-"*55)

# Imprimir los jugadores por ranking globals
def toStringRankingGlobals(rankingGlobals):
    print("> Ranking final:")
    print(f"{'Jugador':<10}  {'Kills':<6}   {'Assists':<6}  {'Deaths':<6}   {'MVP':<5}   {'Score':<5}")
    print("-"*55)
    for jugador,stats in rankingGlobals:
        print(f"{jugador:<10} | {stats['kills']:<6} | {stats['assists']:<6} | {stats['deaths']:<6} | {stats['MVP']:<6}| {stats['score']:<6}|")
    print("-"*55)

def rondas_data(rounds):
    for num_round,round in enumerate(rounds):
        print(f"> Round {num_round+1}:")

        # Para ordena los jugadores por puntos en una ronda
        jugadores_puntos = []
        # Jugadores
        for jugador,stats in round.items():
            # Calcular en la estadistica
            kill, assist, death = calcularEstadistica(stats)
            
            # Puntos por ronda
            puntaje = rondaPorPuntaje(kill,assist,death)
            # Guardar la estadistica del jugador en la lista de ordenada
            jugadores_puntos.append((jugador,stats,puntaje))

            # Actualizar la estadistica de global
            roundsGlobals=calcularEstadisticaGlobals(jugador,kill,assist,death,puntaje)

        # Ordena por los puntos en una ronda
        jugadores_puntos.sort(key=lambda x:x[2],reverse= True)            

        # Actual MVP
        actualMVP = jugadores_puntos[0][0]
        roundsGlobals[actualMVP]['MVP'] += 1
        
        # Imprimr los jugadores por una ronda
        toStringPorRonda(jugadores_puntos,actualMVP)
    
    # Ordena por ranking globals
    rankingGlobals = sorted(roundsGlobals.items(),key=lambda x:x[1]['score'],reverse= True)
    # Imprimr los jugadores por ranking globals
    toStringRankingGlobals(rankingGlobals)

    return rounds