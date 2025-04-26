def general_options_fdf(options:dict=None)-> str:
    # Dictionary with default values (can be modified by parameters)
    defaults = {
        "UseSaveData":"false", #true
        "WriteCoorInital":"false",
        "WriteCoorStep":"false",
        "WriteForces":"false",
        "WriteKpoints":"false",
        "WriteEigenvalues":"false",
        "WriteKbands":"false",
        "WriteBands":"false",
        "WriteWaveFunctions":"false",
        "WriteMullikenPop":"0",
        "WriteDM":"true",
        "WriteCoorXmol":"true",
        "WriteCoorCerius":"false",
        "WriteMDXmol":"true",
        "WriteMDhistory":"true",
        "MD_UseSaveXV":"false"     
    }
    #Update the dictionary with the provided parameters
    if options:
        defaults.update(options)

    # Construir el contenido del archivo .fdf
    return f"""
#####################################
#       General Options             #
  UseSaveData	     {defaults['UseSaveData']}   #	
  WriteCoorInital    {defaults['WriteCoorInital']}#
  WriteCoorStep      {defaults['WriteCoorStep']}  #
  WriteForces	     {defaults['WriteForces']}    # 
  WriteKpoints	     {defaults['WriteKpoints']}   # 
  WriteEigenvalues   {defaults['WriteEigenvalues']}#
  WriteKbands	     {defaults['WriteKbands']}    #
  WriteBands	     {defaults['WriteBands']}     #
  WriteWaveFunctions {defaults['WriteWaveFunctions']}# 
  WriteMullikenPop   {defaults['WriteMullikenPop']}# 
  WriteDM	         {defaults['WriteDM']}        #
  WriteCoorXmol	     {defaults['WriteCoorXmol']}  #
  WriteCoorCerius    {defaults['WriteCoorCerius']}#
  WriteMDXmol	     {defaults['WriteMDXmol']}    #
  WriteMDhistory     {defaults['WriteMDhistory']} #
  MD.UseSaveXV       {defaults['MD_UseSaveXV']}#
####################################
"""

def parallel_options_fdf(options:dict = None)-> str:
    # Dictionary with default values (can be modified by parameters)
    defaults = {
        "BlockSize":"32",
        "ProcessorY":"16",
        "DiagMemory":"1",
        "TryMemoryIncrease":"true",
        "DiagScale":"1",
        "ParallelOverK":"false"        
    }

    if options:
        #Update the dictionary with the provided parameters
        defaults.update(options)

    # Construir el contenido del archivo .fdf
    return f"""
#####################################
#  Parallel options                 #
#  BlockSize   {defaults['BlockSize']}          #
#  ProcessorY  {defaults['ProcessorY']}         #
#  DiagMemory  {defaults['DiagMemory']}         #
#  TryMemoryIncrease  {defaults['TryMemoryIncrease']}#
#  DiagScale   {defaults['DiagScale']}          #
#  ParallelOverK      {defaults['ParallelOverK']}#
#####################################
"""

def system_options_fdf(options:dict = None)-> str:
    # Dictionary with default values (can be modified by parameters)
    defaults = {
        "PAO_BasisSize": "DZP",
        "PAO_EnergyShift": "0.07 eV",
        "XC_functional": "GGA",
        "XC_authors": "PBE",
        "MaxSCFIterations": "550",
        "MeshCutoff": "250 Ry",
        "DM_MixingWeight": "0.1",
        "DM_Tolerance": "1.000E-4",
        "DM_NumberPulay": "5",
        "SolutionMethod": "diagon",
        "ElectronicTemperature": "5.0 meV",
        "Spin": "non-polarized",
        "DFTD3": "True",
        "DFTD3_BJdamping": "True",
        "n1": "3",
        "n2": "3",
        "n3": "1",
        "Diag_Algorithm": "MRRR",
        "NumberOfEigenStates": "-10"
    }

    if options:
        #Update the dictionary with the provided parameters
        defaults.update(options)


    return  f"""
##-------------------------------------
#   DFT   Control
##-------------------------------------
PAO.BasisSize    {defaults['PAO_BasisSize']}
PAO.EnergyShift  {defaults['PAO_EnergyShift']}
XC.functional    {defaults['XC_functional']}
XC.authors       {defaults['XC_authors']}
MaxSCFIterations {defaults['MaxSCFIterations']}
MeshCutoff       {defaults['MeshCutoff']}
DM.MixingWeight  {defaults['DM_MixingWeight']}
DM.Tolerance     {defaults['DM_Tolerance']}
DM.NumberPulay   {defaults['DM_NumberPulay']}
SolutionMethod   {defaults['SolutionMethod']}
ElectronicTemperature {defaults['ElectronicTemperature']}
Spin   {defaults['Spin']}
DFTD3 {defaults['DFTD3']}
DFTD3.BJdamping  {defaults['DFTD3_BJdamping']}
Diag.Algorithm    {defaults['Diag_Algorithm']}
NumberOfEigenStates {defaults['NumberOfEigenStates']}

%block kgrid_Monkhorst_Pack
    {defaults['n1']}   0     0    0.0
     0    {defaults['n2']}   0    0.0
     0     0    {defaults['n3']}  0.0
%endblock kgrid_Monkhorst_Pack
"""

def relax_fdf(options:dict = None)-> str:
    # Dictionary with default values (can be modified by parameters)
    defaults = {
        "MD_TypeOfRun": "FIRE",
        "MD_steps": "500",
        "MD_VariableCell":"False",
        "MD_MaxForceTol": "0.02 eV/Ang",
        "MD_TargetPressure": "0.0 GPa"
    }
    if options:
        #Update the dictionary with the provided parameters
        defaults.update(options)
    return f"""
##-------------------------------------
#   System  Relax  Control
##-------------------------------------
MD.TypeOfRun {defaults['MD_TypeOfRun']}
MD.Steps {defaults['MD_steps']}
MD.VariableCell {defaults['MD_VariableCell']}
MD.MaxForceTol {defaults['MD_MaxForceTol']}
MD.TargetPressure {defaults['MD_TargetPressure']}

    """

def optical_fdf(options:dict = None)-> str:
    # Dictionary with default values (can be modified by parameters)

    defaults = {
        "OpticalCalculation": "True",
        "Optical_Energy_Minimum": "0 eV",
        "Optical_Energy_Maximum":"15 eV",
        "Optical_Broaden": "0.06 eV",
        "Optical_Scissor": "0 eV",
        "Optical_Mesh": "1 1 1",
        "Optical_OffsetMesh": "false",
        "Optical_PolarizationType": "polarized",
        "Optical_Vector": "0.0 0.0 1.0"
    }

    if options:
        #Update the dictionary with the provided parameters
        defaults.update(options)
    
    return f"""
##-------------------------------------
#   Optical
##-------------------------------------
OpticalCalculation {defaults['OpticalCalculation']}
Optical.Energy.Minimum {defaults['Optical_Energy_Minimum']} 
Optical.Energy.Maximum {defaults['Optical_Energy_Maximum']} 
Optical.Broaden {defaults['Optical_Broaden']}
Optical.Scissor {defaults['Optical_Scissor']}
 
%block Optical.Mesh
 {defaults['Optical_Mesh']}
%endblock Optical.Mesh
Optical.OffsetMesh   {defaults['Optical_OffsetMesh']}
Optical.PolarizationType {defaults['Optical_PolarizationType']}
%block Optical.Vector
{defaults['Optical_Vector']}
%endblock Optical.Vector

    """

def dos_fdf(options:dict = None)-> str:
    # Dictionary with default values (can be modified by parameters)
    defaults = {
        "DOS_vector": "-15.0 6.000 0.06   4000 eV",
        "grid1": "1",
        "grid2": "1",
        "grid3": "1",
    }
    if options:
        #Update the dictionary with the provided parameters
        defaults.update(options)
    return f"""
#-----------------------------------------------------------------------------------------------
#  DOS
#------------------------------------------------------------------------------------------------
%block PDOS.kgrid_Monkhorst_Pack
   {defaults['grid1']}  0  0  0.0
   0  {defaults['grid2']}  0  0.0 
   0  0  {defaults['grid3']}  0.0
%endblock PDOS.kgrid_Monkhorst_Pack

%block ProjectedDensityOfStates
  {defaults['DOS_vector']}
%endblock ProjectedDensityOfStates

    """