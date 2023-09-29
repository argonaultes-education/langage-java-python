class Course:
    
    def __init__(self, category):
        self.category = category
        self.bateaux = set()
        self.match_category = {
            '2x': Bateau2x,
            '2-': Bateau2Pte,
            '1x': BateauSkiff
        }
        self.demarre = False
        self.elapsed_time = 0

    def ajout_bateau_ligne_depart(self, bateau):
        # if bateau.__class__.__name__ == self.match_category[self.category]:
        #     self.bateaux.add(bateau)
        if isinstance(bateau, self.match_category[self.category]):
            self.bateaux.add(bateau)
            print(f'Bateau {bateau} ajouté')
        else:
            print(f'Bateau {bateau} n\'est pas de la bonne catégorie.')


    def depart(self):
        if len(self.bateaux) > 1:
            self.demarre = True

    def en_cours(self):
        return self.demarre

    def next_loop(self):
        # est-ce que la course est toujours en cours Optionnel

        # pour chaque bateau, vérifier que la bateau n'a pas encore parcouru 2 km = 2 000 m
        self.demarre = False
        for bateau in self.bateaux:
            elapsed_distance = (self.elapsed_time * 500) / bateau.get_average_speed()
            if elapsed_distance < 2000:
                self.demarre = True
                self.elapsed_time += 1
                break
        #   avancer si la condition précédente est validée


    def affiche_positions(self):
        print(f'Temps écoulé: {self.elapsed_time}')
        grid_sorted = list(self.bateaux)
        grid_sorted.sort(key=Bateau.get_average_speed, reverse=True)
        for idx, bateau in enumerate(grid_sorted):
            print(f'{idx}: {bateau}')

    def vainqueur_max_gt(self):
        return max(self.bateaux)
    
    def vainqueur(self):
        return max(self.bateaux, key=Bateau.get_average_speed)

    def vainqueur_legacy(self):
        for idx, bateau in enumerate(self.bateaux):
            if idx == 0:
                bateauFast = bateau
            elif bateauFast.average_speed < bateau.average_speed:
                bateauFast = bateau
        return str(bateauFast)

    def run(self):
        self.depart() #changer le statut de la course
        while self.en_cours(): #vérifier le statut de la course
            self.next_loop() #avancer tous les bateaux en fonction de leur vitesse
            self.affiche_positions()
            # affiche le nom du bateau et sa distance parcourue
            # mickey,10
            # minnie,20
            # affiche le nom du plus rapide: minnie
        print(self.bateaux)
        print(self.vainqueur()) # renvoyer le bateau qui a la plus grande vitesse
        print(self.bateaux)


class Bateau:
    
    def __init__(self, rower, average_speed):
        self.rower = rower
        self.average_speed = average_speed

    def get_average_speed(self):
        return self.average_speed
    
    def set_average_speed(self, new_average_speed):
        if (new_average_speed > 0):
            self.average_speed = new_average_speed
        else:
            print('Vitesse négative refusée')

    def __repr__(self):
        return self.rower
    
    def __gt__(self, other):
        return self.average_speed > other.average_speed

class Bateau2x(Bateau):

    def __init__(self, rower, average_speed):
        super().__init__(rower, average_speed)

class Bateau2Pte(Bateau):

    def __init__(self, rower, average_speed):
        super().__init__(rower, average_speed)


class BateauSkiff(Bateau):

    def __init__(self, rower, average_speed):
        super().__init__(rower, average_speed)


if __name__ == '__main__':
    course_cadets = Course('2x')
    bateau_4_2x = Bateau2x('dingo', 80)
    bateau_1_2x = Bateau2x('mickey', 62)
    bateau_2_2x = Bateau2x('minnie', 70)
    bateau_3_skiff = BateauSkiff('picsou', 120)
    course_cadets.ajout_bateau_ligne_depart(bateau_3_skiff)
    course_cadets.ajout_bateau_ligne_depart(bateau_1_2x)
    course_cadets.ajout_bateau_ligne_depart(bateau_2_2x)
    course_cadets.ajout_bateau_ligne_depart(bateau_4_2x)
    # affichage d'un message
    # le bateau n'a pas pu être ajouté
    # mais continue l'exécution de l'application
    course_cadets.run()