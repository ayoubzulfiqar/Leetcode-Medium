class Solution:
    def digArtifacts(self, n: int, artifacts: list[list[int]], dig: list[list[int]]) -> int:
        cell_to_artifact_id = {}
        total_cells_per_artifact = [0] * len(artifacts)
        uncovered_counts = [0] * len(artifacts)

        for artifact_id, (r1, c1, r2, c2) in enumerate(artifacts):
            current_artifact_cells_count = 0
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    cell_to_artifact_id[(r, c)] = artifact_id
                    current_artifact_cells_count += 1
            total_cells_per_artifact[artifact_id] = current_artifact_cells_count

        for dr, dc in dig:
            if (dr, dc) in cell_to_artifact_id:
                artifact_id = cell_to_artifact_id[(dr, dc)]
                uncovered_counts[artifact_id] += 1

        extracted_artifacts_count = 0
        for artifact_id in range(len(artifacts)):
            if uncovered_counts[artifact_id] == total_cells_per_artifact[artifact_id]:
                extracted_artifacts_count += 1

        return extracted_artifacts_count