import csv
from matplotlib import pyplot as plt


def generate_summary_for_web(csvfile, html_title, html_filename, show_barchart_gender=True):

    data,headers = get_datalist_from_csv(csvfile)

    if data == "File error":
        print("File error")
        return None

    with open(html_filename, 'w') as html:
        html.write('<html>\n')
        html.write('<title>' + html_title + '</title>\n')
        html.write('<center>\n')
        html.write('<h1>' + html_title + '</h1>\n')
        html_table = create_html_table_with_data(data,headers)
        html.write(html_table)
        if show_barchart_gender:
            barChartFileName = drawBarChart(data)
            html.write("<img src="+ barChartFileName +" style='width:600px;height:400px;'>")
        html.write('</center>\n')
        html.write('</html>\n')

    return data


def get_datalist_from_csv(csvfile):
    try:
        with open(csvfile, "r") as data:
            headers = data.readline().split(',')
            headers = headers[2:len(headers)-1]
            reader = csv.reader(data)
            datalist = list(reader)
            return datalist, headers
    except (FileNotFoundError):
        return "File error"


def create_html_table_with_data(data,headers):

    html_string = """  
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border: solid 2px black;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;
  padding:10px 5px;word-break:normal;box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);min-width: 100px;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-2etr{border: solid 2px black;background-color:#9aff99;font-family:Georgia, serif !important;;text-align:centre;vertical-align:middle;}
.tg .tg-2etr:hover{background-color: #6DFE46;}
.tg .tg-no25{border: solid 2px black;font-family:"Comic Sans MS", cursive, sans-serif !important;;text-align:center;
  vertical-align:middle; background-color: #009879; color: #ffffff}
.tg .tg-pkbl{border: solid 2px black;background-color:#ffccc9;font-family:Georgia, serif !important;;text-align:centre;vertical-align:middle;}
.tg .tg-pkbl:hover{background-color: #F83B38;}
.tg .tg-bclw{border: solid 2px black;background-color:#fd6864;border-color:#000000;font-family:"Arial Black", Gadget, sans-serif !important;;
  text-align:centre;vertical-align:middle;}
.tg .tg-ua4v{border: solid 2px black;background-color: #009879; color: #ffffff;font-family:"Comic Sans MS", cursive, sans-serif !important;;text-align:center;
  vertical-align:middle;}
.tg .tg-ua4v:hover{background-color: #38F8EC;}
.tg .tg-zpyb{border: solid 2px black;background-color:#67fd9a;border-color:#000000;font-family:"Arial Black", Gadget, sans-serif !important;;
  text-align:centre;vertical-align:middle;}
.tg .tg-zpyb{border: solid 2px black;background-color:#67fd9a;border-color:#000000;font-family:"Arial Black", Gadget, sans-serif !important;;
  text-align:centre;vertical-align:middle;}
</style>
<table class="tg">
<thead>
  <tr>
    <td class="tg-ua4v" rowspan="3"><span style="font-weight:bold">Attributes</span><br></td>
    <td class="tg-no25" colspan="4"><span style="font-weight:bold">Class</span></td>
  </tr>
  <tr>
    <td class="tg-bclw" colspan="2"><span style="font-weight:bold">Positive</span></td>
    <td class="tg-zpyb" colspan="2"><span style="font-weight:bold">Negative</span></td>
  </tr>
  <tr>
    <td class="tg-2etr">Yes </td>
    <td class="tg-pkbl">No</td>
    <td class="tg-2etr">Yes</td>
    <td class="tg-pkbl">No</td>
  </tr>
</thead>
    """
    counterDic=[]
    copyHeaders=[]
    for i in headers:
        counterDic.append([0,0,0,0])
        copyHeaders.append(i.title())
        
    headers = copyHeaders
    
    for i in range(len(data)):
        usableData = data[i][2:len(data[i])]
        for index in range(len(usableData)-1):
            if usableData[-1] == "Positive":
                if usableData[index]== "Yes":
                    counterDic[index][0] += 1
                elif usableData[index]== "No":
                    counterDic[index][1] += 1
            elif usableData[-1] == "Negative":
                if usableData[index]== "Yes":
                    counterDic[index][2] += 1
                elif usableData[index]== "No":
                    counterDic[index][3] += 1
            
            
    counter = 0
    for i in headers:
        highestValue = max(counterDic[counter])
        html_string += "<tr>"
        html_string += "<td class='tg-ua4v'>"+i+"</td>"
        if highestValue == counterDic[counter][0]:
            html_string += "<td class='tg-2etr'><u><b>"+str(counterDic[counter][0])+"</b></u></td>"
        else:
            html_string += "<td class='tg-2etr'>"+str(counterDic[counter][0])+"</td>"
        if highestValue == counterDic[counter][1]:
            html_string += "<td class='tg-pkbl'><u><b>"+str(counterDic[counter][1])+"</b></u></td>"
        else:
            html_string += "<td class='tg-pkbl'>"+str(counterDic[counter][1])+"</td>"
        if highestValue == counterDic[counter][2]:
            html_string += "<td class='tg-2etr'><u><b>"+str(counterDic[counter][2])+"</b></u></td>"
        else:
            html_string += "<td class='tg-2etr'>"+str(counterDic[counter][2])+"</td>"
        if highestValue == counterDic[counter][3]:
            html_string += "<td class='tg-pkbl'><u><b>"+str(counterDic[counter][3])+"</b></u></td>"
        else:
            html_string += "<td class='tg-pkbl'>"+str(counterDic[counter][3])+"</td>"

        
        html_string += "</tr>"
        counter +=1
    
    html_string += "</table>\n\n"
    return html_string

def drawBarChart(data):
    
    outputs = [0,0,0,0]
    
    for row in data:
        if row[-1]== "Positive":
            if row[1]== "Male":
                outputs[0] +=1
            elif row[1]=="Female":
                outputs[1] +=1
        elif row[-1]=="Negative":
            if row[1]== "Male":
                outputs[2] +=1
            elif row[1]=="Female":
                outputs[3] +=1
                

    male =[outputs[0], outputs[2]]
    female = [outputs[1],outputs[3]]
    x = ["Positive", "Negative"]

    ind = [0,1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    width = 0.35  
    
    ind2=[]
    for i in ind:
        ind2.append(i+width)
    
    averageind = []
    for i in range(len(ind)):
        averageind.append((ind[i]+ind2[i])/2)
    
    bar1 = plt.bar(ind,  male, label="Male", width=width, align="center", color='cyan')
    bar2 = plt.bar(ind2,  female, label="Female", width=width, align="center", color='purple')
    
    plt.title("Gender of Positive vs Negative case")
    ax.set_xlabel('Class', labelpad=15, color='#001FFF')
    ax.set_ylabel('Count', labelpad=15, color='#FF000C')
    ax.set_xticks(averageind)
    ax.set_xticklabels(('Positive', 'Negative'))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    
    ax.tick_params(bottom=False, left=False)
    
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)
    
    bar_color1 = bar1[0].get_facecolor()
    bar_color2 = bar2[0].get_facecolor()
    
    for bar in bar1:
      ax.text(
      bar.get_x() + bar.get_width() / 2,
      bar.get_height() + 4,
      round(bar.get_height(), 1),
      horizontalalignment='center',
      color=bar_color1,
      weight='bold'
  )
    for bar in bar2:
      ax.text(
      bar.get_x() + bar.get_width() / 2,
      bar.get_height() + 4,
      round(bar.get_height(), 1),
      horizontalalignment='center',
      color=bar_color2,
      weight='bold'
  )
    
    plt.legend()
    fig.tight_layout()
    
    fig.savefig('temp.png', dpi=fig.dpi)
    return "temp.png"


