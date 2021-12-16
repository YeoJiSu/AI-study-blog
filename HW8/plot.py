import numpy as np
import matplotlib.pyplot as plt

# First-choice hill climbing
first_y = []
# 파일을 열어서 읽어와 first_y에 따른 first_x를 저장함
infile = open("first.txt", 'r')
for line in infile:
    first_y.append(float(line))
first_x = np.arange(len(first_y))
infile.close()

# Simulated annealing
anneal_y =[]
# 파일을 열어서 읽어와 anneal_y에 따른 anneal_x를 저장함
infile = open('anneal.txt', 'r')
for line in infile:
    anneal_y.append(float(line))
anneal_x = np.arange(len(anneal_y))
infile.close()

# 함수를 그린다. 
plt.plot(first_x, first_y)
plt.plot(anneal_x, anneal_y)

# 각각에 해당하는 레이블, 제목, legend를 붙여준다. 
plt.xlabel('Number of Evaluations')
plt.ylabel('Tour Cost')
plt.title('Search Performance (TSP-100)')
plt.legend(['First-Choice HC', 'Simulated Annealing'])

# 함수를 보인다. 
plt.show()