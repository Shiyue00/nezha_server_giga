defmodule NezhaServer.Application do
  use Application

  def start(_type, _args) do
    children = [
      {Plug.Cowboy, scheme: :http, plug: NezhaServer.Router, options: [port: 8080]},  
      {NezhaServer.NezhaAgent, []}
    ]

    opts = [strategy: :one_for_one, name: NezhaServer.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
