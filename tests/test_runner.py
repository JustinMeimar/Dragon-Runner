from dragon_runner.harness import RegularHarness
from dragon_runner.config import Config
from dragon_runner.cli import CLIArgs

def test_gcc_pass(config_factory, cli_factory):

    config : Config = config_factory("gccPassConfig.json")
    args : CLIArgs = cli_factory(**{
        "mode": "regular",
        "timeout": 5
    })
    
    harness = RegularHarness(config=config, cli_args=args) 
    assert harness is not None 
    success = harness.run()
    assert success == True

def test_gcc_pass_darwin(config_factory, cli_factory):

    config : Config = config_factory("catConfigDarwin.json")
    args : CLIArgs = cli_factory(**{
        "mode": "regular",
        "timeout": 5
    })
    
    harness = RegularHarness(config=config, cli_args=args) 
    assert harness is not None 
    success = harness.run()
    assert success == True

def test_gcc_fail(config_factory, cli_factory):

    config : Config = config_factory("gccFail.json")
    args : CLIArgs = cli_factory(**{
        "mode": "regular",
        "timeout": 5
    })
    
    harness = RegularHarness(config=config, cli_args=args) 
    assert harness is not None 
    success = harness.run()
    assert success == False

