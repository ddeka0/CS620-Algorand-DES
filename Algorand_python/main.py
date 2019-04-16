# !/bin/python3
from node import *
from network_utils import *

def executeEvent(ev):
	print("got eventType = ",ev.evType," for targetNode ",ev.targetNode.nodeId)
	print("got eventTime = ", ev.evTime, " for targetNode ", ev.targetNode.nodeId)
	print("got refTime = ", ev.refTime, " for targetNode ", ev.targetNode.nodeId)

	eventType = ev.evType
	targetNode = ev.targetNode
	if eventType == EventType.BLOCK_PROPOSER_SORTITION_EVENT:
		targetNode.proposePriority(ev)
	elif eventType == EventType.GOSSIP_EVENT:
		targetNode.sendGossip(ev)
	elif eventType == EventType.SELECT_TOP_PROPOSER_EVENT:
		targetNode.selectTopProposer(ev)
	else:
		print("Event Type is not recognised")


if __name__ == "__main__":

	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)

	allNodes.append(a)
	allNodes.append(b)
	allNodes.append(c)
	allNodes.append(d)

	a.peerList.append(d)
	a.peerList.append(c)
	b.peerList.append(c)
	c.peerList.append(d)

	for i in range(MAX_NODES):
		lz = [0] * MAX_NODES
		delays.append(lz)

	delays[a.nodeId][d.nodeId] = 2
	delays[a.nodeId][c.nodeId] = 1
	delays[b.nodeId][c.nodeId] = 2
	delays[c.nodeId][d.nodeId] = 3


	for node in allNodes:
		print("pushed new event")
		newEvent = Event(0,
						0,
						EventType.BLOCK_PROPOSER_SORTITION_EVENT,
						noMessage(),
						TIMEOUT_NOT_APPLICABLE,
						node,
						1)
		eventQ.add(newEvent)

	print("Initial eventQ size = ",len(eventQ))

	while(True):
		if len(eventQ) == 0:
			break
		ev = eventQ.pop(0)
		executeEvent(ev)

	print("Simulation completed !")