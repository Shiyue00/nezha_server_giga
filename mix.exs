defmodule NezhaServer.MixProject do
  use Mix.Project

  def project do
    [
      app: :nezha_server,
      version: "0.1.0",
      elixir: "~> 1.14.0",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  def application do
    [
      extra_applications: [:logger],
      mod: {NezhaServer.Application, []}
    ]
  end

  defp deps do
    [
      {:plug_cowboy, "~> 2.5"}
    ]
  end
end
