def clean_data(input_file, output_file):
    with open(input_file, 'r') as f, open(output_file, 'w') as out:
        for line in f:
            parts = line.strip().split(',')

            cleaned = []
            for val in parts:
                val = val.strip()

                if not val:
                    continue

                try:
                    val = int(val)
                except:
                    pass

                cleaned.append(str(val))

            if cleaned:
                out.write(','.join(cleaned) + '\n')