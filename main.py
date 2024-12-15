from solverBiCG import Solver as SolverBiCG

S = SolverBiCG(51, 51, 7)
S.solve()
S.plot_heatmap()