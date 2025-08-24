"""
Generator Module
----------------
Handles response generation using an LLM (e.g., OpenAI GPT).
"""

from openai import OpenAI

class Generator:
    def __init__(self, model_name: str = "gpt-4o-mini", api_key: str = None):
        """
        Initialize LLM Generator.

        Args:
            model_name (str): LLM model to use.
            api_key (str): API key for provider.
        """
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name

    def generate(self, query: str, context_docs: list) -> str:
        """
        Generate a domain-specific answer using retrieved context.

        Args:
            query (str): User query.
            context_docs (list): Retrieved documents.

        Returns:
            str: LLM-generated response.
        """
        context_text = "\n".join([doc.payload.get("content", "") for doc in context_docs])

        prompt = f"""
        You are an expert in the {self.model_name} domain.
        Answer the following question using the provided context.

        Question: {query}

        Context:
        {context_text}

        Answer:
        """

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()
