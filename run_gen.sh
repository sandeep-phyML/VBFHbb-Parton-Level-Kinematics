cmsDriver.py Configuration/GenProduction/python/VBF_HToBB_GEN_fragment_13_6_annote.py \
    --python_filename VBF_HToBB_GEN_13p6TeV_GEN_cfg.py \
    --eventcontent RAWSIM,LHE \
    --customise Configuration/DataProcessing/Utils.addMonitoring \
    --datatier GEN,LHE \
    --fileout file:VBF_HToBB_GEN_13p6TeV_GEN.root \
    --conditions 124X_mcRun3_2022_realistic_postEE_v1 \
    --beamspot Realistic25ns13p6TeVEarly2022Collision \
    --customise_commands "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=1" \
    --step LHE,GEN \
    --era Run3 \
    --mc \
    --no_exec \
    -n 100
cmsRun VBF_HToBB_GEN_13p6TeV_GEN_cfg.py

