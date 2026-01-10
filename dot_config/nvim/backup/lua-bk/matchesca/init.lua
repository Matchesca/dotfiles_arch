-- Set line numbers
vim.opt.number = true
vim.opt.relativenumber = true

-- Scroll settings
vim.opt.scrolloff = 10

-- Set highlight on search and clear on pressing escape
vim.opt.hlsearch = true
vim.keymap.set("n", "<Esc>", "<cmd>nohlsearch<CR>")
