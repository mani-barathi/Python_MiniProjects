@echo off



set argC=0
for %%x in (%*) do Set /A argC+=1


If "%1"=="" (
    echo "Error: no repo name"
) else ( 
    c:
	python C:\Users\manib\Desktop\Programs\Automate_repo_creation_github\.py %1 %2
    )
 

if %argC%==1 (
		cd C:\Users\manib\Documents
	)
