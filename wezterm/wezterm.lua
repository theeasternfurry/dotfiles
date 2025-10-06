local wezterm = require 'wezterm'

local config = wezterm.config_builder()

config.default_prog = { 'fish' }
config.font_size = 12
config.font = wezterm.font('VictorMono Nerd Font')

return config
