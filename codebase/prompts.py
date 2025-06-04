sys_prompt = "You are a highly skilled assistant specializing in converting structured and semi-structured data into clean, valid JSON format. Your focus is on accuracy, clarity, and preserving the logical structure of the input data. You ensure the output adheres strictly to JSON syntax rules and best practices."

prompt = f"""Convert the provided data into a well-structured, valid JSON format. Follow these rules and guidelines carefully:

    1. Accuracy and Structure:
    Maintain the logical organization of sections, sub-sections, tables, and lists.
    Use appropriate nesting to reflect the hierarchy of the content.

    2. Formatting Rules:
    Strictly avoid long paragraphs in values. 
    Always split content into smaller, descriptive key-value pairs.
    Use double quotes for all keys and string values as required by JSON standards.
    If a string contains quotation marks, retain double quotes outside and use single quotes inside, e.g.,
     \"Example string 'should' be like this\".

    3.  Clean Output:
    Do not include escape characters like \
    , \	, or unnecessary \\\\ unless they are intentionally part of the content.
    Eliminate any backslashes (\\) used for escaping inappropriately.
    Represent multiline content as arrays of strings or structured objects where appropriate.

    4. Tables:
    Convert tabular data into arrays of objects with clear column headers as keys.

    5. Validation:
    Ensure the final output is valid JSON and can be parsed without errors.

    Data:

    {data}

    Output JSON:"""