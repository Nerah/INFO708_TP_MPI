EXECS= broadcast_prog
MPICC?= mpiCC

all: ${EXECS}

broadcast_prog: broadcast_prog.cpp
	${MPICC} -o broadcast_prog broadcast_prog.cpp

clean:
	rm -f ${EXECS}