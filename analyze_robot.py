from robot.api import ExecutionResult
import glob
import json

#xml_file = glob.glob("**/output.xml", recursive=True)[0]
xml_file = glob.glob("logs/output.xml")

result = ExecutionResult(xml_file)

# Statistics
total = result.suite.statistics.total
passed = result.suite.statistics.passed
failed = result.suite.statistics.failed

print(f"Total Tests : {total}")
print(f"Passed      : {passed}")
print(f"Failed      : {failed}")

failures = []

def collect_failures(suite):
    for test in suite.tests:
        if test.status == "FAIL":
            failures.append({
                "name": test.longname,
                "message": test.message
            })

    for child in suite.suites:
        collect_failures(child)

collect_failures(result.suite)

print("\nFailed Test Details:")
for f in failures:
    print(f"\nTest: {f['name']}")
    print(f"Message: {f['message']}")

# Optional JSON output
summary = {
    "total": total,
    "passed": passed,
    "failed": failed,
    "failures": failures
}

with open("robot_summary.json", "w") as fp:
    json.dump(summary, fp, indent=2)
