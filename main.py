from solverBiCG import Solver as SolverBiCG

S = SolverBiCG(15, 15, 7)
S.solve()
S.plot_heatmap()