from solverBiCG import Solver as SolverBiCG

S = SolverBiCG(30, 30, 3)
S.solve()
S.plot_heatmap()