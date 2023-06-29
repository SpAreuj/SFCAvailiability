import random

"""PRAMETERS"""
availiability_treshold=0.999999
cost_penalty_regulizer = 1
"""
seed=0
random.seed(seed)
"""
population=20
iterations=10000

"""STARTING POINT"""
#notazione la serie è indicata come una lista in cui i numeri all interno corrispondono al numero di blocchi per quella posizione
model = [1,1,1,1]
avliabilities=[0.99187055,0.99187055,0.991855699,0.990683662]


"""MUTATION ENGINE"""
def mutation(model):
    selector = random.randint(0, 2*(len(model)))
    change_mode = int(selector/len(model)-1)
    block_selected = selector%len(model)
    if change_mode == 0: #RIDONDA
        model[block_selected] = model[block_selected]+1
    elif change_mode == 1: #RIMUOVI
        if model[block_selected]>1: #controllo se posso farlo
            model[block_selected] = model[block_selected]-1
    return model


"""AVALIABILITY EVALUATION"""
def evaluate_availiability(model, availiabilities):
    partial_av=[]
    block_selector=0
    for block in model:
        partial_av.append(1-pow((1-availiabilities[block_selector]),model[block_selector]))
        block_selector=block_selector+1
    av=1
    for part in partial_av:
        av *= part
    return av

"""BLOCK CALCULATION"""
def block_count(model):
    tot_block=0
    for block in range(0,len(model)-1):
        tot_block = tot_block + model[block]
    return tot_block

"""FITNESS EVALUATION"""
def fitness_function(model, total_availiabilty,cost_penalty_regulizer):
    tot_block = block_count(model)

    fit_value = total_availiabilty-tot_block/cost_penalty_regulizer
    return fit_value

#MAIN
winner = [99,99,99,99]
for i in range(1,iterations):
    conditon = True
    best_model = [1,1,1,1]
    best_fitness = fitness_function(model,evaluate_availiability(model, avliabilities),cost_penalty_regulizer)
    while (conditon):
        for sample in range(1,population):
            sample_model = mutation(best_model)
            sample_availability = evaluate_availiability(sample_model,avliabilities)
            sample_fitness = fitness_function(sample_model,sample_availability,cost_penalty_regulizer)
            if sample_fitness > best_fitness:
                best_model= sample_model
                best_fitness= sample_fitness
            if(sample_availability >= availiability_treshold):
                conditon= False
                if block_count(winner)>block_count(sample_model):
                    print("Nuovo miglior modello", sample_model,"con availability",sample_availability)
                    winner=sample_model
                break
    
