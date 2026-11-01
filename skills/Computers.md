---
srd-type: "skill"
section: "Skills"
key-ability: "Int"
based-on:
  - "[[modern srd 3.5/skills/Computer Use|Computer Use (Modern)]]"
  - "[[modern srd 3.5/skills/Knowledge (Technology)|Knowledge (Technology) (Modern)]]"
  - "[[star srd 3.5/rules/Skills|Skills (Starfinder)]]"
status: draft
change: new
pi-review: 2026-10-31
tags: [rangoric, rangoric/skill, core]
---

# Computers

Computers covers using, programming and breaking into computers and networks, and knowing technology in general: what a device does, and how robots and starships are built. It came from Modern’s Computer Use and Knowledge (technology) and Starfinder’s Computers (2026-10-31). It only comes up in settings that have computers.

Most ordinary computer use needs no check. Finding public information is research, which is [[rangoric-srd/skills/Investigation#Research|Investigation]]. Forging a document, on paper or not, is [[rangoric-srd/skills/Imitation|Imitation]]. Building and repairing the machine itself is [[rangoric-srd/skills/Engineering|Engineering]].

**Trained only**: Defeating security, degrading programming and writing programs can’t be done untrained. Everything else can.

## Finding Files

**Check**: You can find files or data on a private system you don’t know. The DC and the time depend on the size of the system.

| Size of System | DC | Time |
| --- | --- | --- |
| Personal computer | 10 | 1 round |
| Small office network | 15 | 2 rounds |
| Large office network | 20 | 1 minute |
| Massive corporate network | 25 | 10 minutes |

## Defeating Security

**Check**: The DC depends on the quality of the security. If you fail by 5 or more, the system alerts its administrator, who may try to identify you or cut off your access. If you beat the DC by 10 or more, you automatically succeed at later security checks on the same system until your session ends.

| Level of Security | DC |
| --- | --- |
| Minimum | 20 |
| Average | 25 |
| Exceptional | 35 |
| Maximum | 40 |

### Hacking

Breaking into a system you aren’t allowed in takes several steps. A system can be one computer or a network of many; every system has an administrator who keeps its security, and each visit is one session.

1. **Covering your tracks** (optional, DC 20): anyone trying to identify you takes a –5 penalty.
2. **Getting in**: either reach a computer on the system physically, or find the system over a network (DC 10) and then defeat its security.
3. **Finding what you want**: as Finding Files.
4. **Defeating file security**, if the files have their own.
5. **Doing what you came for**: reading needs no further check. Changing or deleting records may need another security check. Copying a lot of data can take minutes.

## Defending a System

**Check**: If you’re a system’s administrator (even of your own computer) and it alerts you to an intruder, you can make an opposed Computers check to cut off the intruder’s session (a full-round action), or another opposed check to learn where the intruder is working from (1 minute, and the intruder must stay connected the whole time). Shutting the system down also stops them, if you can.

## Degrading Programming

**Check**: You can crash a computer, destroy its programs so it can’t be used until they’re repaired, or damage them so that every Computers check on it takes a –4 penalty, which its user may not notice. Each extra computer on the same system adds +2 to the DC. Fixing the damage takes 1 hour and a check against the DC to cause it + 5.

| Change | DC | Time |
| --- | --- | --- |
| Crash computer | 10 | 1 minute |
| Destroy programming | 15 | 10 minutes |
| Damage programming | 20 | 10 minutes |

## Writing Programs

**Check**: A DC 20 check and 1 hour make a program for one specific task (one kind of operation against one target). It gives a +2 circumstance bonus on that task.

## Operating Remote Devices

**Check**: With access to the computer that runs cameras, locks, alarms and other remote devices, you can shut them off or change how they work. If you fail by 5 or more, the system alerts its administrator.

| Operation | DC | Time |
| --- | --- | --- |
| Shut down a passive device (camera, door lock) | 20 | 1 round per device |
| Shut down an active device (motion detector, alarm) | 25 | 1 round per device |
| Reset its settings | 30 | 1 minute per device |
| Change passcodes | 25 | 1 minute |
| Hide that anything was changed | +10 | 1 minute |
| Minimum security | –5 | — |
| Exceptional security | +10 | — |
| Maximum security | +15 | — |

## Identifying Technology

**Check**: You can identify a starship by type, a robot by frame, or a vehicle by model (DC 10), work out what a mechanical system or cybernetic implant does (DC 15), or recall the standard design of a kind of starship, robot or vehicle (DC 20).

Faced with an unfamiliar device, you can work out its main purpose. This doesn’t let you use it or make you proficient with it.

**Identifying Creatures**: Computers identifies technological constructs, such as robots; see [[rangoric-srd/skills/Identifying Creatures|Identifying Creatures]].

| Unfamiliar Item | DC |
| --- | --- |
| Basic tool or instrument | 10 |
| Robotic or vehicle part | 15 |
| Cybernetic implant | 20 |
| Alien weapon or nanotechnology | 25 |
| Alien artifact | 30 |
| Each step of technology older or newer than yours | +5 |

## For Every Use

**Action**: At least a full-round action. Times for longer tasks are given above.

**Try Again**: Usually. You can take 10, and you can take 20 except when failing has a cost, such as defeating or defending security.
