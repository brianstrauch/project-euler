for i in $(seq -f "%03g" 1 10)
do
	echo \#$i

	if [ -f c/$i.c ]
	then
		echo -en 'c\t'
		gcc c/$i.c
		./a.out
		rm a.out
	fi

	if [ -f cpp/$i.cpp ]
	then
		echo -en 'cpp\t'
		g++ cpp/$i.cpp
		./a.out
		rm a.out
	fi

	if [ -f go/$i.go ]
	then
		echo -en 'go\t'
		go run go/$i.go
	fi

	if [ -f java/$i.java ]
	then
		echo -en 'java\t'
		cd java
		javac $i.java
		java Problem$i
		rm Problem$i.class
		cd ..
	fi
	
	if [ -f py/$i.py ]
	then
		echo -en 'py\t'
		python py/$i.py
	fi
	echo
done
