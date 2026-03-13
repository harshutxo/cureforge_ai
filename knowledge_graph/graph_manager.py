import networkx as nx
from .schema import Node, Edge, NodeType, EdgeType

class KnowledgeGraphManager:
    """
    Manages the longevity knowledge graph using NetworkX backend.
    Links Genes, Pathways, Drugs, and Diseases.
    """
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node: Node):
        self.graph.add_node(node.id, **node.model_dump())
        
    def add_edge(self, edge: Edge):
        self.graph.add_edge(edge.source_id, edge.target_id, **edge.model_dump())

    def reason_path(self, source_id: str, target_id: str):
        """
        Example reasoning chain: Drug -> Pathway -> Disease Risk -> Impact
        """
        try:
            paths = list(nx.shortest_simple_paths(self.graph, source_id, target_id))
            if not paths:
                return "No logical path found."
            return paths[0]
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return "No logical path found."

    def build_dummy_graph(self):
        """Build a sample graph for the 5-step Longevity reasoning."""
        # Nodes
        drug = Node(id="dr_01", type=NodeType.DRUG, name="Rapamycin")
        pathway = Node(id="pw_01", type=NodeType.BIOLOGICAL_PATHWAY, name="mTOR Inhibition")
        disease = Node(id="dz_01", type=NodeType.DISEASE, name="Metabolic syndrome")
        biomarker = Node(id="bm_01", type=NodeType.BIOMARKER, name="Glucose tolerance")

        for n in [drug, pathway, disease, biomarker]:
            self.add_node(n)

        # Edges
        self.add_edge(Edge(source_id="dr_01", target_id="pw_01", type=EdgeType.INHIBITION))
        self.add_edge(Edge(source_id="pw_01", target_id="bm_01", type=EdgeType.CAUSAL_RELATIONSHIP))
        self.add_edge(Edge(source_id="bm_01", target_id="dz_01", type=EdgeType.ASSOCIATION))
        
        print("[Knowledge Graph] Initialized with longevity base nodes.")
