EXECS= gathering_prog
MPICC?= mpiCC

all: ${EXECS}

gathering_prog: gathering_prog.cpp
	${MPICC} -o gathering_prog gathering_prog.cpp

clean:
	rm -f ${EXECS}