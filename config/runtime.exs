import Config

config :nezha_server, port: String.to_integer(System.get_env("PORT") || "4000")
