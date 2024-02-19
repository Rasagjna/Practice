import matplotlib.pyplot as plt
import numpy as np
# x=[1,2,3,4,5,6,7]
# y= [50,51,52,48,47,49,46]

# # plt.plot(x,y,color="green",linewidth=5,linestyle='dotted,markersize=20')
# plt.xlabel('Day')
# plt.ylabel('Temperature')
# # plt.plot(x,y,'g+-')
# plt.plot(x,y,color='green',alpha=1) # alpha controls transperancy-> 1 is opaque
# plt.show()

# days = [1,2,3,4,5,6,7]
# max_t = [50,51,52,48,47,49,46]
# min_t = [43,42,40,44,33,35,37]
# avg_t = [45,48,48,46,40,42,41]
# plt.xlabel("Days")
# plt.ylabel("Temperature")
# plt.title("Weather")
# plt.plot(days, max_t,label="Max")
# plt.plot(days, min_t,label = "Min")
# plt.plot(days, avg_t,label="Avg")
# plt.legend(loc="best",shadow = True,fontsize="small")
# plt.grid()
# plt.show()

company=["GOOGL","AMZN","MSFT","FB"]
revenue = [90,136,89,27]
profit=[40,2,34,12]
xpos=np.arange(len(company))
plt.xticks(xpos,company)
plt.ylabel("revenue(bln)")
plt.title("US Tech Stocks")
plt.bar(xpos-0.2,revenue,width=0.4,label ="Revenue")
plt.bar(xpos+0.2,profit,width=0.4, label="Profit")
plt.legend()
plt.show()

# horizontal bars -> barh

############## histograms ##########################
blood_sugar_men = [113,85,90,150,149,88,115,135,80,77,82,129]
blood_sugar_women = [65,98,89,120,133,150,84,69,89,120,112,100]
plt.xlabel("sugar range")
plt.ylabel("total no of patients")
plt.title("blood sugar analysis")
plt.hist([blood_sugar_men,blood_sugar_women],bins=3,rwidth=0.95, rwidth=0.95,color=["g","o"],label=["man","women"],orientation="horizontal")
plt.legend()

exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent", "Food", "Phone/Internet Bill","Car","Other Utilities"]
plt.axis("equal")
plt.pie(exp_vals,labels=exp_labels,radius=1.5,autopct='%0.1f%%',shadow=True,explode=[0,0.1,0.1,0,0],startangle=180)
plt.savefig("piechart.png",bbox_inches="tight")
plt.show()


