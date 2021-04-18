def evaluation(attempt, solution):
    attempt = list(attempt)
    solution = list(solution)
    (red, white) = (0,0)
    
    for index,value in enumerate(attempt):
        if value == solution[index]:
            red += 1
            attempt[index] = "-"
            solution[index] = "*"
    for index,value in enumerate(attempt):
        if value in solution:
            white += 1
            solution[solution.index(value)] = "*"
    return (red, white)


def test_evaluation():
    """ Desc """
    assert evaluation("RVBJ","RMOB") == (1,1)
    assert evaluation("RRRR","RRRR") == (4,0)
    assert evaluation("RVBJ","MNOG") == (0,0)
    assert evaluation("RVBJ","JRVB") == (0,4)
    assert evaluation("RVVR","RVRV") == (2,2)
    assert evaluation("RRVV","VVRR") == (0,4)
    assert evaluation("RVRV","VRVR") == (0,4)
    assert evaluation("RVRN","NNOO") == (0,1)
    assert evaluation("RVRN","NNOO") == evaluation("NNOO", "RVRN")

test_evaluation()