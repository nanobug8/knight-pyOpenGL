class Conf:

    def __init__(self, filename):

        self.path = ''
        self.attack = []
        self.walk = []
        self.fallback = []
        self.model1 = ''
        self.tex1 = ''
        self.tex2 = ''
        self.step_sound = ''
        self.attack_sound = ''
        self.width = 0
        self.height = 0
        self.sback = ''
        self.svoy = ''
        self.light_position = []
        self.light_ambient = []
        self.light_diffuse = []
        
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'p':
                self.path = values[1]
            elif values[0] == 'a':
                self.attack.append(values[1])
            elif values[0] == 'w':
                self.walk.append(values[1])
            elif values[0] == 'w1':
                self.fallback.append(values[1])
            elif values[0] == 'm1':
                self.model1 = values[1]
            elif values[0] == 't1':
                self.tex1 = values[1]
            elif values[0] == 't2':
                self.tex2 = values[1]
            elif values[0] == 'ss':
                self.step_sound = values[1]
            elif values[0] == 'ks':
                self.attack_sound = values[1]
            elif values[0] == 'sback':
                self.sound_back = values[1]
            elif values[0] == 'svoy':
                self.sound_voy = values[1]
            elif values[0] == 'width':
                self.width = int(values[1])
            elif values[0] == 'height':
                self.height = int(values[1])
            elif values[0] == 'GL_POSITION':
                self.light_position.append(values[0])
                self.light_position.append(values[1])
                self.light_position.append(values[2])
                self.light_position.append(values[3])
                self.light_position.append(values[4])                
            elif values[0] == 'GL_AMBIENT':
                self.light_ambient.append(values[0])
                self.light_ambient.append(values[1])
                self.light_ambient.append(values[2])
                self.light_ambient.append(values[3])
                self.light_ambient.append(values[4])
            elif values[0] == 'GL_DIFFUSE':
                self.light_diffuse.append(values[0])
                self.light_diffuse.append(values[1])
                self.light_diffuse.append(values[2])
                self.light_diffuse.append(values[3])
                self.light_diffuse.append(values[4])
                  
