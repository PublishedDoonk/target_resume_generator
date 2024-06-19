import json
import keyring

"""
This is the base class for all language models in Magic Mink. It contains the basic structure for all language models
Please feel free to extend this object to include any other unsupported language model you like. Example:

class MyRadLanguageModel(LanguageModel):
    def __init__(self, instructions: str, sample_outputs: list | None = None, schema: dict | None = None, prev_messages: list | None = None):
        super().__init__(instructions, sample_outputs, schema, prev_messages)
        
    def prompt_model(self: MyRadLanguageModel, prompt: str) -> str | dict | None:
        # implement the logic to prompt your model here, the response will be returned to the prompt method to be returned to the user
        # this is where any kind of API handling logic should be implemented
"""

class LanguageModel:
    
    def __init__(self, instructions: str, sample_outputs: list | None = None, schema: dict | None = None, prev_messages: list | None = None):
        # stores formatted instructions, outputs, schema, and previous messages
        self.instructions = self.get_instructions(instructions, sample_outputs, schema)
        self.prev_messages = []
        self.schema = schema
        if prev_messages and type(prev_messages) == list:
            self.prev_messages = prev_messages
    
    def import_key_from_keyring(self, key: str) -> str:
        # returns the value for the key {key} from the keyring
        # this should be used to load API key for the model, if needed
        return keyring.get_password('magic_mink', key)

    def get_instructions(self, instructions: str, sample_outputs: list | None, schema: dict | None):
        # formats the instructions, sample_outputs, schema, and previous messages in a uniform way
        output_instrucs, schema_instrucs = '', ''
        if sample_outputs and type(sample_outputs) == list:
            output_instrucs = '\n\n'.join([f'Sample Output {i+1}:\n{json.dumps(s)}' for i, s in enumerate(sample_outputs)])
        if schema and type(schema) == dict:
            schema_instrucs = f' Return your output as a correct JSON string. It should be loadable with the python command json.loads(output).\n\nOutput Schema:\n{json.dumps(schema)}'
        instructions = instructions + schema_instrucs + output_instrucs
        return [{'role': 'system', 'content': instructions}] 
    
    def prompt(self, prompt: str, retries: int = 3) -> str | dict | None:
        # prompts the model with the given input and returns the response based on stored instructions
        # implement specific prompting logic in the child class with prompt_model function
        for _ in range(retries):
            try:
                response = self.prompt_model(prompt)
                return response
            except Exception as e:
                pass
        #print('Failed to return output.')
        return None
                
    def prompt_model(self, prompt: str) -> str | dict | None:
        """
            This method should include the actual logic to reach out to the language
            model and return a response. Usually, I have the output returned from the 
            request to the model API either converted to JSON with json.loads or return 
            the string content of the response directly. Depends on your use case.
            
            Your model may require an API key. Use the mink loadenv action to import the key
            from a .env file. Example:
            
            - mink loadenv -f path/to/.env
            
            The mink loadenv method will permanently save your keys in the keyring, so you
            do not need the .env file anymore after importing.
            
            The keys in the .env file should be in the format API_KEY=your_key
            mink loadenv will automatically import all the key/value pairs from the .env file
            and securely store it in the keyring using your OS's secure key storage.
            
            After storing the API key in the keyring, you can access it using the
            self.load_key_from_keyring(key) method. Example:
            
            .env file includes OPENAI_API_KEY=your_key
            mink loadenv -f path/to/.env
            self.load_key_from_keyring('OPENAI_API_KEY')
            
            - .env file should contain API_KEY=your_key
        
        """
        pass
