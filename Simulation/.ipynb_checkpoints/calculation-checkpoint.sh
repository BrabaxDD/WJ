for filename in ./gases/*; do
	for filenameGraphene in ./grapheneDefects/*; do
		echo "$(echo "$filename" | awk -F/ '{print $NF}') $(echo "$filenameGraphene" | awk -F/ '{print $NF}' )"
		mkdir "$(echo "$filename" | awk -F/ '{print $NF}') $(echo "$filenameGraphene" | awk -F/ '{print $NF}' )"
	done
done
