import FWCore.ParameterSet.Config as cms

def insertVtxSmeared(process):
  for sequ in process.sequences:
    if sequ == "ProductionFilterSequence":
      getattr(process,sequ)._seq.insert(
          1,
          process.VtxSmeared )
  return process

def changeBeta(process):
  process.VtxSmeared.Beta = cms.double(0.434)
  return changeBeta

def customiseVtxSmeared(process):
  process = insertVtxSmeared(process)
  changeBeta(process)
  return process
