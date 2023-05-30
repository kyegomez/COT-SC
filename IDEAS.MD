
Architectural Overview:

Prompt a language model using chain-of-thought (CoT) prompting.
Sample from the language model's decoder to generate a diverse set of reasoning paths.
For each rejected path, store the reason for rejection.
Use the rejection reasons to influence the evaluation of other paths.
Marginalize out the reasoning paths and aggregate by choosing the most consistent answer in the final answer set.
Algorithmic Pseudocode:

function self_consistency(prompt, question, language_model, num_samples):
    sampled_outputs = sample_outputs(prompt, question, language_model, num_samples)
    rejection_reasons = get_rejection_reasons(sampled_outputs)
    adjusted_outputs = adjust_outputs(sampled_outputs, rejection_reasons)
    aggregated_answers = aggregate_answers(adjusted_outputs)
    most_consistent_answer = find_most_consistent_answer(aggregated_answers)
    return most_consistent_answer
Python Implementation:

def get_rejection_reasons(sampled_outputs: List[Tuple[str, str]]) -> Dict[str, Any]:
    rejection_reasons = {}
    for output in sampled_outputs:
        reasoning_path, answer = output
        reason = check_rejection_reason(reasoning_path, answer)
        if reason:
            rejection_reasons[reasoning_path] = reason
    return rejection_reasons

def check_rejection_reason(reasoning_path: str, answer: str) -> Optional[Any]:
    # Implement a function to check the reason for rejection of a reasoning path
    pass

def adjust_outputs(sampled_outputs: List[Tuple[str, str]], rejection_reasons: Dict[str, Any]) -> List[Tuple[str, str]]:
    adjusted_outputs = []
    for output in sampled_outputs:
        reasoning_path, answer = output
        if reasoning_path not in rejection_reasons:
            adjusted_outputs.append(output)
        else:
            adjusted_reasoning_path = adjust_reasoning_path(reasoning_path, rejection_reasons)
            adjusted_outputs.append((adjusted_reasoning_path, answer))
    return adjusted_outputs

def adjust_reasoning_path(reasoning_path: str, rejection_reasons: Dict[str, Any]) -> str:
    # Implement a function to adjust the reasoning path based on rejection reasons
    pass

def self_consistency(prompt: str, question: str, language_model, num_samples: int) -> str:
    sampled_outputs = sample_outputs(prompt, question, language_model, num_samples)
    rejection_reasons = get_rejection_reasons(sampled_outputs)
    adjusted_outputs = adjust_outputs(sampled_outputs, rejection_reasons)
    aggregated_answers = aggregate_answers(adjusted_outputs)
    most_consistent_answer = find_most_consistent_answer(aggregated_answers)
    return most_consistent_answer
Copy code
This implementation follows the architectural overview and pseudocode provided. Note that the check_rejection_reason and adjust_reasoning_path functions need to be implemented based on the specific criteria for rejection and how to adjust the reasoning paths. The language_model parameter in the self_consistency function should be an instance of a pre-trained language model that has a generate method for generating text.

