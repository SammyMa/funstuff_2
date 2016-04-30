TS=3					# number of pits in game
STONES=3 				# number of stones in game
COUNTER=0				# counts the number of games played
GAMES=10				# number of games to play
TIMER=30				# max seconds per turn
 
rm *result_* # delete old files
	  
  	while [ $COUNTER -lt $GAMES ]; do
		python run_game.py $PITS $STONES $TIMER $1 $2 > result_game
		tail -1 result_game >> result_total
		let COUNTER=COUNTER+1
	done
sort result_total | uniq -dc"""Clear the transposition table

