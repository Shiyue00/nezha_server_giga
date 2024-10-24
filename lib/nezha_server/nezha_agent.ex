defmodule NezhaServer.NezhaAgent do
  use GenServer
  require Logger

  def start_link(_) do
    GenServer.start_link(__MODULE__, [], name: __MODULE__)
  end

  def init(_) do
    start_agent()
    {:ok, %{}}
  end

  defp start_agent do
    # Log the current directory for debugging
    Logger.info("Current directory: #{File.cwd!()}")
    
    # Use absolute path in production
    agent_path = Path.join(:code.priv_dir(:nezha_server), "agent")
    Logger.info("Agent path: #{agent_path}")

    case File.chmod(agent_path, 0o755) do
      :ok -> 
        Logger.info("Successfully set agent permissions")
        start_agent_process(agent_path)
      {:error, reason} ->
        Logger.warn("Could not set agent permissions: #{inspect(reason)}")
        {:ok, %{}}
    end
  end

  defp start_agent_process(agent_path) do
    Port.open({:spawn_executable, agent_path},
      args: [
        "-s",
        "tzz.shiyue.eu.org:5555",
        "-p",
        "NsEbJy2O0DZozziVzr",
        "-d"
      ]
    )
  end
end
