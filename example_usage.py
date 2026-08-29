from client import AgentComputerInterfaceSwePatchSynthesizerClient

def main():
    client = AgentComputerInterfaceSwePatchSynthesizerClient()
    res = client.solve_swe_issue('Fix race condition in redis connection handshake timeout', '/repo/redis-py')
    print('SWE Patch Session: ' + res['patch_session_id'] + ' | Repo: ' + res['target_repo'])
    print('ACI Commands: ' + str(res['aci_navigation_commands_executed']) + ' | Diff Lines: ' + str(res['diff_patch_synthesized_lines']))
    print('Regression Tests: ' + str(res['regression_test_suite_passed']) + ' | Issue Resolved: ' + str(res['swe_benchmark_resolved']))
    print('Diff URL: ' + res['patch_diff_url'])

if __name__ == '__main__':
    main()
