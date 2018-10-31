import numpy as np
 
def laplace_mech(data,sensitivity,epsilon):
    beta = sensitivity / epsilon
    for i in range(len(data)):
        data = data + np.random.laplace(0,beta,len(data))
    return data
 
if __name__ =='__main__':
    data = (110.,0.,10.,59.,1111.)
    sensitivety = 1
    epsilon = 1
    data = laplace_mech(data,sensitivety,epsilon)
    print('the vector result under the Laplace Mechanism: '+ str(data))

