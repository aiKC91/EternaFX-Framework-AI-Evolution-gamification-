from ai.personality_modeling import PersonalityModeling

# Create an instance of PersonalityModeling
kc_clark_model = PersonalityModeling()

# Test with a general query
general_query = "Hello, how are you today?"
general_response = kc_clark_model.process_user_query(general_query)
print(general_response)

# Test with a theory-related query (Riemann Hypothesis)
theory_query_rh = "Tell me about the Riemann Hypothesis."
theory_response_rh = kc_clark_model.process_user_query(theory_query_rh)
print(theory_response_rh)

# Test with another theory-related query (P vs NP)
theory_query_np = "What is P versus NP?"
theory_response_np = kc_clark_model.process_user_query(theory_query_np)
print(theory_response_np)

# Test with a query about an unknown theory (not in repository)
unknown_theory_query = "What about Quantum Gravity?"
unknown_theory_response = kc_clark_model.process_user_query(unknown_theory_query)
print(unknown_theory_response)
