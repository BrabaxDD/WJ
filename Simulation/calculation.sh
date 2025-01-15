mkdir results
cd results
touch results.txt
cd ..
python jsoninit.py
for filename in ./gases/*; do
	for filenameGraphene in ./grapheneDefects/*; do
		echo "$(echo "$filename" | awk -F/ '{print $NF}') $(echo "$filenameGraphene" | awk -F/ '{print $NF}' )"
		mkdir "results/$(echo "$filename" | awk -F/ '{print $NF}') $(echo "$filenameGraphene" | awk -F/ '{print $NF}' )"
		cd "results/$(echo "$filename" | awk -F/ '{print $NF}') $(echo "$filenameGraphene" | awk -F/ '{print $NF}' )"
		cp ./../../$filenameGraphene .
		mv $(echo "$filenameGraphene" | awk -F/ '{print $NF}' ) defect 
		cp ./../../$filename .
		mv $(echo "$filename" | awk -F/ '{print $NF}' ) gas 
		cp ./../../script.py .
        cp ./../../statistics.py .
		python script.py
		mkdir gasdir
		cd gasdir
		cp ./../gas .
		echo "\$write
   json=true
   output file=properties.out" >> gas
 
		xtb gas --opt > output
		cd ..
		mkdir defectdir 
		cd defectdir 
		cp ./../defect .
		echo "\$write
   json=true
   output file=properties.out" >> defect
 

		xtb defect --opt > output
		cd ..
		mkdir interactiondir
		cd interactiondir 
		cp ./../interaction .
		echo "\$write
   json=true
   output file=properties.out" >> interaction
 

		xtb interaction --opt > output
		cd ..
        python statistics.py


		cd ../..
	done
done
