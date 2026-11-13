"""Owner-approved connection helper; requires the separately installed cloudgpu SDK."""
import sys

def main():
    try:
        from cloudgpu.__main__ import main as connect
    except ImportError:
        raise SystemExit('Install the reviewed CloudGPU Python SDK first; see README. No API key is required in this command.') from None
    sys.argv=[sys.argv[0],'connect',*sys.argv[1:],'--hermes']
    connect()
if __name__=='__main__':main()
