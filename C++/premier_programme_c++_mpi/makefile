EXECS= premier_prog
MPICC?= mpiCC

all: ${EXECS}

premier_prog: main.cpp
	${MPICC} -o premier_prog main.cpp

clean:
	rm -f ${EXECS}