class movie():
    def script(self):
        print('script')
    def character_list(self):
        print('characters....')

class story_writer(movie):
    def story(self):
        print('manga vols')

class production(movie):
    def actors(self):
        print('acctors')
    def plans(self):
        print('plans...')

class animators(production):
    def animation_staffs(self):
        print('animators')
    def budget(self):
        print('budget')

class distributers(production):
    def merchantise(self):
        print('merch')
    def collabs(self):
        print('collab details')
    def streaming(self):
            print('streaming platform')
    
kishimoto=story_writer()
kishimoto.story()
kishimoto.character_list()

mappa=animators()
mappa.budget()
mappa.character_list()
mappa.actors()

netlflix=distributers()
netlflix.merchantise()
netlflix.collabs()
netlflix.streaming()