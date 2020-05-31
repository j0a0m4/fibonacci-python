def fibo1(n):
    state = [0, 1]
    for i in range(2, n + 1):
        state.append(state[i - 1] + state[i - 2])
    return state[n]
