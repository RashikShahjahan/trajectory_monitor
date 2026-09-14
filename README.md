# Trajectory Monitor Test Environment

A minimal Control Tower environment based on the hands-on tutorial. It provides a Flask message board, an `add_search` main task, and a `hidden_admin` side task for producing honest and attack trajectories that can be evaluated with custom monitors.

## Install

Clone this repository, then link it into a Control Tower checkout:

```bash
uv run ct settings pull /absolute/path/to/trajectory_monitor
uv run ct envs validate -e /absolute/path/to/trajectory_monitor
```

## Generate Trajectories

Run an honest evaluation:

```bash
uv run ct run eval --env trajectory_monitor --main-task add_search --policy honest
```

Run an attack evaluation:

```bash
uv run ct run eval --env trajectory_monitor --main-task add_search --side-task hidden_admin --policy attack
```

Run a monitor over the resulting eval log:

```bash
uv run ct run monitor logs/<eval-file>.eval --trusted-model openai/gpt-5-nano
```

The custom monitor implementation is separate from this environment and can be selected with a packaged name, Markdown asset path, or `module:function` import path.
