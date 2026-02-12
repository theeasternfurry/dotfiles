local wezterm = require 'wezterm'

local config = wezterm.config_builder()

config.default_prog = { 'fish' }
config.font_size = 12
config.font = wezterm.font('VictorMono Nerd Font')

local hour = tonumber(wezterm.time.now():format("%H"))

if hour >= 6 and hour < 18 then
    config.color_scheme = 'Rosé Pine Dawn (Gogh)'
else
    config.color_scheme = 'Rosé Pine Moon (Gogh)'
end

return config
