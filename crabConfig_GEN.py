from CRABClient.UserUtilities import config
import os
config = config()

config.General.requestName = 'VBF_HToBB_GEN_13p6TeV_GEN_v1'
config.General.workArea = 'crab_projects_GEN'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'VBF_HToBB_GEN_13p6TeV_GEN_cfg.py'
config.JobType.outputFiles = ['VBF_HToBB_GEN_13p6TeV_GEN.root']
#config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = 'VBF_HToBB_GEN_13p6TeV'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000   # events per job
NJOBS = 1000                     # total 1M events
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

# 👇 Output path on EOS home area
config.Data.outLFNDirBase = '/store/user/sapradha/PhD_Projects/VBF_analysis/Parton_Kinematic_Study/CMSSW_12_4_11_patch3/src/OUTPUT/'  # logical storage area (kept as-is)
#/eos/home-s/sapradha/PhD_Projects/VBF_analysis/Parton_Kinematic_Study/CMSSW_12_4_11_patch3/src/OUTPUT
# 👇 Physical destination (maps to your CERNBox area)
config.Site.storageSite = 'T3_CH_CERNBOX'

