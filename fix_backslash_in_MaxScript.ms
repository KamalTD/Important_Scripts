/*Replace Character */

fn replace_char strName_ char rep_char =(
	strName = strName_

	strArr = filterString strName char
	newName = ""
	eofName = false
	for str in strArr while eofName != true do (


		if trimRight str char != "." then
		(
			newName += str + rep_char
		)
		else 
		(
			eofName = true
		)

	)
	return newName
)

/*using replace_char*/
print (replace_char ("C:\\mayfolder\\andmyfolder\\") "\\" "/") /*replace backslash with forwordslash */
