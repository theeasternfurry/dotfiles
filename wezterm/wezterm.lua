local wezterm = require 'wezterm'

local config = wezterm.config_builder()

config.default_prog = { 'fish' }
config.font_size = 11.5
config.font = wezterm.font('VictorMono Nerd Font')
config.hide_tab_bar_if_only_one_tab = true

config.color_scheme = "Noctalia"

return config
