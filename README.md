# fedblock
## Build Steps
- Setup `ganache-cli` and `truffle`
- Setup `ipfs` and `redis`
- Run setup.sh
- Run ganache using `ganache-cli -p 7545`
- Run ipfs using `ipfs daemon`
- Run Redis using `redis-server`
- Run `run.py` in ./flask/organizaton and ./flask/client respectively

Our Fedblock mainly has 3 major components i.e. Client Side Interface , Organization Side Interface and a Machine Learning Model Processor. One could consider that our system proceeds in a round by round fashion. In a round, the organization publishes a base_model to IPFS which the client uses to learn trends locally. The client then publishes an incremental model update to IPFS. The organization then uses the FederatedAveraging mechanism to merge all these incremental models into one model and sets it as the new base_model. The process repeats and over time the base_model learns from trends generated on all devices.