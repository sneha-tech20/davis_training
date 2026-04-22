def error_report(input_file, output_file):
    errors = {}

    with open(input_file, 'r') as f:
        for line in f:
            error_type = line.strip().split(':')[0]
            errors[error_type] = errors.get(error_type, 0) + 1

    with open(output_file, 'w') as f:
        for k, v in errors.items():
            f.write(f"{k}: {v}\n")