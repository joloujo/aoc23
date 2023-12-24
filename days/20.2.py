from updateData import updateData, loadDay # Automatically updates data files
import numpy as np

DAY = 20
TEST = False

updateData(DAY)
data = loadDay(DAY, TEST)
if data == None:
    print("No data yet :(")
    exit()

lines = data.readlines()


class Pulse():
    def __init__(self, source: str, destination: str, power: str) -> None:
        self.s = source
        self.d = destination
        self.p = power

    def __str__(self) -> str:
        return f"{self.s} -{self.p}-> {self.d}"


broadcast_queue: list[Pulse] = []


class Module():
    def __init__(self, module: str, module_type: str, destinations: list[str]) -> None:
        self.m = module
        self.t = module_type
        self.d = destinations

    def broadcast(self, pulse: Pulse):
        return
    
    def __str__(self) -> str:
        return f"{self.t} {self.m} -> {', '.join(self.d)}"


class Broadcaster(Module):
    def __init__(self, module: str, destinations: list[str]) -> None:
        super().__init__(module, 'broadcaster', destinations)
    
    def broadcast(self, pulse: Pulse):
        for destination in self.d:
            broadcast_queue.append(Pulse(self.m, destination, pulse.p))


class FlipFlop(Module):
    def __init__(self, module: str, destinations: list[str]) -> None:
        super().__init__(module, 'flip flop', destinations)
        self.s: bool = False
    
    def broadcast(self, pulse: Pulse):
        if pulse.p == "low":
            self.s = not self.s
            for destination in self.d:
                next_pulse_power = "high" if self.s else "low"
                broadcast_queue.append(Pulse(self.m, destination, next_pulse_power))


class Conjunction(Module):
    def __init__(self, module: str, destinations: list[str]) -> None:
        super().__init__(module, 'conjunction', destinations)
        self.i: list[str] = []
        self.s: list[bool] = []

    def broadcast(self, pulse):
        i = self.i.index(pulse.s)
        self.s[i] = pulse.p == "high"

        next_pulse_power = "high"
        if all(self.s):
            next_pulse_power = "low"
        
        for destination in self.d:
            broadcast_queue.append(Pulse(self.m, destination, next_pulse_power))


modules: list[Module] = []

for raw_line in lines:
    line = raw_line.strip('\n\r')

    words = line.split()

    module = words[0]
    module_type = module[0]
    if module == 'broadcaster':
        module_type = 'broadcaster'
    else:
        module = module[1:]

    destinations = [d.strip(',') for d in words[2:]]

    match module_type:
        case "broadcaster":
            modules.append(Broadcaster(module, destinations))
        case "%":
            modules.append(FlipFlop(module, destinations))
        case "&":
            modules.append(Conjunction(module, destinations))
    
for m in modules:
    if type(m) == Conjunction:
        for m2 in modules:
            if m.m in m2.d:
                m.i.append(m2.m)
                m.s.append(False)

def cycle():
    global high_pulses, low_pulses

    broadcast_queue.append(Pulse("button module", "broadcaster", "low"))
    while len(broadcast_queue) > 0:

        pulse = broadcast_queue.pop(0)
        # print(pulse)

        if pulse.d == "rx" and pulse.p == "low":
            return False

        module = pulse.d

        for m in modules:
            if m.m == module:
                m.broadcast(pulse)
    
    return True

keep_looping = True
i = 0
while keep_looping:
    i += 1
    if i % 1000 == 0:
        print("CYCLE:", i)
    keep_looping = cycle()

print(i)