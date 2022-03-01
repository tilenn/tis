from pathlib import Path
from timeit import default_timer as timer
import json
from naloga1 import naloga1


def test_naloga1(case_dir, case_id):
    """
    Funkcija za preverjanje naloge 1.
    Primer zagona:
    from test_naloga1 import test_naloga1
    test_naloga1('primeri',1)
    """
    base_path = Path(__file__).parent
    file_path = (base_path / str(case_dir) / (str(case_id) + ".json")).resolve()
    json_file = open(file_path, "r", encoding="utf8")
    tol = 1e-3
    data = json.load(json_file, strict=False)
    start = timer()
    H = naloga1(data["besedilo"], data["p"])
    end = timer()
    success = abs(H - data["H"]) < tol
    print(
        "Rezultat za primer",
        case_id,
        ":",
        success,
        ";",
        "Izracunani H:",
        H,
        ";",
        "Pravi H:",
        float(data["H"]),
    )
    print(f"Cas izvajanja: {end-start:.2f} s")


# print("TESTNI PRIMERI")
# test_naloga1("./primeri", 1)
# test_naloga1("./primeri", 2)
# test_naloga1("./primeri", 3)
# test_naloga1("./primeri", 4)
# test_naloga1("./primeri", 5)

print("SKRITI TESTNI PRIMERI")
for i in range(1, 11):
    test_naloga1("./primeri_skriti", i)
