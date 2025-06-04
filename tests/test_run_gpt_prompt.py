import importlib.util
import sys
import types
import datetime
import unittest

class ScratchStub:
    def __init__(self):
        self.f_daily_schedule_hourly_org = []
        self.curr_time = datetime.datetime.now()
        self.first_name = "Test"
        self.age = 0
        self.innate = ""
        self.learned = ""
        self.currently = ""
        self.lifestyle = ""
        self.daily_plan_req = ""
        self.name = "Test Person"

    def get_f_daily_schedule_hourly_org_index(self, advance=0):
        return 0

    def get_str_iss(self):
        return "ISS"

    def get_str_firstname(self):
        return self.first_name

class PersonaStub:
    def __init__(self):
        self.name = "Test Person"
        self.scratch = ScratchStub()

class RunGptPromptTaskDecompTest(unittest.TestCase):
    def test_empty_gpt_response(self):
        # Stub dependencies before importing the module
        sys.modules['global_methods'] = types.ModuleType('global_methods')
        gpt_mod = types.ModuleType('persona.prompt_template.gpt_structure')
        gpt_mod.safe_generate_response = lambda *a, **k: []
        gpt_mod.generate_prompt = lambda *a, **k: ""
        sys.modules['persona.prompt_template.gpt_structure'] = gpt_mod
        print_mod = types.ModuleType('persona.prompt_template.print_prompt')
        print_mod.print_run_prompts = lambda *a, **k: None
        sys.modules['persona.prompt_template.print_prompt'] = print_mod

        spec = importlib.util.spec_from_file_location(
            'run_gpt_prompt',
            'reverie/backend_server/persona/prompt_template/run_gpt_prompt.py'
        )
        run_gpt_prompt = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(run_gpt_prompt)
        run_gpt_prompt.debug = False

        persona = PersonaStub()
        output, _ = run_gpt_prompt.run_gpt_prompt_task_decomp(persona, 'task', 30)
        self.assertEqual(output, [])

if __name__ == '__main__':
    unittest.main()
