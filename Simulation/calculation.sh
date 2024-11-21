for filename in ./gases/*; do
	for filenameGraphene in ./grapheneDefects/*; do
		echo "$(echo "$filename" | awk -F/ '{print $NF}') $(echo "$filenameGraphene" | awk -F/ '{print $NF}' )"
		mkdir "$(echo "$filename" | awk -F/ '{print $NF}') $(echo "$filenameGraphene" | awk -F/ '{print $NF}' )"
		cd "$(echo "$filename" | awk -F/ '{print $NF}') $(echo "$filenameGraphene" | awk -F/ '{print $NF}' )"
		cp ./../$filenameGraphene .
		mv $(echo "$filenameGraphene" | awk -F/ '{print $NF}' ) defect 
		cp ./../$filename .
		mv $(echo "$filename" | awk -F/ '{print $NF}' ) gas 
		cd ..
	done
done
