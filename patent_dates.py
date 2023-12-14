import sys
import json
def patent_dates(input_file, output_file):
    with open(input_file, "r") as f:
        with open(output_file, 'a') as fs:
            fs.write("Filing Date|Publication Date|Grant Date|Priority Date\n")
            for pt in f.readlines():
                patent = json.loads(pt)
                filing_date = patent.get("filing_date", "")
                publication_date = patent.get("publication_date", "")
                grant_date = patent.get("grant_date", "")
                priority_date = patent.get("priority_date", "")

                fs.write(f"{filing_date}|{publication_date}|{grant_date}|{priority_date}\n")

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = "./patent_dates.txt"
    patent_dates(input_file, output_file)