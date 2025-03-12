from ai.theories_repository import TheoriesRepository

# Create an instance of the repository
repo = TheoriesRepository()

# Get information about the Riemann Hypothesis
rh_info = repo.get_theory_info("Riemann Hypothesis")
print(rh_info)

# Get information about P vs NP
p_vs_np_info = repo.get_theory_info("P vs NP")
print(p_vs_np_info)

# Get information about an unknown theory
unknown_info = repo.get_theory_info("Quantum Gravity?") # Typo, intentionally unknown
print(unknown_info)
