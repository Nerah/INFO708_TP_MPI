EXECS= ping_pong
MPICC?= mpiCC

all: ${EXECS}

ping_pong: ping_pong.cpp
	${MPICC} -o ping_pong ping_pong.cpp

clean:
	rm -f ${EXECS}