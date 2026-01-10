return {
  "ThePrimeagen/harpoon",
  branch = "harpoon2", -- Use the harpoon2 branch for the latest features
  dependencies = { "nvim-lua/plenary.nvim" },
  opts = {
    settings = {
      save_on_toggle = false,
      sync_on_ui_close = false,
    },
  },
  keys = {
    {
      "<leader>a",
      function() require("harpoon"):list():add() end,
      desc = "Harpoon Add File",
    },
    {
      "<C-e>",
      function()
        local harpoon = require("harpoon")
        harpoon.ui:toggle_quick_menu(harpoon:list())
      end,
      desc = "Harpoon Quick Menu",
    },
    {
      "<C-t>",
      function() require("harpoon"):list():select(1) end,
      desc = "Harpoon To File 1",
    },
    {
      "<C-h>",
      function() require("harpoon"):list():select(2) end,
      desc = "Harpoon To File 2",
    },
  },
}

