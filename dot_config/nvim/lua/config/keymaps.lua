-- netrw settings
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex, { desc="Open NetRW" })

-- Set highlight on search and clear on pressing escape
vim.opt.hlsearch = true
vim.keymap.set("n", "<Esc>", "<cmd>nohlsearch<CR>")
