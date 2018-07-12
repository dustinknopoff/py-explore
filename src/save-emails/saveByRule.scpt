using terms from application "Mail"
	on perform mail action with messages theMessages for rule theRule
		tell application "Mail"
			set msgs to selection
			
			if length of msgs is not 0 then
				
				set theFolder to (system attribute "HOME") & "/Downloads/"
				
				repeat with msg in msgs
					set msgContent to source of msg
					-- determine date received of msg and put into YYYY-MM-DD format
					set msgDate to date received of msg
					-- parse date SEMversion below using proc pad2()
					set {year:y, month:m, day:d, hours:h, minutes:min} to (msgDate)
					set msgDate to ("" & y & "-" & my pad2(m as integer) & "-" & my pad2(d))
					
					-- assign subject of msg
					set msgSubject to (subject of msg)
					
					-- create filename.eml to be use as title saved
					set newFile to (msgDate & "-" & msgSubject & ".eml") as rich text
					set newFilePath to theFolder & newFile as rich text
					
					set referenceNumber to open for access newFilePath with write permission
					try
						write msgContent to referenceNumber
						delete msg
					on error
						close access referenceNumber
					end try
					close access referenceNumber
					
				end repeat
				
			end if -- msgs > 0
		end tell
	end perform mail action with messages
end using terms from

on pad2(n)
	return text -2 thru -1 of ("00" & n)
end pad2
