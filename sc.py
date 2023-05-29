import random
from collections import Counter
from typing import List, Tuple

def sample_outputs(prompt: str, question: str, language_model, num_samples: int) -> List[Tuple[str, str]]:
    sampled_outputs = []
    for _ in range(num_samples):
        output = language_model.generate(prompt, question)
        reasoning_path, answer = parse_output(output)
        sampled_outputs.append((reasoning_path, answer))
    return sampled_outputs

def parse_output(output: str) -> Tuple[str, str]:
    # Implement a function to parse the output into reasoning_path and answer
    pass

def aggregate_answers(sampled_outputs: List[Tuple[str, str]]) -> List[str]:
    answers = [output[1] for output in sampled_outputs]
    return answers

def find_most_consistent_answer(aggregated_answers: List[str]) -> str:
    counter = Counter(aggregated_answers)
    most_consistent_answer, _ = counter.most_common(1)[0]
    return most_consistent_answer

def self_consistency(prompt: str, question: str, language_model, num_samples: int) -> str:
    sampled_outputs = sample_outputs(prompt, question, language_model, num_samples)
    aggregated_answers = aggregate_answers(sampled_outputs)
    most_consistent_answer = find_most_consistent_answer(aggregated_answers)
    return most_consistent_answer