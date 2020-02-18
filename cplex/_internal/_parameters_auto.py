# --------------------------------------------------------------------------
# Version 12.9.0
# --------------------------------------------------------------------------
# Licensed Materials - Property of IBM
# 5725-A06 5725-A29 5724-Y48 5724-Y49 5724-Y54 5724-Y55 5655-Y21
# Copyright IBM Corporation 2000, 2019. All Rights Reserved.
# 
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with
# IBM Corp.
# --------------------------------------------------------------------------


from ._constants import *


setAdvance = [CPX_PARAM_ADVIND, "indicator for advanced starting information:\n  0 = no advanced start\n  1 = standard advanced start\n  2 = alternate advanced start", CPX_PARAMTYPE_INT]
BarrierAlgorithm = [CPX_PARAM_BARALG, "barrier algorithm choice:\n  0 = default\n  1 = infeasibility - estimate start\n  2 = infeasibility - constant start\n  3 = standard barrier", CPX_PARAMTYPE_INT]
BarrierColNonzeros = [CPX_PARAM_BARCOLNZ, "minimum number of entries to consider a column dense:\n  0 = dynamically calculated\n  >0 = specific number of column entries", CPX_PARAMTYPE_INT]
BarrierConvergeTol = [CPX_PARAM_BAREPCOMP, "tolerance on complementarity for convergence", CPX_PARAMTYPE_DOUBLE]
BarrierCrossover = [CPX_PARAM_BARCROSSALG, "barrier crossover choice:\n  -1 = no crossover\n  0 = automatic\n  1 = primal crossover\n  2 = dual crossover", CPX_PARAMTYPE_INT]
BarrierDisplay = [CPX_PARAM_BARDISPLAY, "barrier display level:\n  0 = no display\n  1 = display normal information\n  2 = display detailed (diagnostic) output", CPX_PARAMTYPE_INT]
BarrierLimitsCorrections = [CPX_PARAM_BARMAXCOR, "maximum correction limit:\n  -1 = automatically determined\n  0 = none\n  >0 = maximum correction limit", CPX_PARAMTYPE_LONG]
BarrierLimitsGrowth = [CPX_PARAM_BARGROWTH, "factor used to determine unbounded optimal face", CPX_PARAMTYPE_DOUBLE]
BarrierLimitsIteration = [CPX_PARAM_BARITLIM, "barrier iteration limit", CPX_PARAMTYPE_LONG]
BarrierLimitsObjRange = [CPX_PARAM_BAROBJRNG, "barrier objective range (above and below zero)", CPX_PARAMTYPE_DOUBLE]
BarrierOrdering = [CPX_PARAM_BARORDER, "barrier ordering algorithm:\n  0 = automatic\n  1 = approximate minimum degree\n  2 = approximate minimum fill\n  3 = nested dissection", CPX_PARAMTYPE_INT]
BarrierQCPConvergeTol = [CPX_PARAM_BARQCPEPCOMP, "tolerance on complementarity for QCP convergence", CPX_PARAMTYPE_DOUBLE]
BarrierStartAlg = [CPX_PARAM_BARSTARTALG, "barrier starting point algorithm:\n  1 = dual is 0\n  2 = estimate dual\n  3 = primal avg, dual is 0\n  4 = primal avg, dual estimate", CPX_PARAMTYPE_INT]
BendersStrategy = [CPX_PARAM_BENDERSSTRATEGY, "choice of benders decomposition to use:\n  -1 = do not use benders decomposition\n  0 = automatic\n  1 = use the decomposition specified by annotation\n  2 = auto-decompose workers specified by annotation\n  3 = ignore annotation and auto-decompose model (for MIP only)", CPX_PARAMTYPE_INT]
BendersTolerancesfeasibilitycut = [CPX_PARAM_BENDERSFEASCUTTOL, "tolerance for considering a feasibility cut violated", CPX_PARAMTYPE_DOUBLE]
BendersTolerancesoptimalitycut = [CPX_PARAM_BENDERSOPTCUTTOL, "tolerance for considering an optimality cut violated", CPX_PARAMTYPE_DOUBLE]
BendersWorkerAlgorithm = [CPX_PARAM_WORKERALG, "method for optimizing benders subproblems:\n  0 = automatic\n  1 = primal simplex\n  2 = dual simplex\n  3 = network simplex\n  4 = barrier\n  5 = sifting", CPX_PARAMTYPE_INT]
setClockType = [CPX_PARAM_CLOCKTYPE, "type of clock used to measure time:\n  0 = automatic\n  1 = CPU time\n  2 = wall-clock time", CPX_PARAMTYPE_INT]
ConflictAlgorithm = [CPX_PARAM_CONFLICTALG, "algorithm used to find minimal conflicts:\n  0 = automatic\n  1 = fast\n  2 = propagation\n  3 = presolve\n  4 = IIS\n  5 = limited solve\n  6 = solve", CPX_PARAMTYPE_INT]
ConflictDisplay = [CPX_PARAM_CONFLICTDISPLAY, "level of the conflict display:\n  0 = no display\n  1 = summary display\n  2 = display every model being solved", CPX_PARAMTYPE_INT]
setCPUmask = [CPX_PARAM_CPUMASK, "cpubinding mask (off, auto, or a hex mask)", CPX_PARAMTYPE_STRING]
setDetTimeLimit = [CPX_PARAM_DETTILIM, "deterministic time limit in ticks", CPX_PARAMTYPE_DOUBLE]
DistMIPRampupDetTimeLimit = [CPX_PARAM_RAMPUPDETTILIM, "deterministic time limit on rampup", CPX_PARAMTYPE_DOUBLE]
DistMIPRampupDuration = [CPX_PARAM_RAMPUPDURATION, "duration of the rampup phase in distributed MIP:\n  -1 = rampup is disabled\n  0 = automatic\n  1 = rampup is followed by distributed tree search\n  2 = infinite horizon rampup", CPX_PARAMTYPE_INT]
DistMIPRampupTimeLimit = [CPX_PARAM_RAMPUPTILIM, "wall-clock time limit on rampup", CPX_PARAMTYPE_DOUBLE]
EmphasisMemory = [CPX_PARAM_MEMORYEMPHASIS, "reduced memory emphasis", CPX_PARAMTYPE_INT]
EmphasisMIP = [CPX_PARAM_MIPEMPHASIS, "emphasis for MIP optimization:\n  0 = balance optimality and integer feasibility\n  1 = integer feasibility\n  2 = optimality\n  3 = moving best bound\n  4 = finding hidden feasible solutions", CPX_PARAMTYPE_INT]
EmphasisNumerical = [CPX_PARAM_NUMERICALEMPHASIS, "extreme numerical caution emphasis", CPX_PARAMTYPE_INT]
FeasoptMode = [CPX_PARAM_FEASOPTMODE, "relaxation measure:\n  0 = find minimum-sum relaxation\n  1 = find optimal minimum-sum relaxation\n  2 = find minimum number of relaxations\n  3 = find optimal relaxation with minimum number of relaxations\n  4 = find minimum quadratic-sum relaxation\n  5 = find optimal minimum quadratic-sum relaxation", CPX_PARAMTYPE_INT]
FeasoptTolerance = [CPX_PARAM_EPRELAX, "minimum amount of accepted relaxation", CPX_PARAMTYPE_DOUBLE]
setLPMethod = [CPX_PARAM_LPMETHOD, "method for linear optimization:\n  0 = automatic\n  1 = primal simplex\n  2 = dual simplex\n  3 = network simplex\n  4 = barrier\n  5 = sifting\n  6 = concurrent optimizers", CPX_PARAMTYPE_INT]
MIPCutsBQP = [CPX_PARAM_BQPCUTS, "type of BQP cut generation (only applies to non-convex models solved to global optimality):\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive\n  3 = very aggressive", CPX_PARAMTYPE_INT]
MIPCutsCliques = [CPX_PARAM_CLIQUES, "type of clique cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive\n  3 = very aggressive", CPX_PARAMTYPE_INT]
MIPCutsCovers = [CPX_PARAM_COVERS, "type of cover cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive\n  3 = very aggressive", CPX_PARAMTYPE_INT]
MIPCutsDisjunctive = [CPX_PARAM_DISJCUTS, "type of disjunctive cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive\n  3 = very aggressive", CPX_PARAMTYPE_INT]
MIPCutsFlowCovers = [CPX_PARAM_FLOWCOVERS, "type of flow cover cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive", CPX_PARAMTYPE_INT]
MIPCutsGomory = [CPX_PARAM_FRACCUTS, "type of Gomory fractional cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive", CPX_PARAMTYPE_INT]
MIPCutsGUBCovers = [CPX_PARAM_GUBCOVERS, "type of GUB cover cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive", CPX_PARAMTYPE_INT]
MIPCutsImplied = [CPX_PARAM_IMPLBD, "type of implied bound cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive", CPX_PARAMTYPE_INT]
MIPCutsLiftProj = [CPX_PARAM_LANDPCUTS, "type of Lift and Project cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive\n  3 = very aggressive", CPX_PARAMTYPE_INT]
MIPCutsLocalImplied = [CPX_PARAM_LOCALIMPLBD, "type of local implied bound cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive\n  3 = very aggressive", CPX_PARAMTYPE_INT]
MIPCutsMCFCut = [CPX_PARAM_MCFCUTS, "type of MCF cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive", CPX_PARAMTYPE_INT]
MIPCutsMIRCut = [CPX_PARAM_MIRCUTS, "type of mixed integer rounding cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive", CPX_PARAMTYPE_INT]
MIPCutsPathCut = [CPX_PARAM_FLOWPATHS, "type of flow path cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive", CPX_PARAMTYPE_INT]
MIPCutsRLT = [CPX_PARAM_RLTCUTS, "type of RLT cut generation (only applies to non-convex models solved to global optimality):\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive\n  3 = very aggressive", CPX_PARAMTYPE_INT]
MIPCutsZeroHalfCut = [CPX_PARAM_ZEROHALFCUTS, "type of zero-half cut generation:\n  -1 = do not generate\n  0 = automatic\n  1 = moderate\n  2 = aggressive", CPX_PARAMTYPE_INT]
MIPDisplay = [CPX_PARAM_MIPDISPLAY, "level of mixed integer node display:\n  0 = no display\n  1 = display integer feasible solutions\n  2 = display nodes under 'mip interval' control\n  3 = same as 2, but add information on node cuts and solution times\n  4 = same as 3, but add LP display for root node\n  5 = same as 3, but add LP display for all nodes", CPX_PARAMTYPE_INT]
MIPInterval = [CPX_PARAM_MIPINTERVAL, "interval for printing mixed integer node display:\n  0 = automatic (equivalent to -1000)\n  n>0 = display every n nodes and new incumbents\n  n<0 = progressively less log output over time (closer to 0: more frequent)", CPX_PARAMTYPE_LONG]
MIPLimitsAggForCut = [CPX_PARAM_AGGCUTLIM, "constraint aggregation limit for cut generation:\n  0 = no constraint aggregation for cut generation\n  positive values at this limit", CPX_PARAMTYPE_INT]
MIPLimitsAuxRootThreads = [CPX_PARAM_AUXROOTTHREADS, "number of threads to use for auxiliary root tasks:\n  -1 = off\n  0 = automatic\n  n>0 = use n threads for auxiliary root tasks", CPX_PARAMTYPE_INT]
MIPLimitsCutPasses = [CPX_PARAM_CUTPASS, "number of cutting plane passes:\n  -1 = none\n  0 = automatic\n  positive values give number of passes to perform", CPX_PARAMTYPE_LONG]
MIPLimitsCutsFactor = [CPX_PARAM_CUTSFACTOR, "rows multiplier factor to limit cuts:\n  -1 = automatic (dynamically calculated)\n  0<=n<=1 = disable cutting plane generation\n  n>1 = number of cuts limited to (n-1) times the original number of rows", CPX_PARAMTYPE_DOUBLE]
MIPLimitsEachCutLimit = [CPX_PARAM_EACHCUTLIM, "limit on number of cuts for each type per pass", CPX_PARAMTYPE_INT]
MIPLimitsGomoryCand = [CPX_PARAM_FRACCAND, "candidate limit for generating Gomory fractional cuts", CPX_PARAMTYPE_INT]
MIPLimitsGomoryPass = [CPX_PARAM_FRACPASS, "pass limit for generating Gomory fractional cuts:\n  0 = automatic\n  positive values at this limit", CPX_PARAMTYPE_LONG]
MIPLimitsNodes = [CPX_PARAM_NODELIM, "branch and cut node limit", CPX_PARAMTYPE_LONG]
MIPLimitsPolishTime = [CPX_PARAM_POLISHTIME, "time limit for polishing best solution", CPX_PARAMTYPE_DOUBLE]
MIPLimitsPopulate = [CPX_PARAM_POPULATELIM, "solutions limit for each populate call", CPX_PARAMTYPE_INT]
MIPLimitsProbeDetTime = [CPX_PARAM_PROBEDETTIME, "deterministic time limit for probing", CPX_PARAMTYPE_DOUBLE]
MIPLimitsProbeTime = [CPX_PARAM_PROBETIME, "time limit for probing", CPX_PARAMTYPE_DOUBLE]
MIPLimitsRepairTries = [CPX_PARAM_REPAIRTRIES, "number of times to try repair heuristic:\n  -1 = none\n  0 = automatic\n  positive values give number of repair attempts", CPX_PARAMTYPE_LONG]
MIPLimitsSolutions = [CPX_PARAM_INTSOLLIM, "mixed integer solutions limit", CPX_PARAMTYPE_LONG]
MIPLimitsStrongCand = [CPX_PARAM_STRONGCANDLIM, "strong branching candidate limit", CPX_PARAMTYPE_INT]
MIPLimitsStrongIt = [CPX_PARAM_STRONGITLIM, "strong branching iteration limit:\n  0 = automatic\n  positive values at this limit", CPX_PARAMTYPE_LONG]
MIPLimitsTreeMemory = [CPX_PARAM_TRELIM, "upper limit on size of tree in megabytes", CPX_PARAMTYPE_DOUBLE]
MIPOrderType = [CPX_PARAM_MIPORDTYPE, "type of generated priority order:\n  0 = none\n  1 = decreasing cost\n  2 = increasing bound range\n  3 = increasing cost per coefficient count", CPX_PARAMTYPE_INT]
MIPPolishAfterAbsMIPGap = [CPX_PARAM_POLISHAFTEREPAGAP, "absolute MIP gap after which to start solution polishing", CPX_PARAMTYPE_DOUBLE]
MIPPolishAfterDetTime = [CPX_PARAM_POLISHAFTERDETTIME, "deterministic time after which to start solution polishing", CPX_PARAMTYPE_DOUBLE]
MIPPolishAfterMIPGap = [CPX_PARAM_POLISHAFTEREPGAP, "relative MIP gap after which to start solution polishing", CPX_PARAMTYPE_DOUBLE]
MIPPolishAfterNodes = [CPX_PARAM_POLISHAFTERNODE, "node count after which to start solution polishing", CPX_PARAMTYPE_LONG]
MIPPolishAfterSolutions = [CPX_PARAM_POLISHAFTERINTSOL, "solution count after which to start solution polishing", CPX_PARAMTYPE_LONG]
MIPPolishAfterTime = [CPX_PARAM_POLISHAFTERTIME, "time after which to start solution polishing", CPX_PARAMTYPE_DOUBLE]
MIPPoolAbsGap = [CPX_PARAM_SOLNPOOLAGAP, "absolute objective gap", CPX_PARAMTYPE_DOUBLE]
MIPPoolCapacity = [CPX_PARAM_SOLNPOOLCAPACITY, "capacity of solution pool", CPX_PARAMTYPE_INT]
MIPPoolIntensity = [CPX_PARAM_SOLNPOOLINTENSITY, "intensity for populating the MIP solution pool:\n  0 = automatic\n  1 = mild: generate few solutions quickly\n  2 = moderate: generate a larger number of solutions\n  3 = aggressive: generate many solutions and expect performance penalty\n  4 = very aggressive: enumerate all practical solutions", CPX_PARAMTYPE_INT]
MIPPoolRelGap = [CPX_PARAM_SOLNPOOLGAP, "relative objective gap", CPX_PARAMTYPE_DOUBLE]
MIPPoolReplace = [CPX_PARAM_SOLNPOOLREPLACE, "solution pool replacement strategy:\n  0 = replace oldest solutions\n  1 = replace solutions with worst objective\n  2 = replace least diverse solutions", CPX_PARAMTYPE_INT]
MIPStrategyBacktrack = [CPX_PARAM_BTTOL, "factor for backtracking, lower values give more", CPX_PARAMTYPE_DOUBLE]
MIPStrategyBBInterval = [CPX_PARAM_BBINTERVAL, "interval to select best bound node", CPX_PARAMTYPE_LONG]
MIPStrategyBranch = [CPX_PARAM_BRDIR, "direction of first branch:\n  -1 = down branch first\n  0 = automatic\n  1 = up branch first ", CPX_PARAMTYPE_INT]
MIPStrategyDive = [CPX_PARAM_DIVETYPE, "dive strategy:\n  0 = automatic\n  1 = traditional dive\n  2 = probing dive\n  3 = guided dive ", CPX_PARAMTYPE_INT]
MIPStrategyFile = [CPX_PARAM_NODEFILEIND, "file for node storage when tree memory limit is reached:\n  0 = no node file\n  1 = node file in memory and compressed\n  2 = node file on disk\n  3 = node file on disk and compressed", CPX_PARAMTYPE_INT]
MIPStrategyFPHeur = [CPX_PARAM_FPHEUR, "feasibility pump heuristic:\n  -1 = none\n  0 = automatic\n  1 = feasibility\n  2 = objective and feasibility", CPX_PARAMTYPE_INT]
MIPStrategyHeuristicFreq = [CPX_PARAM_HEURFREQ, "frequency to apply periodic heuristic algorithm:\n  -1 = none\n  0 = automatic\n  positive values at this frequency", CPX_PARAMTYPE_LONG]
MIPStrategyKappaStats = [CPX_PARAM_MIPKAPPASTATS, "strategy to gather statistics on the kappa of subproblems:\n  -1 = never\n  0 = automatic\n  1 = sample\n  2 = always", CPX_PARAMTYPE_INT]
MIPStrategyLBHeur = [CPX_PARAM_LBHEUR, "indicator for local branching heuristic", CPX_PARAMTYPE_INT]
MIPStrategyMIQCPStrat = [CPX_PARAM_MIQCPSTRAT, "MIQCP strategy:\n  0 = automatic\n  1 = solve QCP relaxation at each node\n  2 = solve LP relaxation at each node", CPX_PARAMTYPE_INT]
MIPStrategyNodeSelect = [CPX_PARAM_NODESEL, "node selection strategy:\n  0 = depth-first search\n  1 = best-bound search\n  2 = best-estimate search\n  3 = alternate best-estimate search", CPX_PARAMTYPE_INT]
MIPStrategyOrder = [CPX_PARAM_MIPORDIND, "indicator to use priority orders", CPX_PARAMTYPE_INT]
MIPStrategyPresolveNode = [CPX_PARAM_PRESLVND, "node presolve strategy:\n  -1 = no node presolve\n  0 = automatic\n  1 = force node presolve\n  2 = node probing\n  3 = aggressive node probing", CPX_PARAMTYPE_INT]
MIPStrategyProbe = [CPX_PARAM_PROBE, "probing strategy:\n  -1 = no probing\n  0 = automatic\n  1 = moderate\n  2 = aggressive\n  3 = very aggressive", CPX_PARAMTYPE_INT]
MIPStrategyRINSHeur = [CPX_PARAM_RINSHEUR, "frequency to apply RINS heuristic:\n  -1 = none\n  0 = automatic\n  positive values at this frequency", CPX_PARAMTYPE_LONG]
MIPStrategySearch = [CPX_PARAM_MIPSEARCH, "indicator for search method:\n  0 = automatic\n  1 = traditional branch-and-cut search\n  2 = dynamic search", CPX_PARAMTYPE_INT]
MIPStrategyStartAlgorithm = [CPX_PARAM_STARTALG, "algorithm to solve initial relaxation:\n  0 = automatic\n  1 = primal simplex\n  2 = dual simplex\n  3 = network simplex\n  4 = barrier\n  5 = sifting\n  6 = concurrent optimizers", CPX_PARAMTYPE_INT]
MIPStrategySubAlgorithm = [CPX_PARAM_SUBALG, "algorithm to solve subproblems:\n  0 = automatic\n  1 = primal simplex\n  2 = dual simplex\n  3 = network simplex\n  4 = barrier\n  5 = sifting", CPX_PARAMTYPE_INT]
MIPStrategyVariableSelect = [CPX_PARAM_VARSEL, "variable selection strategy:\n  -1 = minimum integer infeasibility\n  0 = automatic\n  1 = maximum integer infeasibility\n  2 = pseudo costs\n  3 = strong branching\n  4 = pseudo reduced costs", CPX_PARAMTYPE_INT]
MIPSubMIPStartAlg = [CPX_PARAM_SUBMIPSTARTALG, "algorithm to solve initial relaxation for sub-MIPs:\n  0 = automatic\n  1 = primal simplex\n  2 = dual simplex\n  3 = network simplex\n  4 = barrier\n  5 = sifting", CPX_PARAMTYPE_INT]
MIPSubMIPSubAlg = [CPX_PARAM_SUBMIPSUBALG, "algorithm to solve subproblems for sub-MIPs:\n  0 = automatic\n  1 = primal simplex\n  2 = dual simplex\n  3 = network simplex\n  4 = barrier\n  5 = sifting", CPX_PARAMTYPE_INT]
MIPSubMIPNodeLimit = [CPX_PARAM_SUBMIPNODELIMIT, "sub-MIP node limit", CPX_PARAMTYPE_LONG]
MIPSubMIPScale = [CPX_PARAM_SUBMIPSCAIND, "type of scaling used for sub-MIPs:\n  -1 = no scaling\n  0 = equilibration scaling\n  1 = aggressive scaling", CPX_PARAMTYPE_INT]
MIPTolerancesAbsMIPGap = [CPX_PARAM_EPAGAP, "absolute mixed integer optimality gap tolerance", CPX_PARAMTYPE_DOUBLE]
MIPTolerancesIntegrality = [CPX_PARAM_EPINT, "integrality tolerance", CPX_PARAMTYPE_DOUBLE]
MIPTolerancesLowerCutoff = [CPX_PARAM_CUTLO, "lower objective cutoff", CPX_PARAMTYPE_DOUBLE]
MIPTolerancesMIPGap = [CPX_PARAM_EPGAP, "mixed integer optimality gap tolerance", CPX_PARAMTYPE_DOUBLE]
MIPTolerancesObjDifference = [CPX_PARAM_OBJDIF, "absolute amount successive objective values should differ", CPX_PARAMTYPE_DOUBLE]
MIPTolerancesRelObjDifference = [CPX_PARAM_RELOBJDIF, "relative amount successive objective values should differ", CPX_PARAMTYPE_DOUBLE]
MIPTolerancesUpperCutoff = [CPX_PARAM_CUTUP, "upper objective cutoff", CPX_PARAMTYPE_DOUBLE]
MultiObjectiveDisplay = [CPX_PARAM_MULTIOBJDISPLAY, "level of display during multi-objective optimization:\n  0 = no display\n  1 = summary display after each sub-problem\n  2 = same as 1, but add sub-problem logs", CPX_PARAMTYPE_INT]
NetworkDisplay = [CPX_PARAM_NETDISPLAY, "level of the network iteration display:\n  0 = no display\n  1 = display true objective values\n  2 = display penalized objective values", CPX_PARAMTYPE_INT]
NetworkIterations = [CPX_PARAM_NETITLIM, "network simplex iteration limit", CPX_PARAMTYPE_LONG]
NetworkNetFind = [CPX_PARAM_NETFIND, "level of network extraction:\n  1 = natural network only\n  2 = reflection scaling\n  3 = general scaling ", CPX_PARAMTYPE_INT]
NetworkPricing = [CPX_PARAM_NETPPRIIND, "pricing strategy index:\n  0 = let cplex select pricing strategy\n  1 = partial pricing\n  2 = multiple partial pricing (no sorting)\n  3 = multiple partial pricing (with sorting)", CPX_PARAMTYPE_INT]
NetworkTolerancesFeasibility = [CPX_PARAM_NETEPRHS, "feasibility tolerance", CPX_PARAMTYPE_DOUBLE]
NetworkTolerancesOptimality = [CPX_PARAM_NETEPOPT, "reduced cost optimality tolerance", CPX_PARAMTYPE_DOUBLE]
setOptimalityTarget = [CPX_PARAM_OPTIMALITYTARGET, "type of solution CPLEX will attempt to compute:\n  0 = auto\n  1 = optimal solution to convex problem\n  2 = first-order optimal solution\n  3 = global optimal solution", CPX_PARAMTYPE_INT]
OutputCloneLog = [CPX_PARAM_CLONELOG, "control the creation of clone log files:\n  0 = no clone log\n  1 = create clone log", CPX_PARAMTYPE_INT]
OutputIntSolFilePrefix = [CPX_PARAM_INTSOLFILEPREFIX, "file name prefix for storing incumbents when they arrive", CPX_PARAMTYPE_STRING]
OutputMPSLong = [CPX_PARAM_MPSLONGNUM, "indicator for long numbers in MPS output files", CPX_PARAMTYPE_INT]
OutputWriteLevel = [CPX_PARAM_WRITELEVEL, "variables to include in .sol and .mst files:\n  0 = auto\n  1 = all values\n  2 = discrete values\n  3 = non-zero values\n  4 = non-zero discrete values", CPX_PARAMTYPE_INT]
setParallel = [CPX_PARAM_PARALLELMODE, "parallel optimization mode:\n  -1 = opportunistic\n  0 = automatic\n  1 = deterministic", CPX_PARAMTYPE_INT]
setParamDisplay = [CPX_PARAM_PARAMDISPLAY, "whether to display changed parameters before optimization", CPX_PARAMTYPE_INT]
PreprocessingAggregator = [CPX_PARAM_AGGIND, "limit on applications of the aggregator:\n  -1 = automatic (1 for LP, infinite for MIP)\n  0 = none\n  >0 = aggregator application limit", CPX_PARAMTYPE_INT]
PreprocessingBoundStrength = [CPX_PARAM_BNDSTRENIND, "type of bound strengthening:\n  -1 = automatic\n  0 = off\n  1 = on", CPX_PARAMTYPE_INT]
PreprocessingCoeffReduce = [CPX_PARAM_COEREDIND, "level of coefficient reduction:\n  -1 = automatic\n  0 = none\n  1 = reduce only to integral coefficients\n  2 = reduce any potential coefficient\n  3 = aggressive reduction with tilting", CPX_PARAMTYPE_INT]
PreprocessingDependency = [CPX_PARAM_DEPIND, "indicator for preprocessing dependency checker:\n  -1 = automatic\n  0 = off\n  1 = at beginning\n  2 = at end\n  3 = at both beginning and end", CPX_PARAMTYPE_INT]
PreprocessingDual = [CPX_PARAM_PREDUAL, "take dual in preprocessing:\n  -1 = no\n  0 = automatic\n  1 = yes", CPX_PARAMTYPE_INT]
PreprocessingFill = [CPX_PARAM_AGGFILL, "limit on fill in aggregation", CPX_PARAMTYPE_LONG]
PreprocessingFolding = [CPX_PARAM_FOLDING, "indicator for folding of LPs:\n  -1 = automatic\n  0 = off\n  1-5 = increasing aggressive levels", CPX_PARAMTYPE_INT]
PreprocessingLinear = [CPX_PARAM_PRELINEAR, "indicator for linear reductions:\n  0 = only linear reductions\n  1 = full reductions", CPX_PARAMTYPE_INT]
PreprocessingNumPass = [CPX_PARAM_PREPASS, "limit on applications of presolve:\n  -1 = automatic\n  0 = none\n  >0 = presolve application limit", CPX_PARAMTYPE_INT]
PreprocessingPresolve = [CPX_PARAM_PREIND, "presolve indicator", CPX_PARAMTYPE_INT]
PreprocessingQCPDuals = [CPX_PARAM_CALCQCPDUALS, "dual calculation for QCPs:\n  0 = do not calculate\n  1 = calculate only if it does not interfere with presolve reductions\n  2 = calculate and disable interfering presolve reductions", CPX_PARAMTYPE_INT]
PreprocessingQPMakePSD = [CPX_PARAM_QPMAKEPSDIND, "indicator to make a binary qp psd or tighter", CPX_PARAMTYPE_INT]
PreprocessingQToLin = [CPX_PARAM_QTOLININD, "indicator to linearize products in the objective involving binary variables (for convex MIQP), or all products of bounded variables (for global QP):\n  -1 = automatic\n  0 = off\n  1 = on", CPX_PARAMTYPE_INT]
PreprocessingReduce = [CPX_PARAM_REDUCE, "type of primal and dual reductions:\n  0 = no primal and dual reductions\n  1 = only primal reductions\n  2 = only dual reductions\n  3 = both primal and dual reductions", CPX_PARAMTYPE_INT]
PreprocessingRelax = [CPX_PARAM_RELAXPREIND, "indicator for additional presolve of lp relaxation of mip:\n  -1 = automatic\n  0 = off\n  1 = on", CPX_PARAMTYPE_INT]
PreprocessingRepeatPresolve = [CPX_PARAM_REPEATPRESOLVE, "repeat mip presolve:\n  -1 = automatic\n  0 = off\n  1 = repeat presolve without cuts\n  2 = repeat presolve with cuts\n  3 = repeat presolve with cuts and allow new root cuts", CPX_PARAMTYPE_INT]
PreprocessingSymmetry = [CPX_PARAM_SYMMETRY, "indicator for symmetric reductions:\n  -1 = automatic\n  0 = off\n  1-5 = increasing aggressive levels", CPX_PARAMTYPE_INT]
setQPMethod = [CPX_PARAM_QPMETHOD, "method for quadratic optimization:\n  0 = automatic\n  1 = primal simplex\n  2 = dual simplex\n  3 = network simplex\n  4 = barrier\n  5 = sifting\n  6 = concurrent optimizers", CPX_PARAMTYPE_INT]
setRandomSeed = [CPX_PARAM_RANDOMSEED, "seed to initialize the random number generator", CPX_PARAMTYPE_INT]
ReadAPIEncoding = [CPX_PARAM_APIENCODING, "code page for API strings", CPX_PARAMTYPE_STRING]
ReadConstraints = [CPX_PARAM_ROWREADLIM, "constraint read size", CPX_PARAMTYPE_INT]
ReadDataCheck = [CPX_PARAM_DATACHECK, "indicator to check data consistency:\n  0 = data checking off\n  1 = data checking on input\n  2 = provide modeling assistance", CPX_PARAMTYPE_INT]
ReadFileEncoding = [CPX_PARAM_FILEENCODING, "code page for file reading and writing", CPX_PARAMTYPE_STRING]
ReadNonzeros = [CPX_PARAM_NZREADLIM, "constraint nonzero read size", CPX_PARAMTYPE_LONG]
ReadQPNonzeros = [CPX_PARAM_QPNZREADLIM, "quadratic nonzero read size", CPX_PARAMTYPE_LONG]
ReadScale = [CPX_PARAM_SCAIND, "type of scaling used:\n  -1 = no scaling\n  0 = equilibration scaling\n  1 = aggressive scaling", CPX_PARAMTYPE_INT]
ReadVariables = [CPX_PARAM_COLREADLIM, "variable read size", CPX_PARAMTYPE_INT]
ReadWarningLimit = [CPX_PARAM_WARNLIM, "max number of warnings to display", CPX_PARAMTYPE_LONG]
setRecord = [CPX_PARAM_RECORD, "record calls to C API", CPX_PARAMTYPE_INT]
SiftingAlgorithm = [CPX_PARAM_SIFTALG, "algorithm used to solve sifting subproblems:\n  0 = automatic\n  1 = primal simplex\n  2 = dual simplex\n  3 = network simplex\n  4 = barrier", CPX_PARAMTYPE_INT]
SiftingSimplex = [CPX_PARAM_SIFTSIM, "allow sifting to be called from simplex", CPX_PARAMTYPE_INT]
SiftingDisplay = [CPX_PARAM_SIFTDISPLAY, "level of the sifting iteration display:\n  0 = no display\n  1 = display major sifting iterations\n  2 = display work LP logs", CPX_PARAMTYPE_INT]
SiftingIterations = [CPX_PARAM_SIFTITLIM, "sifting iteration limit", CPX_PARAMTYPE_LONG]
SimplexCrash = [CPX_PARAM_CRAIND, "type of crash used:\n  LP primal: 0 = ignore objective coefficients during crash\n  LP primal: 1 or -1 = alternate ways of using objective coefficients\n  LP dual: 1 = default starting basis\n  LP dual: 0 or -1 = aggressive starting basis\n  QP primal: -1 = slack basis\n  QP primal: 0 = ignore Q terms and use LP solver for crash\n  QP primal: 1 = ignore objective and use LP solver for crash\n  QP dual: -1 = slack basis\n  QP dual: 0 or 1 = use Q terms for crash", CPX_PARAMTYPE_INT]
SimplexDGradient = [CPX_PARAM_DPRIIND, "type of dual gradient used in pricing:\n  0 = determined automatically\n  1 = standard dual pricing\n  2 = steepest-edge pricing\n  3 = steepest-edge pricing in slack space\n  4 = steepest-edge pricing, unit initial norms\n  5 = devex pricing", CPX_PARAMTYPE_INT]
SimplexDisplay = [CPX_PARAM_SIMDISPLAY, "level of the iteration display:\n  0 = no display\n  1 = display after refactorization\n  2 = display every iteration", CPX_PARAMTYPE_INT]
SimplexDynamicRows = [CPX_PARAM_DYNAMICROWS, "indicator for dynamic management of rows:\n  -1 = automatic\n   0 = keep all rows\n   1 = manage rows", CPX_PARAMTYPE_INT]
SimplexLimitsIterations = [CPX_PARAM_ITLIM, "upper limit on primal and dual simplex iterations", CPX_PARAMTYPE_LONG]
SimplexLimitsLowerObj = [CPX_PARAM_OBJLLIM, "lower limit on value of objective", CPX_PARAMTYPE_DOUBLE]
SimplexLimitsPerturbation = [CPX_PARAM_PERLIM, "upper limit on iterations with no progress:\n  0 = automatic\n  >0 = user specified limit", CPX_PARAMTYPE_INT]
SimplexLimitsSingularity = [CPX_PARAM_SINGLIM, "upper limit on repaired singularities", CPX_PARAMTYPE_INT]
SimplexLimitsUpperObj = [CPX_PARAM_OBJULIM, "upper limit on value of objective", CPX_PARAMTYPE_DOUBLE]
SimplexPerturbationConstant = [CPX_PARAM_EPPER, "perturbation constant", CPX_PARAMTYPE_DOUBLE]
SimplexPerturbationIndicator = [CPX_PARAM_PERIND, "perturbation indicator", CPX_PARAMTYPE_INT]
SimplexPGradient = [CPX_PARAM_PPRIIND, "type of primal gradient used in pricing:\n  -1 = reduced-cost pricing\n  0 = hybrid reduced-cost and devex pricing\n  1 = devex pricing\n  2 = steepest-edge pricing\n  3 = steepest-edge pricing, 1 initial norms\n  4 = full pricing", CPX_PARAMTYPE_INT]
SimplexPricing = [CPX_PARAM_PRICELIM, "size of the pricing candidate list", CPX_PARAMTYPE_INT]
SimplexRefactor = [CPX_PARAM_REINV, "refactorization interval", CPX_PARAMTYPE_INT]
SimplexTolerancesFeasibility = [CPX_PARAM_EPRHS, "feasibility tolerance", CPX_PARAMTYPE_DOUBLE]
SimplexTolerancesMarkowitz = [CPX_PARAM_EPMRK, "Markowitz threshold tolerance", CPX_PARAMTYPE_DOUBLE]
SimplexTolerancesOptimality = [CPX_PARAM_EPOPT, "reduced cost optimality tolerance", CPX_PARAMTYPE_DOUBLE]
setSolutionType = [CPX_PARAM_SOLUTIONTYPE, "solution information CPLEX will attempt to compute:\n  0 = auto\n  1 = basic solution\n  2 = primal dual vector pair", CPX_PARAMTYPE_INT]
setThreads = [CPX_PARAM_THREADS, "default parallel thread count:\n  0 = automatic\n  1 = sequential\n  >1 = parallel", CPX_PARAMTYPE_INT]
setTimeLimit = [CPX_PARAM_TILIM, "time limit in seconds", CPX_PARAMTYPE_DOUBLE]
TuneDetTimeLimit = [CPX_PARAM_TUNINGDETTILIM, "deterministic time limit per model and per test setting", CPX_PARAMTYPE_DOUBLE]
TuneDisplay = [CPX_PARAM_TUNINGDISPLAY, "level of the tuning display:\n  0 = no display\n  1 = minimal display\n  2 = display settings being tried\n  3 = display settings and logs", CPX_PARAMTYPE_INT]
TuneMeasure = [CPX_PARAM_TUNINGMEASURE, "method used to compare across multiple problems:\n  1 = average\n  2 = minmax", CPX_PARAMTYPE_INT]
TuneRepeat = [CPX_PARAM_TUNINGREPEAT, "number of times to permute the model and repeat", CPX_PARAMTYPE_INT]
TuneTimeLimit = [CPX_PARAM_TUNINGTILIM, "time limit per model and per test setting", CPX_PARAMTYPE_DOUBLE]
setWorkDir = [CPX_PARAM_WORKDIR, "directory for CPLEX working files", CPX_PARAMTYPE_STRING]
setWorkMem = [CPX_PARAM_WORKMEM, "memory available for working storage (in megabytes)", CPX_PARAMTYPE_DOUBLE]
