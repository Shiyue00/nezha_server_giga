defmodule NezhaServer.NezhaAgent do
  use GenServer

  def start_link(_) do
    GenServer.start_link(__MODULE__, [], name: __MODULE__)
  end

  def init(_) do
    start_agent()
    {:ok, %{}}
  end

  defp start_agent do
    agent_path = "./agent"
    File.chmod!(agent_path, 0o755)

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
