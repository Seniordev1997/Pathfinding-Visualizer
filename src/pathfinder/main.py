from .search.astar import AStarSearch
from .search.bfs import BreadthFirstSearch
from .search.dfs import DepthFirstSearch
from .search.dijkstras import DijkstrasSearch
from .models.grid import Grid
from .models.solution import Solution
from .models.search_types import Search
from .models.search_types import Search
from .types import SearchFunction, Visualiser

SEARCH: dict[Search, SearchFunction] = {
    Search.ASTAR_SEARCH: AStarSearch.search,
    Search.DIJKSTRAS_SEARCH: DijkstrasSearch.search,
    Search.BREADTH_FIRST_SEARCH: BreadthFirstSearch.search,
    Search.DEPTH_FIRST_SEARCH: DepthFirstSearch.search,
}


class PathFinder:
    @staticmethod
    def find_path(
            grid: Grid,
            search: Search,
            callback: Visualiser | None = None
    ) -> Solution:
        return SEARCH[search](grid=grid, callback=callback)
