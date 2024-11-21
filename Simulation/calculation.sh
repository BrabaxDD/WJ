mkdir results
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
		python script.py
		mkdir gasdir
		cd gasdir
		cp ./../gas .
		echo "\$write
   json=true
   output file=properties.out" >> gas
 
		xtb gas > output
		cd ..
		mkdir defectdir 
		cd defectdir 
		cp ./../defect .
		echo "\$write
   json=true
   output file=properties.out" >> defect
 

		xtb defect > output
		cd ..

		cd ../..
	done
done
