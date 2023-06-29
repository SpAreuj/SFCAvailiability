# Analisi di affidabilità di un esempio di SFC con tecnologia NFV

## Gruppo
* Luigi Ferraioli 0622701853
* Dario Picone 0622701750
* Mario Petagna 0622701757

## Costrtruzione di un modello SRN
È stato costruito un modello SRN per rappresentare il singolo nodo dell NFV e su di esso è stata calcolata la disponibilità

## Stima a massima verosimilianza dei parametri
È stato calcolato MTTF e MTTR a partire da 2 dataset di dati censurati e non per lo strato hardware del nodo presentato

## Raggiungimento dei six-nines di disponibilità
È stato utilizzato un modello RDB per rappresentare la catena di nodi. Sono stati utilizzati 2 approcci; uno puramente euristico e uno basato su un algoritmo genetico che trova una possibile configurazione minima

## Analisi di sensitività
È stata analizzata la sensitività al variare dell MTTF e MTTR della parte relativa al docker dei container ricavano cosi quanto si potessere allargare il margine rimanendo nel goal dei six-nines di disponibilità
