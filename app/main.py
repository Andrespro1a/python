import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv("data.csv")
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  
  countries = list(map(lambda x: x["Country/Territory"], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)



  country = input("Type Country => ")
  print(country)
  
  result = utils.populations_by_country(data, country)

  if len(result) > 0: 
    print(country)
    country = result[0]
    labels, values = utils.get_populations(country)
    charts.generate_basr_chart(country[country], labels, values)

if __name__ == '__main__':
  run()
