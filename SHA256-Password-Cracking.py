import hashlib
import sys
from tqdm import tqdm

def calculate_hash(data, algorithm="sha256"):
	hash_obj = hashlib.new(algorithm)
	hash_obj.update(data)
	return hash_obj.hexdigest()

if len(sys.argv) < 2 or len(sys.argv) > 3:
	print("Right use: ")
	print(">> python {} <hash> [algorithm]".format(sys.argv[0]))
	print("Default algorithm is sha256, options: sha256, sha1, md5")
	sys.exit(1)

wanted_hash = sys.argv[1]

algorithm = sys.argv[2] if len(sys.argv) == 3 else "sha256"

valid_algorithm = hashlib.algorithms_available
if algorithm not in valid_algorithm:
	print(f"Algorithm {algorithm} is not supported. Use one of: {', '.join(sorted(valid_algorithm))}")
	sys.exit(1)

password_file_path = "rockyou.txt"

try:
	attempts = 0
	with open(password_file_path, "r", encoding="latin-1") as f:
		for line in tqdm(f, desc="Try passwords", unit="password"):
			password = line.strip().encode("latin-1")
			password_hash = calculate_hash(password, algorithm)
			attempts += 1

			if password_hash == wanted_hash:
				print(f"\nPassword found after {attempts} attempts '{password.decode('latin-1')}' hash {wanted_hash}")
				sys.exit(0)

	print("Password not found!")

except FileNotFoundError:
	print(f"File {password_file_path} not found. add the file path on script")
except Exception as e:
	print(f"Error: {e}")
