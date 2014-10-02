import FWCore.ParameterSet.Config as cms

def insertVtxSmeared(process):
  for sequ in process.sequences:
    if sequ == "ProductionFilterSequence":
      getattr(process,sequ)._seq.insert(
          1,
          process.VtxSmeared )
  return process

def customiseVtxSmeared(process):
  process = insertVtxSmeared(process)
  return process
