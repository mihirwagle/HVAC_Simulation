# HVAC_Simulation
Simple simulation of a HVAC system to show propagation of messages.

## Getting setup
    * Install python 3.x

## Running project
    * Running the following commands will run a simulation for hundred seconds.
    * python3 runSim.py
    * python3 runComplexSim.py
    
## Sample output
    * Sample output on the network in runSim.py is attached in sampleSimulation.txt
    * Sample output on the network in runComplexSim.py is attached in sampleComplexSimulation.txt

## Network details
    * The network consists of three types of entities.
        * A single Central Heating System
        * Multiple HVAC nodes
        * Edge servers connected to nodes and the CHS
    * The connections are as follows:
        * A CHS can have edge servers or the HVAC nodes as its children.
        * While a CHS can technically manage a HVAC node directly, using an edge server in between gives more order.
        * An edge server can only have the HVAC nodes as its children.
        * A HVAC node can have multiple parents.
        * An edge server can have multiple parents.
    * A simple tree like network is present in runSim.py
    * A more complex graph like network is shown in runComplexSim.py
    * The simple tree like network is more efficient since an update has to go up through only one chain.
    * The graph can try to update the same things again and again, which we handle internally.
    * Thus the graph can be thought of a network where there are more messages being sent but if each node is connected to multiple parents, we essentially have a failsafe if an edge server fails.
