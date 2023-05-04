import csv

def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter= ",")
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dit = {key : value for key, value in iterable}
      print(country_dit)
      data.append(country_dit)
      return data
      
    

if __name__ == "__main__":
  data = read_csv("./app/data.csv")
  print(data[0])
  