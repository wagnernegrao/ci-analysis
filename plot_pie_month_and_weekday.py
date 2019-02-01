# Plot para ver dados em pizza com percentual por dia da semana e mês

def plot_pie_weekday(monday, tuesday, wednesday, thursday, friday, saturday, sunday): #year
    
    x_list= [len(monday), len(tuesday), len(wednesday), len(thursday), len(friday), len(saturday), len(sunday)]
    labels_list = ['Monday', 'Tuesday','wednesday','thursday ','friday','saturday','sunday']
    
    plt.axis('equal')
    
    plt.pie(x_list, labels = labels_list, autopct='%1.1f%%')
    plt.title("Frequencia de commit por dia da semana")
    plt.show()


def plot_graphic_month(january, february, march, april, may, june, july, august, september, october, november, december): #year
    
    x_list = [len(january), len(february), len(march), len(april), len(may), len(june), len(july), len(august), len(september), len(october), len(november), len(december)]
    labels_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    
    plt.axis('equal')
    
    plt.pie(x_list, labels = labels_list, autopct='%1.1f%%')
    plt.title("Frequencia de commit por mês do ano")
    plt.show()