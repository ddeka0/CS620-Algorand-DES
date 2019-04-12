#pragma once
#include <bits/stdc++.h>
using namespace std;

class Node;
class Event {
public:
	int refTime;	// start reference time of this type of event
	int eventTime;
	int eventType;
	int eventTimeOutTime;
	shared_ptr<Node> targetNode;
	string msgToDeliver;
	
	// add more field if required
	Event(int refTime,int eventTime,shared_ptr<Node> targetNode,string msg,
        int eventType,int timeOut) {
		this->refTime = refTime;
		this->eventTime = eventTime;
		this->targetNode = targetNode;
		this->msgToDeliver = msg;
		this->eventType = eventType;
		this->eventTimeOutTime = timeOut;
	}
	// overload < operator so that the queue can be sorted atomatically
	bool operator < (const Event & event) const;
};