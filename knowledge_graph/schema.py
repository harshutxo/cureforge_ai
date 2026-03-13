from enum import Enum
from pydantic import BaseModel

class NodeType(Enum):
    GENE = "Gene"
    PROTEIN = "Protein"
    BIOLOGICAL_PATHWAY = "Biological Pathway"
    DRUG = "Drug"
    BIOMARKER = "Biomarker"
    DISEASE = "Disease"
    CLINICAL_TRIAL = "Clinical Trial"

class EdgeType(Enum):
    ACTIVATION = "Activation"
    INHIBITION = "Inhibition"
    ASSOCIATION = "Association"
    CLINICAL_EVIDENCE = "Clinical Evidence"
    CAUSAL_RELATIONSHIP = "Causal Relationship"

class Node(BaseModel):
    id: str
    type: NodeType
    name: str
    metadata: dict = {}

class Edge(BaseModel):
    source_id: str
    target_id: str
    type: EdgeType
    weight: float = 1.0
    metadata: dict = {}
