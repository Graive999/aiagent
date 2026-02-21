import os
import subprocess
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python script in the sandbox",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(type=types.Type.STRING, description="Script to run"),
            "args": types.Schema(
                type=types.Type.ARRAY, 
                items=types.Schema(type=types.Type.STRING),
                description="Optional CLI arguments"
            )
        },
        required=["file_path"]
    ),
)




def run_python_file(working_directory, file_path, args=None):
    try:
        
        working_dir_abs = os.path.abspath(working_directory)
        target_file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        if os.path.commonpath([working_dir_abs, target_file_abs]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        
        if not os.path.isfile(target_file_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'


        
        command = ["python", target_file_abs]
        if args:
            command.extend(args)

        
        result = subprocess.run(
            command,
            cwd=working_dir_abs, 
            capture_output=True, 
            text=True,           
            timeout=30           
        )

        output = ""
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        
        if not result.stdout and not result.stderr:
            output += "No output produced"
        else:
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}"
        
        return output.strip()

    except Exception as e:
        return f"Error: executing Python file: {e}"


