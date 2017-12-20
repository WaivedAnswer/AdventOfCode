#day20
import math
class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        
def GetCoordinatesFromTag(input):
    #print input
    tag = input[input.index("<")+1:input.index(">")]
    coords = [ int(x) for x in tag.split(",") ]
    return coords
    
def GetDistance(coords):
    return coords[0]*coords[0] + coords[1]*coords[1] + coords[2]*coords[2]
    
def GetClosestValueInLongTerm(particles):
    minAcceleration = float('inf');
    minIndex = -1;
    counter = 0;
    for particle in particles:
        accelValue = GetDistance(particle.acceleration)
        #print accelValue
        if(accelValue < minAcceleration):
            #print accelValue
            minIndex = counter
            minAcceleration = accelValue
        counter +=1
        
    return minIndex
    
def Get1DCollisionTime(particle1, particle2, ind):
    b = particle2.velocity[ind] - particle1.velocity[ind]
    a = 1.0/2.0 * (particle2.acceleration[ind] - particle1.acceleration[ind])
    c = particle2.position[ind] - particle1.position[ind]
    if(a == 0):
        #print c,b
        if(b == 0):
            if c != 0:
                return -1, -1
            return 0,0
        val = -c/b
        return val, val
    if(b*b < 4*a*c):
        return -1,-1
    return (-b + math.sqrt(b*b - 4*a*c))/2/a, (-b - math.sqrt(b*b - 4*a*c))/2/a
    
def CheckParticleCollision(particle1, particle2):
    return (particle1.position[0] == particle2.position[0]) and \
    (particle1.position[1] == particle2.position[1]) and \
    particle1.position[2] == particle2.position[2]
    
    
def DoParticlesCollide(particle1, particle2):
    #df=v_i*t + 1/2*a*t^2 + di
    #0 =  + (v_i2 - v_i1) * t + (d2 - d1)
    if(CheckParticleCollision(particle1, particle2)):
        return True
    timesX = Get1DCollisionTime(particle1, particle2, 0)
    timesY = Get1DCollisionTime(particle1, particle2, 1)
    timesZ = Get1DCollisionTime(particle1, particle2, 2)
    
    allTimes = set()
    allTimes.add(timesX[0])
    allTimes.add(timesX[1])
    allTimes.add(timesY[0])
    allTimes.add(timesY[1])
    allTimes.add(timesZ[0])
    allTimes.add(timesZ[1])
    #print allTimes
    if(set(timesX) != set([0])):
        allTimes = allTimes.intersection(set(timesX))
    if(set(timesY) != set([0])):
        allTimes = allTimes.intersection(set(timesY))
    if(set(timesZ) != set([0])):
        allTimes = allTimes.intersection(set(timesZ))
    #print allTimes   
    return len(allTimes) != 0
    
def CheckForFutureCollisions(particles):
    for particle1 in particles:
        for particle2 in particles:
            if particle1 == particle2:
                continue
            if(DoParticlesCollide(particle1, particle2)):
                #print "collide"
                return True
    #print "no collisions"
    return False
            
    
def ManhattanDistance(particle):
    return particle.position[0] + particle.position[1] + particle.position[2]
    
def UpdateParticle(particle):
    particle.velocity[0] += particle.acceleration[0]
    particle.velocity[1] += particle.acceleration[1]
    particle.velocity[2] += particle.acceleration[2]
    particle.position[0] += particle.velocity[0]
    particle.position[1] += particle.velocity[1]
    particle.position[2] += particle.velocity[2]
    

def Day20(input):
    particles = []
    for line in input:
        values = line.split()
        position = GetCoordinatesFromTag(values[0])
        velocity = GetCoordinatesFromTag(values[1])
        acceleration = GetCoordinatesFromTag(values[2])
        particle = Particle(position, velocity, acceleration)
        particles.append(particle)
        
    print "Closest: " + str(GetClosestValueInLongTerm(particles))
    
    time = 0
    while CheckForFutureCollisions(particles):
        for particle in particles:
            UpdateParticle(particle)
        tempParticles = particles[:]
        for particle1 in particles:
            for particle2 in particles:
                if particle1 == particle2:
                    continue
                if(CheckParticleCollision(particle1, particle2)):
                    if(particle1 in tempParticles):
                        tempParticles.remove(particle1)
                    if(particle2 in tempParticles):
                        tempParticles.remove(particle2)
        particles = tempParticles
    
    print "ParticleCount: " + str(len(particles))
        
    
    
         
        
    
def Day20File(filename):
    testFile = open(filename)
    text = testFile.readlines()
    Day20(text)
    

Day20File("input.txt")
#Day20File("testInput.txt")