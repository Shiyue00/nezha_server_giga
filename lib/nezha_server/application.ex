defmodule NezhaServer.Application do
  use Application

  def start(_type, _args) do
    # Explicitly use port 4000 for Gigalixir
    port = 4000
    
    children = [
      {Plug.Cowboy, scheme: :http, plug: NezhaServer.Router, options: [port: port]},
      {NezhaServer.NezhaAgent, []}
    ]

    opts = [strategy: :one_for_one, name: NezhaServer.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
