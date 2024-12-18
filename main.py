from solverBiCG import Solver as SolverBiCG

S = SolverBiCG(100, 100, 6)
S.solve()
S.plot_heatmap()