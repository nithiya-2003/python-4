def voter_age_validation(currentyear,birthyear,votingage=18):
    age=currentyear-birthyear
    if age>=votingage:
        return ("yes you are")
    else :
        return("no,you are uneligible")



currentyear=(int(input("enter the current year")))
birthyear=(int(input("enter the birth year ")))
print(voter_age_validation(currentyear,birthyear))
